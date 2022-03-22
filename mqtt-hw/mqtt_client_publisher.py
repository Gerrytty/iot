import paho.mqtt.client as mqtt
import time
import configparser
import subprocess
import re

if __name__ == "__main__":
	config = configparser.RawConfigParser()
	config.read('ConfigFile.properties')

	client = mqtt.Client("team1")
	client.connect(host=config.get('Broker', 'broker_address'), port=int(config.get('Broker', 'broker_port')))

	while True:
		result = subprocess.run(["sensors"], stdout=subprocess.PIPE)
		result = re.search("ntemp.*", str(result.stdout)).group(0).replace(" ", "")[7:10]
		client.publish("itis/team1", str(result))
		time.sleep(5)