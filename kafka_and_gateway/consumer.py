from kafka import KafkaConsumer

if __name__ == "__main__":
    consumer = KafkaConsumer('topic_1', bootstrap_servers=['localhost:9092'])
    for message in consumer:
        print (message.value.decode("utf-8"))