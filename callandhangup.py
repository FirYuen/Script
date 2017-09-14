import requests
import json
import time

urls = 'http://192.168.60.23/mtapi/conf/hangupconf'
ss = json.dumps({"head":{"sessionid":"undefined","seqid":0},"body":{"basetype":1,"eventid":"hangupconf"}})
url = 'http://192.168.60.23/mtapi/conf/makecall'
s = json.dumps({"head":{"sessionid":"undefined","seqid":0},"body":{"param1":{"basetype":"192.168.33.176"},"param2":{"basetype":4096},"param3":{"basetype":1}}})

i = 1 
while i <10000:
	r = requests.post(url, data=s)
	time.sleep(8)
	r = requests.post(urls, data=ss)
	time.sleep(5)
	i=i+1