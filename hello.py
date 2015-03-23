#!/usr/bin/python
import paho.mqtt.client as mqtt
mqttc = mqtt.Client(client_id="1046")
mqttc.username_pw_set("Louis", password="xxxxxxxx")

import time
counter = 0
while counter<20:
	time.sleep(3)
	print "hello python!"
	mqttc.connect("opensensors.io")
	mqttc.publish("/users/Louis/test2", payload="Hello Opensensors!", qos=0, retain=False)
	mqttc.disconnect();
	
	counter += 1
	print counter
