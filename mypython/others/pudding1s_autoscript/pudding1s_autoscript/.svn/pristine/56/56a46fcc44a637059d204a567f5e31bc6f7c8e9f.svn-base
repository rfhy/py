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


def cljttsbiaoqing():
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

	requrl = Uri + "/mainctrls/mctlcmd"
	test_ttsshow = {"action": "LedControl/showExpression","data": {"mainctl": "1011000000111007","type":"2","myid" : "ps:f8e04e665c95bddc1865b1ca975eb0c3","token":accesstoken}}
	jdata = json.dumps(test_ttsshow) 
	req = urllib2.Request(requrl,jdata)
	print req

	try:
		res_data = urllib2.urlopen(req)
		res = res_data.read()
		print "ttsbiaoqing result,type is 3",res
		if ':0' in res:
			print 'Passed:tts biaoqing successed,type is 3 ';
		else:
			print 'Failed:error msg: tts biaoqing failed,type is 3, please check tts biaoqing';
			return False
		res_data.close();	
		
	except urllib2.HTTPError,e:
		print 'error resultcode:',e.code;
		print 'error msg:',(e.read().decode('utf-8'));
		return False
	
	time.sleep(5)
	test_ttsshow = {"action": "LedControl/showExpression","data": {"mainctl": "1011000000111007","type":"3","myid" : "ps:f8e04e665c95bddc1865b1ca975eb0c3","token":accesstoken}}
	jdata = json.dumps(test_ttsshow) 
	req = urllib2.Request(requrl,jdata)
	print req

	try:
		res_data = urllib2.urlopen(req)
		res = res_data.read()
		print "ttsbiaoqing result,type is 3",res
		if ':0' in res:
			print 'Passed:tts biaoqing successed ,type is 3';
		else:
			print 'Failed:error msg: tts biaoqing failed,type is 3, please check tts biaoqing';
			return False
		res_data.close();	
		
	except urllib2.HTTPError,e:
		print 'error resultcode:',e.code;
		print 'error msg:',(e.read().decode('utf-8'));
		return False
	
	time.sleep(5)
	test_ttsshow = {"action": "LedControl/showExpression","data": {"mainctl": "1011000000111007","type":"5","myid" : "ps:f8e04e665c95bddc1865b1ca975eb0c3","token":accesstoken}}
	jdata = json.dumps(test_ttsshow) 
	req = urllib2.Request(requrl,jdata)
	print req

	try:
		res_data = urllib2.urlopen(req)
		res = res_data.read()
		print "ttsbiaoqing result,type is 5",res
		if ':0' in res:
			print 'Passed:tts biaoqing successed ,type is 5';
		else:
			print 'Failed:error msg: tts biaoqing failed,type is 5, please check tts biaoqing';
			return False
		res_data.close();	
		
	except urllib2.HTTPError,e:
		print 'error resultcode:',e.code;
		print 'error msg:',(e.read().decode('utf-8'));
		return False

	time.sleep(5)
	test_ttsshow = {"action": "LedControl/showExpression","data": {"mainctl": "1011000000111007","type":"6","myid" : "ps:f8e04e665c95bddc1865b1ca975eb0c3","token":accesstoken}}
	jdata = json.dumps(test_ttsshow) 
	req = urllib2.Request(requrl,jdata)
	print req

	try:
		res_data = urllib2.urlopen(req)
		res = res_data.read()
		print "ttsbiaoqing result,type is 6",res
		if ':0' in res:
			print 'Passed:tts biaoqing successed ,type is 6';
		else:
			print 'Failed:error msg: tts biaoqing failed,type is 6, please check tts biaoqing';
			return False
		res_data.close();	
		
	except urllib2.HTTPError,e:
		print 'error resultcode:',e.code;
		print 'error msg:',(e.read().decode('utf-8'));
		return False

	time.sleep(5)
	test_ttsshow = {"action": "LedControl/showExpression","data": {"mainctl": "1011000000111007","type":"7","myid" : "ps:f8e04e665c95bddc1865b1ca975eb0c3","token":accesstoken}}
	jdata = json.dumps(test_ttsshow) 
	req = urllib2.Request(requrl,jdata)
	print req

	try:
		res_data = urllib2.urlopen(req)
		res = res_data.read()
		print "ttsbiaoqing result,type is 7",res
		if ':0' in res:
			print 'Passed:tts biaoqing successed ,type is 7';
		else:
			print 'Failed:error msg: tts biaoqing failed,type is 7, please check tts biaoqing';
			return False
		res_data.close();	
		
	except urllib2.HTTPError,e:
		print 'error resultcode:',e.code;
		print 'error msg:',(e.read().decode('utf-8'));
		return False
	
	time.sleep(5)
	test_ttsshow = {"action": "LedControl/showExpression","data": {"mainctl": "1011000000111007","type":"8","myid" : "ps:f8e04e665c95bddc1865b1ca975eb0c3","token":accesstoken}}
	jdata = json.dumps(test_ttsshow) 
	req = urllib2.Request(requrl,jdata)
	print req

	try:
		res_data = urllib2.urlopen(req)
		res = res_data.read()
		print "ttsbiaoqing result,type is 8",res
		if ':0' in res:
			print 'Passed:tts biaoqing successed ,type is 8';
		else:
			print 'Failed:error msg: tts biaoqing failed,type is 8, please check tts biaoqing';
			return False
		res_data.close();	
		
	except urllib2.HTTPError,e:
		print 'error resultcode:',e.code;
		print 'error msg:',(e.read().decode('utf-8'));
		return False

	time.sleep(5)
	test_ttsshow = {"action": "LedControl/showExpression","data": {"mainctl": "1011000000111007","type":"9","myid" : "ps:f8e04e665c95bddc1865b1ca975eb0c3","token":accesstoken}}
	jdata = json.dumps(test_ttsshow) 
	req = urllib2.Request(requrl,jdata)
	print req

	try:
		res_data = urllib2.urlopen(req)
		res = res_data.read()
		print "ttsbiaoqing result,type is 9",res
		if ':0' in res:
			print 'Passed:tts biaoqing successed ,type is 9';
		else:
			print 'Failed:error msg: tts biaoqing failed,type is 9, please check tts biaoqing';
			return False
		res_data.close();	
		
	except urllib2.HTTPError,e:
		print 'error resultcode:',e.code;
		print 'error msg:',(e.read().decode('utf-8'));
		return False
   
	time.sleep(5)
	test_ttsshow = {"action": "LedControl/showExpression","data": {"mainctl": "1011000000111007","type":"10","myid" : "ps:f8e04e665c95bddc1865b1ca975eb0c3","token":accesstoken}}
	jdata = json.dumps(test_ttsshow) 
	req = urllib2.Request(requrl,jdata)
	print req

	try:
		res_data = urllib2.urlopen(req)
		res = res_data.read()
		print "ttsbiaoqing result,type is 10",res
		if ':0' in res:
			print 'Passed:tts biaoqing successed ,type is 10';
		else:
			print 'Failed:error msg: tts biaoqing failed,type is 10, please check tts biaoqing';
			return False
		res_data.close();	
		
	except urllib2.HTTPError,e:
		print 'error resultcode:',e.code;
		print 'error msg:',(e.read().decode('utf-8'));
		return False
	
	time.sleep(5)
	test_ttsshow = {"action": "LedControl/showExpression","data": {"mainctl": "1011000000111007","type":"12","myid" : "ps:f8e04e665c95bddc1865b1ca975eb0c3","token":accesstoken}}
	jdata = json.dumps(test_ttsshow) 
	req = urllib2.Request(requrl,jdata)
	print req

	try:
		res_data = urllib2.urlopen(req)
		res = res_data.read()
		print "ttsbiaoqing result,type is 12",res
		if ':0' in res:
			print 'Passed:tts biaoqing successed ,type is 12';
		else:
			print 'Failed:error msg: tts biaoqing failed,type is 12, please check tts biaoqing';
			return False
		res_data.close();	
		
	except urllib2.HTTPError,e:
		print 'error resultcode:',e.code;
		print 'error msg:',(e.read().decode('utf-8'));
		return False
	
	time.sleep(5)
	test_ttsshow = {"action": "LedControl/showExpression","data": {"mainctl": "1011000000111007","type":"13","myid" : "ps:f8e04e665c95bddc1865b1ca975eb0c3","token":accesstoken}}
	jdata = json.dumps(test_ttsshow) 
	req = urllib2.Request(requrl,jdata)
	print req

	try:
		res_data = urllib2.urlopen(req)
		res = res_data.read()
		print "ttsbiaoqing result,type is 13",res
		if ':0' in res:
			print 'Passed:tts biaoqing successed ,type is 13';
		else:
			print 'Failed:error msg: tts biaoqing failed,type is 13, please check tts biaoqing';
			return False
		res_data.close();	
		
	except urllib2.HTTPError,e:
		print 'error resultcode:',e.code;
		print 'error msg:',(e.read().decode('utf-8'));
		return False
		
	time.sleep(5)
	test_ttsshow = {"action": "LedControl/showExpression","data": {"mainctl": "1011000000111007","type":"14","myid" : "ps:f8e04e665c95bddc1865b1ca975eb0c3","token":accesstoken}}
	jdata = json.dumps(test_ttsshow) 
	req = urllib2.Request(requrl,jdata)
	print req

	try:
		res_data = urllib2.urlopen(req)
		res = res_data.read()
		print "ttsbiaoqing result,type is 14",res
		if ':0' in res:
			print 'Passed:tts biaoqing successed ,type is 14';
		else:
			print 'Failed:error msg: tts biaoqing failed,type is 14, please check tts biaoqing';
			return False
		res_data.close();	
		
	except urllib2.HTTPError,e:
		print 'error resultcode:',e.code;
		print 'error msg:',(e.read().decode('utf-8'));
		return False
	
	time.sleep(5)
	test_ttsshow = {"action": "LedControl/showExpression","data": {"mainctl": "1011000000111007","type":"15","myid" : "ps:f8e04e665c95bddc1865b1ca975eb0c3","token":accesstoken}}
	jdata = json.dumps(test_ttsshow) 
	req = urllib2.Request(requrl,jdata)
	print req

	try:
		res_data = urllib2.urlopen(req)
		res = res_data.read()
		print "ttsbiaoqing result,type is 15",res
		if ':0' in res:
			print 'Passed:tts biaoqing successed ,type is 15';
			return True
		else:
			print 'Failed:error msg: tts biaoqing failed,type is 15, please check tts biaoqing';
			return False
		res_data.close();	
		
	except urllib2.HTTPError,e:
		print 'error resultcode:',e.code;
		print 'error msg:',(e.read().decode('utf-8'));
		return False
		

        
