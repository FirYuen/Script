#-*- coding:utf-8 -*-
import requests
import json
import csv


outPut_dict = {
                'Auto':'0',
                'CIF(352*288)':'3',
                '4CIF(720*576)':'5',
                'VGA(640*480)':'10',
                'SVGA(800*600)':'11',
                'XGA(1024*768)':'12',
                '720P(1280*720)':'17',
                'SXGA(1280*1024)':'18',
                'UXGA(1600*1200)':'19',
                '1080p(1920*1080)':'21',
                'WXGA(1280*800)':'22',
                'WSXGA(1440*900)':'23',
                'WXGA(1280*768)':'43',
                'WXGA(1366*768)':'44',
                'WSXGA+(1680*1050)':'46',
                }
setFormat_dict = {
                    'H263':'2',
                    'H263+':'3',
                    'H264':'4',
                    'MPEG4':'5',
                    'H265':'6'
                }


def get_keys(d, value):
    return [k for k,v in d.items() if v == value]
    

assVid = requests.get('http://192.168.60.22/mtapi/deviceinfo/vidsrcstatus?*').content
assVidReplaced = assVid.replace('dwVideoHeight','uselessHeight',2).replace('dwVideoWidth','uselessWeight',2).replace('dwFrameRate','uselessFrame',2)
assVidinfo = json.loads(assVidReplaced)

for i in assVidinfo.get('body').get('atInfoList'):
    if isinstance(i.get('dwVideoHeight'), int) == 1:
        height = i.get('dwVideoHeight')
       
    if isinstance(i.get('dwVideoWidth'), int) == 1:
        width = i.get('dwVideoWidth')

    if isinstance(i.get('dwFrameRate'), int) == 1:
        frame = i.get('dwFrameRate')
assVidinfoStr = str(height)+'X'+str(width)
print 'PC机输出分辨率和帧率',assVidinfoStr,frame




pcassVidprefer = requests.get('http://192.168.60.22/mtapi/cfg/pcassvidprior?*').content
assVideoSetting = json.loads(pcassVidprefer)
emVideoFormat =  assVideoSetting.get('body').get('emVideoFormat')
vidRes =  assVideoSetting.get('body').get('emVideoRes')
emVideoFormatStr = get_keys(setFormat_dict,str(emVideoFormat))
vidResStr = get_keys(outPut_dict, str(vidRes))
print '优选辅视频格式: ',emVideoFormatStr,'辅视频优选制式: ' ,vidResStr




callStatis = requests.get('http://192.168.60.22/mtapi/callinfo/callstatisticsinforeq?*').content
meetinginfo = json.loads(callStatis)
for i in meetinginfo.get('body').get('atAssVidEncStatic'):
    realFormat = get_keys(setFormat_dict,str(i.get('emVidEncType')))
    realPal = str(i.get('dwVidWidth'))+"X"+str(i.get('dwVidHeight'))
    realFrame = i.get('dwFrameRate')
    print '实际发送辅视频流协议:',realFormat,'实际辅视频发送分辨率:',realPal,'实际发送帧率: ',realFrame

#print height,'X',width,frame,get_keys(setFormat_dict,str(emVideoFormat)),get_keys(outPut_dict, str(vidRes)),get_keys(setFormat_dict,str(i.get('emVidEncType'))),i.get('dwVidWidth'),"X",i.get('dwVidHeight')


with open('skyshareAbility.csv', 'a+') as csvfile:
    spamwriter = csv.writer(csvfile,dialect='excel')
    spamwriter.writerow([emVideoFormatStr,vidResStr,realFormat,realPal,realFrame,'1024X768'])

exit()