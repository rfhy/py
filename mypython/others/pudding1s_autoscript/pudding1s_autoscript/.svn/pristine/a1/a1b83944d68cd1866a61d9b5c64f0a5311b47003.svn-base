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
reload(sys)
sys.setdefaultencoding('utf-8')

# first url request
def yuyinchangshouge():
	sn=" -s 1011000000111007 "
	pslogcat="adb "+ sn +"shell \"ps |grep logcat\""
	output = os.popen(pslogcat)
	output = output.read()
	if  "root" not in output:
	            print "There is not logcat process"
	else:
		str = output.split("root")
		val = str[1]
		val = val.lstrip()
		val = val.split(" ")
		pid = val[0]
		command="adb "+ sn + "shell kill -9  "+ pid
		print command
		os.system(command)	
	rmlog="adb "+ sn +"shell \"rm -fr /sdcard/yuyinchangshouge.log \""
	os.system(rmlog)
	cppcm="adb "+ sn +"shell \"busybox cp /sdcard/nihao.pcm /sdcard/test_wakeup.pcm \""
	os.system(cppcm)
	pidstart = 0
	while(pidstart<1):
		pidlogcat="adb "+ sn +"shell \"busybox nohup logcat -v time  -f /sdcard/yuyinchangshouge.log & \""
		test=os.popen(pidlogcat)
		time.sleep(3)
		test=test.read()
		if  "nohup" in test:
			pidstart = 1
			print 'logcat successful'
		else:
			print "logcat failed"
		time.sleep(5)
		
	wakeup = 0
	while(wakeup<1):
		amcommand="adb "+ sn +"shell \"am startservice -n com.juan.voiceservice/com.juan.audio.service.TestWakeUpService\""
		os.system(amcommand)
		time.sleep(3)
		checkloghx="adb "+ sn +"shell \"cat /sdcard/yuyinchangshouge.log |grep -E '唤醒|你好'\""
		output = os.popen(checkloghx)
		res= output.read()
		print "huanxin score:",res
		if '唤醒词' in res or '你好布丁' in res:
			wakeup = 1
			print 'wakeup successful'
		else:
			print 'wakeup failed'
			
	time.sleep(10)	    		
	cpclock="adb "+ sn +"shell \"busybox cp /sdcard/changsg.pcm /sdcard/test_wakeup.pcm \""
	os.system(cpclock)
	os.system(amcommand)
	time.sleep(10)
		
	checklogclock="adb "+ sn +"shell \"cat /sdcard/yuyinchangshouge.log |grep paramJasonStr\""
	output = os.popen(checklogclock)
	time.sleep(3)
	res= output.read()
	print "changshouge logcat",res
	if 'singer' in res:
		print 'set changshouge successful';
	else:
		print 'set changshouge failed'
		return False
	
	time.sleep(3)
	
	wakeup = 0
	while(wakeup<1):
		cppcm="adb "+ sn +"shell \"busybox cp /sdcard/nihao.pcm /sdcard/test_wakeup.pcm \""
		os.system(cppcm)
		amcommand="adb "+ sn +"shell \"am startservice -n com.juan.voiceservice/com.juan.audio.service.TestWakeUpService\""
		os.system(amcommand)
		time.sleep(3)
		checkloghx="adb "+ sn +"shell \"cat /sdcard/yuyinchangshouge.log |grep score\""
		output = os.popen(checkloghx)
		res= output.read()
		print "daduan score:",res
		if 'wakeup' in res:
			wakeup = 1
			print 'daduan successful'
		else:
			print 'daduan failed'
		
	time.sleep(3)
	sleep = 0
	while(sleep<1):
		cpbye="adb "+ sn +"shell \"busybox cp /sdcard/bye.pcm /sdcard/test_wakeup.pcm \""
		os.system(cpbye)
		os.system(amcommand)
		time.sleep(3)
		checklogsleep="adb "+ sn + "shell \"cat /sdcard/yuyinchangshouge.log |grep paramJasonStr\""
		sleepoutput = os.popen(checklogsleep)
		res= sleepoutput.read()	
		print "sleep logcat",res
		if 'sleep' in res:
			print 'sleep successful';
			sleep=1
		else:
			print "sleep failed"
					
	time.sleep(1)
	output = os.popen(pslogcat)
	output = output.read()
	if  "root" in output:
				str = output.split("root")
				val = str[1]
				val = val.lstrip()
				val = val.split(" ")
				pid = val[0]
	killpid="adb "+ sn +"shell kill -9  "+ pid
	os.system(killpid)
	return True	









        
    
        
