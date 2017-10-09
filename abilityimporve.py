#-*- coding:utf-8 -*-
import requests
import json
import csv
import time
import winsound

terminalIP = '192.168.60.23'
urlHangUp = 'http://'+terminalIP+'/mtapi/conf/hangupconf'
dataHangUp = json.dumps({"head": {"sessionid": "undefined", "seqid": 0}, "body": {"basetype": 1, "eventid": "hangupconf"}})

urlCall = 'http://'+terminalIP+'/mtapi/conf/makecall'
urlPrividprior = 'http://'+terminalIP+'/mtapi/cfg/prividprior'

sky300FormatAndPal = {'H265':[0, 21, 17, 16, 5, 13, 3],'H264':[0, 21, 17, 16, 5, 13, 3],'MPEG4':[3,5],'H263':[3],'H261':[3]}

excelName = 'test.csv'
def excelTitle():
    with open(excelName, 'a+') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel')
        spamwriter.writerow(['Time','emVideoFormat','emVidRes','callRate','mainVidEncFormat','mainVidEncFrame','mainVidEncBitrate','mainVidEncFrame','mainVidDecFormat','mainVidDecFrame','mainVidDecBitrate','mainVidDecFrame',])


def callfunc():
    for n in [64,128,192,256,384,512,768,1024,1088,1472,2048,4096]:
        dataCall = json.dumps({"head": {"sessionid": "undefined", "seqid": 0}, "body": {"param1": {"basetype": "192.168.60.27"}, "param2": {"basetype": n}, "param3": {"basetype": 1}}})
        requests.post(urlCall, data=dataCall)
        time.sleep(10)
        getInfoAndWRtoExcel(n)
        time.sleep(5)
        hangUp = requests.post(urlHangUp, data=dataHangUp)
        time.sleep(10)

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

videoFormat_dict = {
    'H261': '0',
    'H262': '1',
    'H263': '2',
    'H263+': '3',
    'MPEG4': '5',
    'H264': '4',
    'H265': '6',
}

def get_keys(d, value):
    return [k for k, v in d.items() if v == value]
def beep():
	for i in [1,2,3]:
		winsound.Beep(3500,500)
		time.sleep(0.1)
		


nowTime = time.strftime('%m%d-%H:%M:S',time.localtime(time.time()))

def getInfoAndWRtoExcel(n):
    priVidprefer = requests.get('http://'+terminalIP+'/mtapi/cfg/prividprior?*').content
    priVideoSetting = json.loads(priVidprefer.replace(']', '').replace('[', ''))
    emVideoFormat = priVideoSetting.get('body').get('atVideoPriorParam').get('emVideoFormat')
    vidRes = priVideoSetting.get('body').get('atVideoPriorParam').get('emVideoRes')
    emVideoFormatStr = get_keys(videoFormat_dict, str(emVideoFormat))
    vidResStr = get_keys(videoRes_dict, str(vidRes))
    print '优选主视频格式: ', emVideoFormatStr, '主视频优选制式: ', vidResStr

    meetingState1 = json.loads(requests.get('http://'+terminalIP+'/mtapi/callinfo/callstatisticsinforeq?*').content)
    mainVidEncInfo1 =  eval(str(meetingState1.get('body').get('atMainVidEncStatic'))[1:-1])
    mainVidEncFormat = get_keys(videoFormat_dict, str(mainVidEncInfo1.get('emVidEncType')))
    mainVidEncPal = str(mainVidEncInfo1.get('dwVidWidth')) + "X" + str(mainVidEncInfo1.get('dwVidHeight'))
    mainVidEncBitrate1 = mainVidEncInfo1.get('dwEncBitrate')
    mainVidEncFrame1 = mainVidEncInfo1.get('dwFrameRate')
    mainVidDecInfo1 = eval(str(meetingState1.get('body').get('atMainVidDecStatic'))[1:-1])
    mainVidDecFormat = get_keys(videoFormat_dict, str(mainVidDecInfo1.get('emVidDecType')))
    mainVidDecPal = str(mainVidDecInfo1.get('dwVidWidth')) + "X" + str(mainVidDecInfo1.get('dwVidHeight'))
    mainVidDecBitrate1 = mainVidDecInfo1.get('dwDecBitrate')
    mainVidDecFrame1 = mainVidDecInfo1.get('dwFrameRate')
    print mainVidDecBitrate1,mainVidDecFrame1
    
    time.sleep(3)
    meetingState2 = json.loads(requests.get('http://'+terminalIP+'/mtapi/callinfo/callstatisticsinforeq?*').content)
    mainVidEncInfo2 =  eval(str(meetingState2.get('body').get('atMainVidEncStatic'))[1:-1])
    mainVidEncBitrate2 = mainVidEncInfo2.get('dwEncBitrate')
    mainVidEncFrame2 = mainVidEncInfo2.get('dwFrameRate')
    mainVidDecInfo2 = eval(str(meetingState2.get('body').get('atMainVidDecStatic'))[1:-1])
    mainVidDecBitrate2 = mainVidDecInfo2.get('dwDecBitrate')
    mainVidDecFrame2 = mainVidDecInfo2.get('dwFrameRate')
    print mainVidDecBitrate2,mainVidDecFrame2

    time.sleep(3)
    meetingState3 = json.loads(requests.get('http://'+terminalIP+'/mtapi/callinfo/callstatisticsinforeq?*').content)
    mainVidEncInfo3 =  eval(str(meetingState3.get('body').get('atMainVidEncStatic'))[1:-1])    
    mainVidEncBitrate3 = mainVidEncInfo3.get('dwEncBitrate')
    mainVidEncFrame3 = mainVidEncInfo3.get('dwFrameRate')
    mainVidDecInfo3 = eval(str(meetingState3.get('body').get('atMainVidDecStatic'))[1:-1])
    mainVidDecBitrate3 = mainVidDecInfo3.get('dwDecBitrate')
    mainVidDecFrame3 = mainVidDecInfo3.get('dwFrameRate')
    print mainVidDecBitrate3,mainVidDecFrame3

    mainVidEncBitrate = (int(mainVidEncBitrate1)+int(mainVidEncBitrate2)+int(mainVidEncBitrate3))/3
    mainVidDecBitrate = (int(mainVidDecBitrate1)+int(mainVidDecBitrate2)+int(mainVidDecBitrate3))/3

    mainVidEncFrame = (int(mainVidEncFrame1)+int(mainVidEncFrame2)+int(mainVidEncFrame3))/3
    mainVidDecFrame = (int(mainVidDecFrame1)+int(mainVidDecFrame2)+int(mainVidDecFrame3))/3


    print '实际发送主视频格式:', mainVidEncFormat, '实际主视频发送分辨率:', mainVidEncPal
    print '实际接收主视频格式:', mainVidDecFormat, '实际主视频接收分辨率:', mainVidDecPal
    print '实际主视频发送码率三次平均值',mainVidEncBitrate,'实际主视频发送帧率三次平均值: ', mainVidEncFrame
    print '实际主视频接收码率三次平均值',mainVidDecBitrate,'实际主视频接收帧率三次平均值: ', mainVidDecFrame

    with open(excelName, 'a+') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel')
        spamwriter.writerow([nowTime,emVideoFormatStr,vidResStr,n,mainVidEncFormat,mainVidEncFrame,mainVidEncBitrate,mainVidEncFrame,mainVidDecFormat,mainVidDecFrame,mainVidDecBitrate,mainVidDecFrame,])



