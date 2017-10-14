#-*- coding:utf-8 -*-
'''
切换输出制式
'''
import requests
import time
def get_keys(d, value):
    return [k for k, v in d.items() if v == value]
videoRes_dict = {
    'Auto': '0',
    'SQCIF 88x72': '1',
    'QCIF 176x144': '2',
    'CIF(352*288)': '3',
    '2CIF(352x576)': '4',
    '4CIF(720*576)': '5',
    '16CIF(1408x1152)': '6',
    'SIF(352x240)': '7',
    '2SIF': '8',
    '4SIF(704x480)': '9',
    'VGA(640*480)': '10',
    'SVGA(800*600)': '11',
    'XGA(1024*768)': '12',
    'WCIF(512*288)': '13',
    'SQCIF(112*96)': '14',
    'SQCIF(96*80)': '15',
    'W4CIF(1024*576)': '16',
    '720P(1280*720)': '17',
    'SXGA(1280*1024)': '18',
    'UXGA(1600*1200)': '19',
    '1080i(1920x1080)': '20',
    '1080p(1920*1080)': '21',
    'WXGA(1280*800)': '22',
    'WSXGA(1440*900)': '23',
    'WXGA(1280*768)': '43',
    'WXGA(1366*768)': '44',
    'WSXGA1280x854': '45',
    'WSXGA+(1680*1050)': '46',
    'WUXGA(1920x1200)': '47',
    '4Kx2K(3840x2160)': '48',
}
ip = '192.168.60.22'
li = [6,1,2,16,3,4,17,32,24,31,9,11,22,29,27]
changePALData='{"head":{"sessionid":"undefined","seqid":null},"body":{"emFirst_priom_video_res":xx,"emFirst_priom_vga_res":6,"emSecond_priom_video_res":6,"emSecond_priom_vga_res":6,"emAss_video_res":0}}'
rebootURL = 'http://'+ip+'/mtapi/entity/mtreboot'
a=1
while a<20000000:
    for i in li:
        changePALRequests = requests.post('http://192.168.60.22/mtapi/cfg/hdresoutput',data=changePALData.replace('xx',str(i)))
        print changePALRequests.content
        time.sleep(20)
        #rebootRequests = requests.post(rebootURL,data ='{}')

        #time.sleep(240)
        print time.asctime( time.localtime(time.time()) )
    print a 
    a=a+1