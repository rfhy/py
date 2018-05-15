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
import autoresult
reload(sys)
sys.setdefaultencoding('utf-8')
Uri = MyUtil.Getfile("host")
sn = MyUtil.Getsn()
def killlogcat():  
    pidlogcat="adb -s "+ sn +" shell \" ps | grep ' logcat' | busybox awk '{print $2}' \""
    test=os.popen(pidlogcat)
    time.sleep(3)
    text=test.read()
    test.close()
##    print text
    testlist = text.replace("\n"," ").replace("\r"," ").split(" ")
    for l in testlist:
        if l=='' or l==' ':
            continue
        else:
            cmd="adb -s "+ sn + " shell \" kill " +l +"\""
            os.system(cmd)
            print "kill pid:"+l
            time.sleep(2)
def sendlongcnn(casejson,resultjson,decname,sleeptime):
##   1.初始化（创建日志文件夹，杀死测试logcat，创建casealllog）
##   2.创建日志文件
##   3.发送长连接(如果服务返回正确就继续判执行结果，如果失败就不判断结果)

##    1.
##    global remindlist
    remindlist=[]
##    resultjson = resultjson.replace("\\\"","\"")
    casejson = casejson.replace("%sn%","\""+sn+"\"")
    resultjsondic = eval(resultjson)
    casejsondic = eval(casejson)
    print casejsondic
    print resultjsondic
    tag = resultjsondic["tag"]
    result=-1
    if "deldb" in resultjsondic['type']:
        amcommand = "adb -s " + sn + " pull /data/data/com.juan.voiceservice/databases/user_alarm2.db"+" ./test.db"
        os.system(amcommand)
        time.sleep(3)
        cx = sqlite3.connect("./test.db")
        cu = cx.cursor() 
        match="select alarmId from user_alarm where TTSText like '%测试%'"
        cu.execute(match)
        remindlist = cu.fetchall()
        print remindlist
        if len(remindlist)>0:
            casejsondic["data"]["id"]=remindlist[0][0]
            print casejsondic
            resultjson = resultjson.replace("select * from user_alarm where alarmId=0","select * from user_alarm where alarmId="+str(remindlist[0][0]))
            print resultjson
        else:
            print"Non-existent remind"
            return 0
        cu.close()
        cx.close()
       
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
    
##  2.
    logtime = time.strftime('%Y%m%d%H%M%S')
    logname = "longcnn_"+decname+"_"+logtime+'.log'
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

##  3.
    test_data = {"action":"mc/tomcserver","data":{"mcserver":"10.51.52.40:7073","cmddata":casejsondic}}           
    jdata = json.dumps(test_data)
    requrl = Uri+"/test/mctest"
    req = urllib2.Request(requrl,jdata)
    try:
        res_data = urllib2.urlopen(req)
        print "senddatatime: " + time.strftime('%m-%d %H:%M:%S')
        res = res_data.read()
        print "sendresult: "+ res
        s = json.loads(res)
        returncode = s["result"]
       
        if 0 == returncode:
                result=0
        else:
                result=returncode
                
        time.sleep(sleeptime)
        killlogcat()
        if "result" in resultjsondic["type"]:
            tomatch = resultjsondic["tomatch"]
            if str(result)==tomatch:
                result=0
                
        else:   
            if  result==0 :
                amcommand = "adb -s " + sn + " shell \" cat /sdcard/autotestlog/"+logname+" | grep "+tag+" \" "
                output = os.popen(amcommand)
                time.sleep(3)
                res = output.read()
                print "caseresultlog:"+res
                output.close()    
                result =  autoresult.autoresult(resultjson,res)
        
        print "caseresult: " +str(result)  
        return result
        res_data.close()
            
            
    except urllib2.HTTPError,e:
        print 'error resultcode:',e.code;
        print 'error msg:',(e.read().decode('utf-8'));
        return -1

    
##strdata,strresult = MyUtil.Getlongcnncase('AddEngAlarm')
##re = sendlongcnn(strdata,strresult,"AddEngAlarm",10)
##print "result:"+str(re)
##for i in range(3):
##
##    time.sleep(5)
##    strdata,strresult = MyUtil.Getlongcnncase('song')
##    result = sendlongcnn(strdata,strresult,"song",15)
##    if(result == 0):
##        print "send  song successful"
##        strdata,strresult = MyUtil.Getlongcnncase('stopsong')
##        result = sendlongcnn(strdata,strresult,"stopsong",10)
##        if(result == 0):
##            print "send  stopsong successful"
##        else:
##            print "send  stopsong failure"
##            
##    else:
##        print "send  song failure"
