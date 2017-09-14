import requests
import json
import time

startConf = 'http://192.168.60.22/mtapi/conf/createconf'
startConf_data = json.dumps({"head":{"sessionid":"undefined","seqid":1},"body":{"achName":"6543210000177","dwDuration":240,"emMeetingSafe":1,"achPassword":"","emEncryptedType":0,"emMeetingType":1,"emClosedMeeting":0,"dwBitrate":2048,"dwMemberCount":1,"atVideoFormatList":[{"emResolution":21,"dwRate":2048}],"atMembers":[{"achAccount":"0512111880422","emAccountType":1}],"emMixMode":1,"dwMixMemberCount":0,"atMixMemberList":[],"tVmp":{"bEnable":1,"emStyle":1,"bVoiceHint":1,"bShowMTName":1,"bIsBroadcast":1}}})
applyForChairman = 'http://192.168.60.22/mtapi/conf/applychairman'
applyForChairman_data = json.dumps({"head":{"sessionid":"undefined","seqid":1},"body":{"eventid":"applychairman"}})
endConf = 'http://192.168.60.22/mtapi/conf/endconf'
endConf_data = json.dumps({"head":{"sessionid":"undefined","seqid":1},"body":{"eventid":"endconf"}})

i = 1 
while i <10000:
	requests.post(startConf, data=startConf_data)
	time.sleep(7)
	requests.post(applyForChairman, data=applyForChairman_data)
	time.sleep(3)
	requests.post(applyForChairman, data=applyForChairman_data)
	time.sleep(3)
	requests.post(applyForChairman, data=applyForChairman_data)
	
	
	requests.post(endConf, data=endConf_data)
	time.sleep(10)
	requests.post(endConf, data=endConf_data)
	time.sleep(10)
	i=i+1