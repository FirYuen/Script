#-*- coding:utf-8 -*-
import requests
import time
li = [6,1,2,16,3,4,17,32,24,31,9,11,22,29,27]
data='{"head":{"sessionid":"undefined","seqid":null},"body":{"emFirst_priom_video_res":xx,"emFirst_priom_vga_res":6,"emSecond_priom_video_res":6,"emSecond_priom_vga_res":6,"emAss_video_res":0}}'
a=1
while a<2:
    for i in li:
        r = requests.post('http://192.168.60.24/mtapi/cfg/hdresoutput',data=data.replace('xx',str(i)))
        print r.content
        time.sleep(15)
        print time.asctime( time.localtime(time.time()) )
    print a 
    a=a+1