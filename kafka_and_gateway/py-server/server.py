import logging
from concurrent.futures import ThreadPoolExecutor
from confluent_kafka.admin import AdminClient
from confluent_kafka import Producer

import grpc

from service_pb2 import MyMessage
from service_pb2_grpc import EchoServicer, add_EchoServicer_to_server


class KafkaProducer:
    def __init__(self, bootstrap_server):
        self.bootstrap_server = bootstrap_server
        self.producer = Producer({'bootstrap.servers': self.bootstrap_server})

    def produce(self, source_data, topic):
        def delivery_report(err, msg):
            if err is not None:
                print(f'Message delivery failed: {err}')
            else:
                message_string = msg.value().decode("utf-8")
                print(f'Message delivered: "{message_string}" to {msg.topic()} [partition {msg.partition()}]')

        for data in source_data:
            self.producer.poll(0)
            self.producer.produce(topic, data.encode('utf-8'), callback=delivery_report)

        r = self.producer.flush(timeout=5)
        if r > 0:
            print(f'Message delivery failed ({r} message(s) still remain, did we timeout sending perhaps?)\n')


class OutliersServer(EchoServicer):

    def __init__(self, bootstrap_server):
        self.admin_client = AdminClient({'bootstrap.servers': bootstrap_server})
        self.kafka_producer = KafkaProducer(bootstrap_server)

    def SendEcho(self, request, context):
        try:
            self.admin_client.list_topics(timeout=10)
            self.kafka_producer.produce([request.msg], "topic_1")
        except Exception as e:
            print("Failed to connect to bootstrap server")

        return MyMessage(msg=f"{request.msg}")


if __name__ == '__main__':
    server = grpc.server(ThreadPoolExecutor())
    add_EchoServicer_to_server(OutliersServer("localhost:9092"), server)
    port = 9999
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    logging.info('server ready on port %r', port)
    server.wait_for_termination()