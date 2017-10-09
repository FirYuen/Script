#-*- coding:utf-8 -*-
import requests
import time


rebootURL1 = 'http://192.168.32.36/mtapi/entity/mtreboot'
rebootURL2 = 'http://192.168.32.38/mtapi/entity/mtreboot'
a=1
while a<20000000:
       
    rebootRequests = requests.post(rebootURL1,data ='{}')
    rebootRequests = requests.post(rebootURL2,data ='{}')
    

    time.sleep(180)
    print time.asctime( time.localtime(time.time()) )
    print a 
    a=a+1