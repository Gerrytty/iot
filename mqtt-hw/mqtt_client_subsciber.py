import paho.mqtt.client as mqtt
import time
import configparser

class Message:
	def __init__(self, message):
		self.message = str(message.payload.decode("utf-8"))
		self.topic = message.topic
		self.qos = message.qos
		self.flag = message.retain

def on_message(client, userdata, message):
    msg = Message(message)
    print(msg.message)
    return msg

if __name__ == "__main__":
	config = configparser.RawConfigParser()
	config.read('ConfigFile.properties')

	client = mqtt.Client("subscriber")
	client.on_message = on_message

	client.connect(config.get('Broker', 'broker_address'), port=int(config.get('Broker', 'broker_port')))
	client.subscribe("itis/team1")
	client.loop_start()

	try:
	  while True:
	    pass
	except KeyboardInterrupt:
	  client.loop_stop()