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


matchdata = "Yuv Snd Vpss GetFrame"
ser = serial.Serial('COM9', 115200)

def sread():
    while 1:
        data = ser.readline()
        print(str(data).strip())
        if matchdata in str(data):
            print('FOUND!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('FOUND!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            for i in range(700,1000,10):
                winsound.Beep(i,50)
    time.sleep(0.01)
sread()
