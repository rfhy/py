#encoding: utf-8
import urllib2
import urllib
import cookielib
import json
import os
import sys
import string
import time
import MyUtil
sn = MyUtil.Getsn()
# Get new build number
##Uri = "http://172.16.244.143:8080/job/pudding2.0/lastSuccessfulBuild/buildNumber";
##reqs = urllib2.Request(Uri)
##ress = urllib2.urlopen(reqs)
##stringnumber = ress.read()
##newnumber = int(stringnumber)
##print "newnumber", newnumber

cf = ConfigParser.ConfigParser()
doc = MyUtil.Getfile("doc")
cf.read(doc)
apknumber = cf.getint("apkname", "pudding2.0")


path= MyUtil.Getfile("server") + stringnumber
os.chdir(path)
listfile=os.listdir(os.getcwd())
os.system("pwd")
os.system("adb pull /sdcard/yuyindadiansheng.log .")
os.system("adb pull /sdcard/yuyinchangshouge.log .")
os.system("adb pull /sdcard/yuyinxiangyouzhuan.log .")
os.system("adb pull /sdcard/yuyinxiangzuozhuan.log .")
os.system("adb pull /sdcard/yuyinzuidasheng.log .")
os.system("adb pull /sdcard/yuyinzuixiaosheng.log .")
os.system("adb pull /sdcard/yuyinclock.log .")
os.system("adb pull /sdcard/yuyinjidian.log .")
os.system("adb pull /sdcard/yuyinjintiantianqi.log .")
os.system("adb pull /sdcard/yuyinpm25.log .")
os.system("cp /cygdrive/d/www/report/Pudding1sreport/testreport.html  .")

print "Testreport website:http://172.16.115.1/report/Pudding1sreport/"+stringnumber+"/testreport.html"
