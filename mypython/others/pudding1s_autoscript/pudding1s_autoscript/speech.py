# -*- coding: utf-8 -*-
import urllib2
import urllib
import cookielib
import json
import os
import sys
import string
import time
import md5
import hashlib
import MyUtil
import sqlite3
import datetime
import autoresult
reload(sys)
sys.setdefaultencoding('utf-8')
sn = MyUtil.Getsn()
pcmpath = MyUtil.Getfile("pcm")
sleepjson,sleepresult = MyUtil.Getspeechcase(u"再见")
alllogcatlist=[]
def killlogcat():  
    pidlogcat="adb -s "+ sn +" shell \" ps | grep ' logcat' | busybox awk '{print $2}' \""
    test=os.popen(pidlogcat)
    time.sleep(3)
    text=test.read()
##    print text
    test.close()
    testlist = text.replace("\n"," ").replace("\r"," ").split(" ")
    for l in testlist:
        if l=='' or l==' ':
            continue
        else:
            cmd="adb -s "+ sn + " shell \" kill " +l +"\""
            os.system(cmd)
            print "kill pid:"+l
            time.sleep(2)
    
def killspecificlogcat():
    killlogcatlist=[]
    killlogcatlist = getlogcat()
    print "current logcat"+str(killlogcatlist)
    print "alllogcatlist"+str(alllogcatlist)
    for l in killlogcatlist :
        if l not in alllogcatlist:
            cmd="adb -s "+ sn + " shell \" kill " +l +"\""
            os.system(cmd)
            print "kill pid:"+l
            time.sleep(2)
                       
def getlogcat():
    templogcatlist=[]
    pidlogcat="adb -s "+ sn +" shell \" ps | grep 'logcat' | busybox awk '{print $2}' \""
    test=os.popen(pidlogcat)
    time.sleep(3)
    text=test.read()
##    print test
    test.close()
    testlist = text.replace("\n"," ").replace("\r"," ").split(" ")
    for l in testlist:
        if l=='' or l==' ':
            continue
        else:
             templogcatlist.append(l)
    return  templogcatlist

def sendspeech(casejson,resultjson,decname,sleeptime):
    
##    0.初始化（创建日志文件夹，杀死测试logcat，创建casealllog,清除sdcard/ve/recorder/normal文件夹）
##    1.确保唤醒（循环调用唤醒接口，监控唤醒日志中的唤醒结果，发现唤醒杀死唤醒进程）
##    2.传入casejson （创建caseanaly日志，调用接口，再调用再见的接口循环休眠，确保休眠）
##    3.调用autoresult.autoresult 进行结果判断（杀死测试logcat，传出数据库文件,将caseanaly日志中的结果信息或者数据库文件，及结果判断类型作为参数传送到autoresult.autoresult中）
    
##    0.
    global alllogcatlist
##    global autoresult.old_volume
    alllogcatlist = []
    resultjsondic = eval(resultjson)
    casejsondic = eval(casejson.replace("\\\"","\""))
    print casejsondic
    print resultjsondic
    tag = resultjsondic["tag"]
    if "volume" in resultjsondic['type']:
        amcommand = "adb -s " + sn + " shell \"service call audio 15 i32 3\""
        test=os.popen(amcommand)
        time.sleep(1)
        text=test.read()
        autoresult.old_volume = text.split("   ")[0].split(' ')[-1][-1]
        test.close()
    if decname=="reminder":
        casejsondic["semantic"]["slots"]['datetime']['date']=time.strftime('%Y-%m-%d')
        casejsondic["semantic"]["slots"]['datetime']['time']=(datetime.datetime.now()+datetime.timedelta(seconds=3600)).strftime('%H-%M-%S')
        casejson = str(casejsondic).replace("'","\"").replace("\\\\","\\").replace("\"","\\\"")
        print casejson
    pidlogcat = "adb -s "+ sn +" shell \" cd /sdcard/autotestlog\""
    test=os.popen(pidlogcat)
    time.sleep(1)
    text=test.read()
    test.close()
    if  "No such file" in text:
        amcommand = "adb -s " + sn + " shell \"mkdir /sdcard/autotestlog\""
        os.system(amcommand)
        time.sleep(2)
    
    killlogcat()
    amcommand = "adb -s " + sn + " shell \" rm -rf  /sdcard/ve/recorder/normal/* \""
    os.system(amcommand)
    amcommand = "adb -s " + sn + " shell \" rm   /sdcard/casewakeup.log \""
    os.system(amcommand)
    time.sleep(3)
    amcommand = "adb -s " + sn + " shell \" rm  /sdcard/casesleep.log\""
    os.system(amcommand)
    time.sleep(3)
    amcommand = "adb -s " + sn + " push  ./anihao.pcm  /sdcard/ve/recorder/normal/"
    os.system(amcommand)
    time.sleep(5)
    logtime = time.strftime('%Y%m%d%H%M%S')
    logname = "speech_"+decname+"_"+logtime+'.log'
    while(True):

        os.system("adb -s "+ sn + " logcat -c ")
        time.sleep(1)
        pidlogcat="adb -s "+ sn +" shell \" busybox nohup logcat -v time  -f /sdcard/autotestlog/"+logname+" & \""
        os.system(pidlogcat)
        pidlogcat = "adb -s "+ sn +" shell \" ls /sdcard/autotestlog/"+logname+" \""
        test=os.popen(pidlogcat)
        time.sleep(3)
        text=test.read()
        if  "No such file" in text:
                print "casealllog failed"
                
        else:
                print 'casealllog successful'
                break
        test.close()        
        time.sleep(3)
    alllogcatlist = getlogcat()  #获得case执行中的不需要杀死的log
    print "current logcat is "+str(alllogcatlist)