excelTitle()

print sky300FormatAndPal.keys()
for i in sky300FormatAndPal.keys():
    if i == 'H265':
        for n in sky300FormatAndPal.get('H265'):
            dataPrividPrior = {"head": {"sessionid": "undefined", "seqid": 1}, "body": {"atVideoPriorParam": [{"emVideoFormat": 6, "emVideoRes": n}]}}
            data = json.dumps(dataPrividPrior)
            changePal = requests.post(urlPrividprior, data=data)
            print data
            time.sleep(10)
            callfunc()
            

    if i == 'H264':
        for n in sky300FormatAndPal.get('H264'):
            dataPrividPrior = {"head": {"sessionid": "undefined", "seqid": 1}, "body": {"atVideoPriorParam": [{"emVideoFormat": 4, "emVideoRes": n}]}}
            data = json.dumps(dataPrividPrior)
            changePal = requests.post(urlPrividprior, data=data)
            print data
            #print changePal.content
            time.sleep(10)
            callfunc()
            

    elif i == 'MPEG4':
        for n in sky300FormatAndPal.get('MPEG4'):
            dataPrividPrior = {"head": {"sessionid": "undefined", "seqid": 1}, "body": {"atVideoPriorParam": [{"emVideoFormat": 5, "emVideoRes": n}]}}
            data = json.dumps(dataPrividPrior)
            changePal = requests.post(urlPrividprior, data=data)
            print data
            time.sleep(10)
            callfunc()
            

    elif i == 'H263':
        for n in sky300FormatAndPal.get('H263'):
            dataPrividPrior = {"head": {"sessionid": "undefined", "seqid": 1}, "body": {"atVideoPriorParam": [{"emVideoFormat":2 , "emVideoRes": 3}]}}
            data = json.dumps(dataPrividPrior)
            changePal = requests.post(urlPrividprior, data=data)
            print data
            time.sleep(10)
            callfunc()

    elif i == 'H261':
        for n in sky300FormatAndPal.get('H261'):
            dataPrividPrior = {"head": {"sessionid": "undefined", "seqid": 1}, "body": {"atVideoPriorParam": [{"emVideoFormat":0 , "emVideoRes": 3}]}}
            data = json.dumps(dataPrividPrior)
            changePal = requests.post(urlPrividprior, data=data)
            print data
            time.sleep(10)
            callfunc()




beep()


exit()