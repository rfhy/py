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
reload(sys)
sys.setdefaultencoding('utf-8')
##Uri = MyUtil.Getfile("host")
sn = MyUtil.Getsn()
global old_volume
old_volume="0"
def autoresult(resultjson,res):
    result = -1
    resultjsondic = eval(resultjson)
    resulttype = resultjsondic['type']
    if "database" in resulttype:
        tempnum=0
        dbpath = resultjsondic["dbpath"]
        tomatch = resultjsondic["tomatch"]
        tomatchlist=tomatch.split(';')
        amcommand = "adb -s " + sn + " pull "+dbpath+" ./test.db"
        os.system(amcommand)
        time.sleep(3)
        cx = sqlite3.connect("./test.db")
        cu = cx.cursor() 
        for match in tomatchlist:
            print "tomatch: "+match
            cu.execute(match)
            lresult = cu.fetchall()
            print "executeresult: "+str(lresult)
            if len(lresult)<=0:
                tempnum+=1
        if tempnum==0:
            result=0  
        cu.close()
        cx.close()
    if "deldb" in resulttype:
        dbpath = resultjsondic["dbpath"]
        tomatch = resultjsondic["tomatch"]
##        tomatchlist=tomatch.split(';')
##        print tomatchlist
        print "tomatch: "+tomatch
        amcommand = "adb -s " + sn + " pull "+dbpath+" ./test.db"
        os.system(amcommand)
        time.sleep(3)
        cx = sqlite3.connect("./test.db")
        cu = cx.cursor() 
        cu.execute(tomatch)
        lresult = cu.fetchall()
##         print "executeresult: "+str(lresult)
        if len(lresult)==0:
            result=0
        cu.close()
        cx.close()
    elif "volume" in resulttype:
##        print "result:"+res
        tomatch = resultjsondic['tomatch']
        print "tomatch: "+tomatch
        operation = resultjsondic['operation']
        print "operation: "+operation
        amcommand = "adb -s " + sn + " shell \""+tomatch+"\""
        test=os.popen(amcommand)
        time.sleep(1)
        text=test.read()
        test.close()
        currentvolume = text.split("   ")[0].split(' ')[-1][-1]
        print "currentvolume: "+currentvolume
        if 'up' in operation:
##            print "currentvolume: "+currentvolume
            print "old_volume: "+old_volume
            if old_volume=='f':
                if currentvolume=='f':
                    result=0
            else:      
                if currentvolume > old_volume:
                    result=0
        elif 'low' in operation:
##            print "currentvolume: "+currentvolume
            print "old_volume: "+old_volume
            if old_volume=='0':
                if currentvolume=='0':
                    result=0
            else:        
                if currentvolume < old_volume:
                    result=0
        elif 'min' in operation:
            if currentvolume =='9':
                result=0
                
        elif 'max' in operation:
            if currentvolume == 'f':
                result=0
                
        elif 'silent' in operation:
            if currentvolume == '0':
                result=0
            
        elif int(operation)<=0:
            if currentvolume == '0':
                result=0
        elif int(operation)>0 and int(operation)<=25:
            if currentvolume == '9':
                result=0
        elif int(operation)>25 and int(operation)<=50:
            if currentvolume == 'b':
                result=0
        elif int(operation)>50 and int(operation)<=75:
            if currentvolume == 'd':
                result=0
        elif int(operation)>75:
            if currentvolume == 'f':
                result=0
            
    elif "log" in resulttype:
##        print "result:"+res
        tomatch = resultjsondic['tomatch']
        tomatchlist=tomatch.split(';')
        print "tomatch: "+tomatch
        for match in tomatchlist:
            if match in res:
                result=0

    elif "xml" in resulttype:
        tomatch = resultjsondic['tomatch']
        xmlpath = resultjsondic['xmlpath']
        linetag = resultjsondic['linetag']
        tomatchlist=tomatch.split(';')
        print "tomatch: "+tomatch
        print "linetag: "+linetag
        cmd="adb -s "+ sn + " shell \" cat  " +xmlpath +" | grep "+linetag+"\""
        test=os.popen(cmd)
        time.sleep(3)
        text=test.read()
        test.close()
        print  text
        if tomatch in text:
            result=0

    return result