##    1.
    wakeupfailednum=0
    while(True):
        while(True):
            os.system("adb -s "+ sn + " logcat -c ")
            time.sleep(1)
            pidlogcat="adb -s "+ sn +" shell \" busybox nohup logcat -v time  -f /sdcard/casewakeup.log -s VoiceService & \""
            os.system(pidlogcat)
            pidlogcat = "adb -s "+ sn +" shell \" ls /sdcard/casewakeup.log \""
            test=os.popen(pidlogcat)
            time.sleep(3)
            text=test.read()
            if  "No such file" in text:
                    print "wakeuplog failed"
                    
            else:
                    print 'wakeuplog successful'
                    break
            test.close()        
            time.sleep(3)
            
        amcommand = "adb -s " + sn + " shell \" am broadcast -a test.action --es key \"test_iat\" --es value \"false\" \""
        os.system(amcommand)
        time.sleep(3)
        amcommand = "adb -s " + sn + " shell \" am broadcast -a test.action --es key \"test_iat\" --es value \"true\" \""
        os.system(amcommand)
##        printtime = time.strftime('%Y-%m-%d %H:%M:%S')
##        print "send test_iat=true : "+printtime
        time.sleep(5)
        amcommand = "adb -s "+ sn +" shell \"cat /sdcard/casewakeup.log | grep 'Change state'\""
        output = os.popen(amcommand)
        res= output.read()
        output.close()
        print "wakeup logcat:",res
        if "Change state from StateSleeping1 to StateUnderstanding2 " in res:
            print "wakeuptime: " + time.strftime('%m-%d %H:%M:%S')
            print "wakeup succeed !"
            break
        else:
            print "wakeup failed !"
            wakeupfailednum += 1
        

##    print "wakeup failed number is "+str(wakeupfailednum)
    killspecificlogcat()
##    2.
    print "senddatatime: " + time.strftime('%m-%d %H:%M:%S')
    amcommand = "adb -s " + sn + " shell \" am startservice -a com.juan.audioservice.TEST_SPEAK_RESULT --es resultJson '"+casejson+"' \""
    os.system(amcommand)
    time.sleep(sleeptime)
    if decname=="song":
        amcommand = "adb -s " + sn + " shell \" am broadcast -a test.action --es key \"test_iat\" --es value \"true\" \""
        os.system(amcommand)
        time.sleep(5)
##    amcommand = "adb -s " + sn + " shell \" am startservice -a com.juan.audioservice.TEST_SPEAK_RESULT --es resultJson '"+sleepjson+"' \""
##    os.system(amcommand)
##    time.sleep(4)   
##    sleepfailednum=0
##    while(True):
##        while(True):
####            os.system("adb -s "+ sn + " logcat -c ")
##            time.sleep(1)
##            pidlogcat="adb -s "+ sn +" shell \" busybox nohup logcat -v time  -f /sdcard/casesleep.log -s VoiceService & \""
##            os.system(pidlogcat)
##            pidlogcat = "adb -s "+ sn +" shell \" ls /sdcard/casesleep.log \""
##            test=os.popen(pidlogcat)
##            time.sleep(3)
##            test=test.read()
##            if  "No such file" in test:
##                    print "sleeplog failed"
##                    
##            else:
##                    print 'sleeplog successful'
##                    break
##                    
##            time.sleep(3)
##        amcommand = "adb -s " + sn + " shell \" am startservice -a com.juan.audioservice.TEST_SPEAK_RESULT --es resultJson '"+sleepjson+"' \""
##        os.system(amcommand)
##        time.sleep(4)   
##        amcommand = "adb -s "+ sn +" shell \"cat /sdcard/casesleep.log/ | grep 'Change state'\""
##        output = os.popen(amcommand)
##        res= output.read()
##        print "sleep logcat:",res
##        if "Change state from StateUnderstanding2 to StateSleeping1" in res:
##            print "sleep succeed !"
##            break
##        else:
##            print "sleep failed !"
##            sleepfailednum += 1
        

##    print "sleep failed number is "+str(sleepfailednum)
##    3.
    killlogcat()
    amcommand = "adb -s " + sn + " shell \" cat /sdcard/autotestlog/"+logname+" | grep "+tag+" \" "
    output = os.popen(amcommand)
    time.sleep(3)
    res = output.read()
    print "caseresultlog:"+res
    output.close()
    return autoresult.autoresult(resultjson,res)
    



    


##def test():
##    for i in range(1):
##        strdata,strresult = MyUtil.Getspeechcase(u'摩羯座星座运势')
##        re = sendspeech(strdata,strresult,"sign",120)
##        print "jieguo: "+str(re)
####    
####
##test()
##    








        
    
        
