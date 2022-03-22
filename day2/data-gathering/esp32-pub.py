
# publishing ESP32 Sensory Feed

import paho.mqtt.client as mqtt
import random as sensor
import time

client=mqtt.Client()

while True:
    h=sensor.randint(20,100)
    t=sensor.randint(25,50)
    k={}
    k['humidity']=h
    k['temperature']=t
    print(k)
    client.connect('broker.hivemq.com',1883)
    print('Broker Connected')
    client.publish('gpcet/ai',str(k))
    print('Data Sent')
    time.sleep(4)