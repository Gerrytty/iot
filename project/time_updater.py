from kafka import KafkaConsumer
import json
from threading import Thread


class TimeUpdater:
    def __init__(self, topic_name, bootstrap_servers):
        self.time_to_alarm = None
        self.consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers)

    def consume_and_update(self):
        while True:
            for message in self.consumer:
                print(message)
                msg = json.loads(message.value.decode("utf-8"))
                self.time_to_alarm = msg["time_to_alarm"]
                print(self.time_to_alarm)

    def endless_consume(self):
        new_thread = Thread(target=self.consume_and_update)
        new_thread.start()