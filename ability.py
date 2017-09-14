#-*- coding:utf-8 -*-
import requests
import json
import csv
import time


def callfunc():
    for i in [4096]:
        urlCall = 'http://192.168.60.23/mtapi/conf/makecall'
        dataCall = json.dumps({"head": {"sessionid": "undefined", "seqid": 0}, "body": {"param1": {"basetype": "192.168.32.38"}, "param2": {"basetype": i}, "param3": {"basetype": 1}}})
        requests.post(urlCall, data=dataCall)


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


def getInfoAndWRtoExcel():
    priVidprefer = requests.get('http://192.168.60.23/mtapi/cfg/prividprior?*').content
    priVideoSetting = json.loads(priVidprefer.replace(']', '').replace('[', ''))
    emVideoFormat = priVideoSetting.get('body').get('atVideoPriorParam').get('emVideoFormat')
    vidRes = priVideoSetting.get('body').get('atVideoPriorParam').get('emVideoRes')
    emVideoFormatStr = get_keys(videoFormat_dict, str(emVideoFormat))
    vidResStr = get_keys(videoRes_dict, str(vidRes))
    print '优选主视频格式: ', emVideoFormatStr, '主视频优选制式: ', vidResStr

    callStatis = requests.get('http://192.168.60.23/mtapi/callinfo/callstatisticsinforeq?*').content
    meetinginfo = json.loads(callStatis)
    mainVideoinfo = eval(str(meetinginfo.get('body').get('atMainVidEncStatic'))[1:-1])
    realMainFormat = get_keys(videoFormat_dict, str(mainVideoinfo.get('emVidEncType')))
    realMainPal = str(mainVideoinfo.get('dwVidWidth')) + "X" + str(mainVideoinfo.get('dwVidHeight'))
    realMainFrame1 = mainVideoinfo.get('dwFrameRate')
    time.sleep(2)
    realMainFrame2 = eval(str(json.loads(requests.get('http://192.168.60.23/mtapi/callinfo/callstatisticsinforeq?*').content).get('body').get('atMainVidEncStatic'))[1:-1]).get('dwFrameRate')
    time.sleep(2)
    realMainFrame3 = eval(str(json.loads(requests.get('http://192.168.60.23/mtapi/callinfo/callstatisticsinforeq?*').content).get('body').get('atMainVidEncStatic'))[1:-1]).get('dwFrameRate')
    print realMainFrame1, realMainFrame2, realMainFrame3
    realMainFrame = (int(realMainFrame1) +int(realMainFrame2) + int(realMainFrame3)) / 3
    print '实际发送主视频格式:', realMainFormat, '实际主视频发送分辨率:', realMainPal, '实际主视频发送帧率三次平均值: ', realMainFrame

    mainDecVideoinfo = eval(str(meetinginfo.get('body').get('atMainVidDecStatic'))[1:-1])
    realDecFormat = get_keys(videoFormat_dict, str(mainDecVideoinfo.get('emVidDecType')))
    realDecPal = str(mainDecVideoinfo.get('dwVidWidth')) + "X" + str(mainDecVideoinfo.get('dwVidHeight'))
    realDecFrame1 = mainDecVideoinfo.get('dwFrameRate')
    time.sleep(2)
    realDecFrame2 = eval(str(json.loads(requests.get('http://192.168.60.23/mtapi/callinfo/callstatisticsinforeq?*').content).get('body').get('atMainVidDecStatic'))[1:-1]).get('dwFrameRate')
    time.sleep(2)
    realDecFrame3 = eval(str(json.loads(requests.get('http://192.168.60.23/mtapi/callinfo/callstatisticsinforeq?*').content).get('body').get('atMainVidDecStatic'))[1:-1]).get('dwFrameRate')
    realDecFrame = (int(realDecFrame1) + int(realDecFrame2) +int(realDecFrame3)) / 3

    print '主视频接收格式:', realDecFormat, '主视频接受分辨率:', realDecPal, '主视频接受帧率三次平均值: ', realDecFrame

    with open('abilitywithx300.csv', 'a+') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel')
        spamwriter.writerow([emVideoFormatStr, vidResStr, realMainFormat,realMainPal, realMainFrame, realDecFormat, realDecPal, realDecFrame])


def get_keys(d, value):
    return [k for k, v in d.items() if v == value]


urlHangUp = 'http://192.168.60.23/mtapi/conf/hangupconf'
dataHangUp = json.dumps({"head": {"sessionid": "undefined", "seqid": 0}, "body": {"basetype": 1, "eventid": "hangupconf"}})


urlPrividprior = 'http://192.168.60.23/mtapi/cfg/prividprior'
#dataPrividPrior = {"head":{"sessionid":"undefined","seqid":0},"body":{"atVideoPriorParam":[{"emVideoFormat":i,"emVideoRes":a}]}}


for i in [6, 4, 5, 0, 2]:
    if i == 6:
        for n in [0, 21, 17, 16, 5, 13, 3]:
            dataPrividPrior = {"head": {"sessionid": "undefined", "seqid": 1}, "body": {"atVideoPriorParam": [{"emVideoFormat": i, "emVideoRes": n}]}}
            data = json.dumps(dataPrividPrior)
            changePal = requests.post(urlPrividprior, data=data)
            print data
            time.sleep(10)
            callfunc()
            time.sleep(10)
            getInfoAndWRtoExcel()
            time.sleep(2)
            hangUp = requests.post(urlHangUp, data=dataHangUp)
            time.sleep(8)

    if i == 4:
        for n in [0, 21, 17, 16, 5, 13, 3]:
            dataPrividPrior = {"head": {"sessionid": "undefined", "seqid": 1}, "body": {"atVideoPriorParam": [{"emVideoFormat": i, "emVideoRes": n}]}}
            data = json.dumps(dataPrividPrior)
            changePal = requests.post(urlPrividprior, data=data)
            print data
            #print changePal.content
            time.sleep(10)
            callfunc()
            time.sleep(10)
            getInfoAndWRtoExcel()
            time.sleep(3)
            hangUp = requests.post(urlHangUp, data=dataHangUp)
            time.sleep(8)

    elif i == 5:
        for n in [3, 5]:
            dataPrividPrior = {"head": {"sessionid": "undefined", "seqid": 1}, "body": {"atVideoPriorParam": [{"emVideoFormat": i, "emVideoRes": n}]}}
            data = json.dumps(dataPrividPrior)
            changePal = requests.post(urlPrividprior, data=data)
            print data
            time.sleep(12)
            callfunc()
            time.sleep(10)
            getInfoAndWRtoExcel()
            time.sleep(3)
            hangUp = requests.post(urlHangUp, data=dataHangUp)
            time.sleep(3)

    else:
        dataPrividPrior = {"head": {"sessionid": "undefined", "seqid": 1}, "body": {
            "atVideoPriorParam": [{"emVideoFormat": i, "emVideoRes": 3}]}}
        data = json.dumps(dataPrividPrior)
        changePal = requests.post(urlPrividprior, data=data)
        print data
        time.sleep(12)
        callfunc()
        time.sleep(10)
        getInfoAndWRtoExcel()
        time.sleep(3)
        hangUp = requests.post(urlHangUp, data=dataHangUp)
        time.sleep(3)

exit()