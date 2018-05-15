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
reload(sys)
sys.setdefaultencoding('utf-8')
sn = MyUtil.Getsn()
pcmpath = MyUtil.Getfile("pcm")
def killlogcat():  
    pidlogcat="adb -s "+ sn +" shell \" ps | grep ' logcat' | busybox awk '{print $2}' \""
    test=os.popen(pidlogcat)
    time.sleep(3)
    test=test.read()
    print test
    testlist = test.replace("\n"," ").replace("\r"," ").split(" ")
    for l in testlist:
        if l=='' or l==' ':
            continue
        else:
            cmd="adb -s "+ sn + " shell \" kill " +l +"\""
            os.system(cmd)
            print "kill pid:"+l
            time.sleep(2)
def newyuyin(casename,decname,sleeptime):
    pcmfile = pcmpath+casename
    returnvalue = True
    pidlogcat = "adb -s "+ sn +" shell \" cd /sdcard/autotestlog\""
    test=os.popen(pidlogcat)
    time.sleep(1)
    test=test.read()
    if  "No such file" in test:
        amcommand = "adb -s " + sn + " shell \"mkdir /sdcard/autotestlog\""
        os.system(amcommand)
    logtime = time.strftime('%Y%m%d%H%M%S')
    logname = casename+logtime+'.log'
    killlogcat()
    amcommand = "adb -s " + sn + " shell \" rm -rf /sdcard/ve/recorder/normal/* \" "
    os.system(amcommand)
    time.sleep(3)
    amcommand = "adb -s " + sn + " push  " + pcmfile + " /sdcard/ve/recorder/normal "
    os.system(amcommand)
    pidstart = 0
    while(pidstart<1):
        
        pidlogcat="adb -s "+ sn +" shell \" busybox nohup logcat -v time  -f /sdcard/autotestlog/"+logname+" & \""
        os.system(pidlogcat)
        pidlogcat = "adb -s "+ sn +" shell \" ls /sdcard/autotestlog/"+logname+" \""
        test=os.popen(pidlogcat)
        time.sleep(3)
        test=test.read()
        if  "No such file" in test:
                print "logcat failed"
                
        else:
                pidstart = 1
                print 'logcat successful'
                
        time.sleep(3)
    print "logname is " +logname
    amcommand = "adb -s " + sn + " shell  am broadcast -a test.action --es key \"test_iat\" --es value \"\""
    os.system(amcommand)
    printtime = time.strftime('%Y%m%d%H%M%S')
    print "send test_iat=false : "+printtime
    time.sleep(3)
    amcommand = "adb -s " + sn + " shell am broadcast -a test.action --es key \"test_iat\" --es value \"true\""
    os.system(amcommand)
    printtime = time.strftime('%Y%m%d%H%M%S')
    print "send test_iat=true : "+printtime
    time.sleep(40)
    amcommand = "adb -s "+ sn +" shell \"cat /sdcard/autotestlog/"+logname+" | grep -E '唤醒|你好'\""
    output = os.popen(amcommand)
    res= output.read()
    print "wakeup logcat:",res
    amcommand = "adb -s " + sn + " shell \" cat /sdcard/autotestlog/"+logname+" | grep NetSender\""
    output = os.popen(amcommand)
    time.sleep(3)
    res = output.read()
    print casename+" logcat",res
    if decname in res:
        print casename+' successful';
    else:
        print casename+' failed'
        returnvalue = False

    killlogcat()
    time.sleep(sleeptime)
    return returnvalue
newyuyin("yuyinxiangzuozhuan","向左转",0)
	







        
    
        
