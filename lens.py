import time
import requests
data1='{"head":{"sessionid":"undefined","seqid":null},"body":{"param1":{"basetype":0},"param2":{"basetype":false},"param3":{"basetype":2},"eventid":"camerazoom"}}'
data1='{"head":{"sessionid":"undefined","seqid":null},"body":{"param1":{"basetype":0},"param2":{"basetype":true},"param3":{"basetype":2},"eventid":"camerazoom"}}'
def big():
    for i in range(1,100):
        bigg = requests.post("http://192.168.60.23/mtapi/camera/camerazoom",data=str(data1))
        time.sleep(0.01)
def small():
    for i in range(1,100):
        bigg = requests.post("http://192.168.60.23/mtapi/camera/camerazoom",data=str(data1))
        time.sleep(0.01)
for i in range(1,500):
    big()
    small()