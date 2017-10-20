import requests
import time
import random

data1 = '{"head":{"sessionid":"undefined","seqid":null},"body":{"param1":{"basetype":0},"param2":{"basetype":false},"param3":{"basetype":xx},"eventid":"camerapreset"}}'
for i in range(1,5000000):
	a = random.randint(0,119)
	re = requests.post("http://192.168.60.23/mtapi/camera/camerapreset",data=data1.replace('xx',str(a)))
	time.sleep(2)