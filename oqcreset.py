#-*- coding:utf-8 -*-
'''
oqcreset
'''
import requests
import time
ip = '192.168.60.23'
mtresetUrl = 'http://'+ip+'/mtapi/entity/mtreset'
data='{"head":{"sessionid":"undefined","seqid":null},"body":{"emFirst_priom_video_res":xx,"emFirst_priom_vga_res":6,"emSecond_priom_video_res":6,"emSecond_priom_vga_res":6,"emAss_video_res":0}}'
a=1
while a<20000000:
        r = requests.post(mtresetUrl,data=data)
        print r.content
        time.sleep(180)
        print time.asctime( time.localtime(time.time()) )
        print a 
        a=a+1


