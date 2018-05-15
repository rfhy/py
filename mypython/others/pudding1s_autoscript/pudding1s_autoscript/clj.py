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
Uri = MyUtil.Getfile("host")
def sendclj(sendaction):
    printstr = sendaction["action"]
    test_data = {"action":"mc/tomcserver","data":{"mcserver":"10.51.52.40:7073","cmddata":sendaction}}           
    jdata = json.dumps(test_data)
    requrl = Uri+"/test/mctest"
    req = urllib2.Request(requrl,jdata)
    print req
    try:
        res_data = urllib2.urlopen(req)
      
        res = res_data.read()
        
        print printstr+" is " +res
       
        s = json.loads(res)
       
        returncode = s["result"]
       
        if 0 == returncode:
                print 'Passed:return  0 successed '
##                return True
        else:
                print 'Failed:error msg: return '+str(returncode) + " failed please check "+ printstr
##                return False
        return returncode
        res_data.close()
            
            
    except urllib2.HTTPError,e:
        print 'error resultcode:',e.code;
        print 'error msg:',(e.read().decode('utf-8'));
        return -1

    
##sendaction = {"action":"AlarmCenter/defenceState","data":{"isauto":False,"mainctl":"101100000011101A","state":False},"id":20832}
##sendclj(sendaction)
