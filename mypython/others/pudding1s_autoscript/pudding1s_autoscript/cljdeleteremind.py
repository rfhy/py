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

# first url request


def cljdeleteremind():
	Uri = "https://pds-api.roo.bo";
	src = 'geG^_s[3Kl123456'
	m1 = md5.new()
	m1.update(src)
	passwd = m1.hexdigest()

	# second time do url request, the cookiejar will auto handle the cookie
	loginUrl = Uri + "/users/login";
	para = {"action": "login","data": {"phonenum": "13810831154","passwd":passwd,"pushid" : "595711815360812521","wifimac":"E0:94:67:D8:D5:C4","tm":"1234"}}
	data = json.dumps(para) 
	req = urllib2.Request(loginUrl, data); 

	try:
		response = urllib2.urlopen(req);
		resstr = response.read();
		print "Login response:",resstr
		tokenlist = []
		tokenlist = resstr.split(',')
		strname = "\"token\":"
		templist = [] 
		accesstoken = ''
		for i in range(0,len(tokenlist)):
			if strname in tokenlist[i]:
				templist= tokenlist[i].split(':')
				print templist
				accesstoken =templist[1]
				print accesstoken
				accesstoken = accesstoken.strip('\"')
				break
		print 'Get the accesstoken:',accesstoken
		
		if 'token' in resstr:
			print 'Passed:Login successed ';
			pass;
		else:
			print 'Failed:error msg: Login fail, please check login';
			exit(1)
		response.close();

	except urllib2.HTTPError,e:
		   print 'error resultcode:',e.code;
		   print 'error msg:',(e.read().decode('utf-8'));

	requrl = Uri + "/messages/msglist"
	jdata ='''{"action": "msg/gethistorybytime","data": {"myid": "ps:f8e04e665c95bddc1865b1ca975eb0c3","token":"'''+ accesstoken +'''","start": 0,"category": 0,"count": 1,"reverse": true,"mainctl": "1011000000111007"}}'''
	req = urllib2.Request(requrl,jdata)

	try:
		res_data = urllib2.urlopen(req)
		res = res_data.read()
		print res
		eventidlist = []
		eventidlist = res.split(',')
		strname = "\"eventId\":"
		templist = [] 
		eventID = ''
		for i in range(0,len(eventidlist)):
			if strname in eventidlist[i]:
				templist= eventidlist[i].split(':')
				eventID =templist[2]
				eventID = eventID.strip('\"')
				break
		print 'Get the eventID:',eventID
		if ':0' in res:
			print 'Passed: eventID successed ';
		else:
			print 'Failed:error msg: get eventID failed, please check get messages list';
			return False
		res_data.close();	
		
	except urllib2.HTTPError,e:
		print 'error resultcode:',e.code;
		print 'error msg:',(e.read().decode('utf-8'));
		return False
		
	eventID=int(eventID)
	requrl = Uri + "/mainctrls/mctlcmd"
	print "requrl",requrl
	test_detection = {"action": "VoiceServer/Delremind","data": {"mainctl": "1011000000111007","id":eventID,"myid":"ps:f8e04e665c95bddc1865b1ca975eb0c3","token":accesstoken}}
	print "delete remind response",test_detection
	jdata = json.dumps(test_detection) 
	req = urllib2.Request(requrl,jdata)
	print req

	try:
		res_data = urllib2.urlopen(req)
		res = res_data.read()
		print "Delete Clock",res
		if '' in res:
			print 'Passed:Delete Clock successed ';
		else:
			print 'Failed:error msg: Delete Clock failed, please check delete clock';
			return False
		res_data.close();	
		
	except urllib2.HTTPError,e:
		print 'error resultcode:',e.code;
		print 'error msg:',(e.read().decode('utf-8'));
		return False
		
	time.sleep(1)



	
		






        
    
        
