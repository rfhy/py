#encoding:utf-8

import os,sys,time,lirun

SN = '151000010000003B'
answer='play Text,'
ask = 'UnderstandDispatcher result text'
wake = 'RokidWakeupTranslator'
xf = 'XunFeiTranslator'
Nuance = 'NuanceOfflineTranslator'

def audio():
    for log in sys.stdin:
        if answer in log:
            a = log.split()
            a1 = ''
            if len(a) == 9:
                a1 = '无回答'
            if len(a) > 9:
                for i in range(9,len(a)):
                    a1 = a1 + a[i] + " "
            a1 = a[0] +" " + a[1] + " 答: " + a1
            lirun.logg(a1.decode('utf-8').encode('gbk'))

        if ask in log:
            b = log.split()
            b1 = b[0] +" " + b[1] + " 问: "
            c = ''
            if wake in log:
                c = 'Rokid唤醒'
            if xf in log:
                c = '讯飞在线识别'
            if Nuance in log:
                c = 'Nuance离线识别'
            b3 = b1 + b[8].split(",")[0] + " === " + c
            lirun.logg(b3.decode('utf-8').encode('gbk'))          

if __name__ == '__main__':
    audio()
