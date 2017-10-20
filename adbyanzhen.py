# -*- coding: utf-8 -*-
import os
import time

def adbconnect():
    os.popen("adb shell input tap 1230 1158")
    time.sleep(0.1)
for i in range(1,500000):
    adbconnect()
    print i