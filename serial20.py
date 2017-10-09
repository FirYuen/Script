# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import serial
import time
import os
import winsound
def say(word):
    word = bytearray(word,'utf8')+bytearray('\n','utf8')
    return word


matchdata = "Boot Animation exit"
ser = serial.Serial('COM20', 115200)
writesussesalarm = " Ev_MT_ThreadDetectUpdateNtf"
warning = "DDR training timeout"


def sread():
    while 1:
        data = ser.readline()
        print(str(data).strip())
        if matchdata in str(data):
            print('found Boot Animation exit !!!!!!!!!!!!!!!!!!!!! ')
            time.sleep(3)
            print('###############################################################')
            #ser.write(say('su'))
            #ser.write(say('hibooter b 3519 /vcmt/media/hi3519/u-boot.bin'))
        elif writesussesalarm in str(data):
            print('BEEP!')
            winsound.Beep(750,1000)
            time.sleep(0.5)
            print('NOTHING FOUND !')
            print('YOU SHOULD CUT THE POWER AND TRY AGAIN')
            print('\n\n\n\n\n\n\n\n\n')
            #os.popen("adb shell input tap 320 620")
            
        elif warning in str(data):
            print('FOUND!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('FOUND!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            for i in range(700,1000,10):
                winsound.Beep(i,50)
    time.sleep(0.01)
sread()

