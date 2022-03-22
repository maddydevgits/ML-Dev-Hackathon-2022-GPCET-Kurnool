import pandas as pd
import paho.mqtt.client as mqtt

client=mqtt.Client()
client.connect('broker.hivemq.com',1883)
print('Broker Connected')

client.subscribe('gpcet/ai')

count=0
data=[]
def notification(sub_client,userdata,msg):
	global data,count
	k=msg.payload.decode('utf-8')
	k=k.split(': ')
	h=int(k[1].split(',')[0])
	t=int(k[-1][:-1])
	#print(h,t)
	label=0
	if (h>40 and h<=60):
		label=1 
	elif(h>60 and h<=80):
		label=2
	elif(h>80 and h<=100):
		label=3
	else:
		label=0
	#print(h,t,label)
	dummy=[] # [20,50,0]
	dummy.append(h)
	dummy.append(t)
	dummy.append(label)
	data.append(dummy)
	print(data)
	count+=1
	if(count==300):
		df=pd.DataFrame(data)
		df.to_csv('dataset.csv')
		count=0


client.on_message=notification
client.loop_forever()