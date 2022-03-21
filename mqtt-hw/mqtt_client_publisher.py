import paho.mqtt.client as mqtt
import time
import configparser

if __name__ == "__main__":
	config = configparser.RawConfigParser()
	config.read('broker.properties')

	client = mqtt.Client("yuliya")
	client.connect(host=config.get('Broker', 'broker_address'), port=int(config.get('Broker', 'broker_port')))

	while True:
		client.publish("house/light", "ON")
		time.sleep(5)