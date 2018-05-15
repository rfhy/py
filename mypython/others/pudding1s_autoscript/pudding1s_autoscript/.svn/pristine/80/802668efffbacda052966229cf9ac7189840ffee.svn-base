# -*- coding: utf-8 -*-
import StringIO
import sys
import os
import subprocess   
import unittest
import HTMLTestRunner
import time
import datetime
import urllib2
import urllib
import xlwt
import ConfigParser
import MyUtil

import longcnn
import speech

reload(sys)
sys.setdefaultencoding('utf-8')
sn = MyUtil.Getsn()
memoryscript = MyUtil.Getfile("memoryscript")
wwwserver = MyUtil.Getfile("server")
report = MyUtil.Getfile("report")
def GetOldNumber(strname):
       cf = ConfigParser.ConfigParser()
       cf.read(MyUtil.Getfile("doc"))
       oldnumber = cf.getint("apkname", strname)
       return oldnumber


# ----------------------------------------------------------------------

def safe_unicode(obj, *args):
    """ return the unicode representation of obj """
    try:
        ascii_text = str(obj).encode('string_escape')
        return unicode(obj, *args)
    except UnicodeDecodeError:
        # obj is byte string
        return unicode(ascii_text)

def safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('unicode_escape')

# ----------------------------------------------------------------------
# SDB tests to drive the HTMLTestRunner

class Pudding1sTest(unittest.TestCase):
    """ Pudding1s test case1

    """
    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)
           
    def test_zalongcnntextToSpeech_chinese(self):
        """    VoiceServer/textToSpeech_chinese test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('textToSpeech_chinese')
               result = longcnn.sendlongcnn(strdata,strresult,"textToSpeech_chinese",10)
               if(result == 0):
                  print "send  textToSpeech_chinese successful"
               else:
                  print "send  textToSpeech_chinese failure"
                  failcount +=1
                  
        if failcount >= 1:
               self.fail("textToSpeech_chinese FAILURE")
               
    def test_zalongcnntextToSpeechEnglish(self):
        """    VoiceServer/textToSpeechEnglish test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('textToSpeech_english')
               result = longcnn.sendlongcnn(strdata,strresult,"textToSpeech_chinese",10)
               if(result == 0):
                  print "send  textToSpeech_chinese successful"
               else:
                  print "send  textToSpeech_chinese failure"
                  failcount +=1
                  
        if failcount >= 1:
               self.fail("textToSpeech_chinese FAILURE")              
    def test_zblongcnnshowExpression(self):
        """    LedControl/showExpression test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('showExpression')
               result = longcnn.sendlongcnn(strdata,strresult,"showExpression",10)
               if(result == 0):
                  print "send  showExpression successful"
               else:
                  print "send  showExpression failure"
                  failcount +=1
        if failcount >= 1:
               self.fail("showExpression FAILURE")
           
    def test_zclongcnnsoundinteresting(self):
        """    VoiceServer/aiActions soundinteresting test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('soundinteresting')
               result = longcnn.sendlongcnn(strdata,strresult,"soundinteresting",10)
               if(result == 0):
                  print "send  soundinteresting successful"
               else:
                  print "send  soundinteresting failure"
                  failcount +=1
               
        if failcount >= 1:  
               self.fail(" soundinteresting FAILURE")
    
           
    def test_zdlongcnnchangeMasterVolume(self):
        """    VoiceServer/changeMasterVolume  test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('changeMasterVolume')
               result = longcnn.sendlongcnn(strdata,strresult,"changeMasterVolume",10)
               if(result == 0):
                  print "send   changeMasterVolume  successful"
               else:
                  print "send   changeMasterVolume failure"
                  failcount +=1
        if failcount >= 1:
               self.fail("changeMasterVolume  FAILURE")
           
    def test_zelongcnnnightModeEnableopen(self):
        """    VoiceServer/nightModeEnableopen test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('nightModeEnableopen')
               result = longcnn.sendlongcnn(strdata,strresult,"nightModeEnableopen",10)
               if(result == 0):
                  print "send  nightModeEnableopen successful"
               else:
                  print "send  nightModeEnableopen failure"
                  failcount +=1
        if failcount >= 1:
               self.fail("  nightModeEnableopen FAILURE")
           
    def test_zflongcnnnightModeEnableclose(self):
        """    VoiceServer/nightModeEnableclose test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('nightModeEnableclose')
               result = longcnn.sendlongcnn(strdata,strresult,"nightModeEnableclose",10)
               if(result == 0):
                  print "send  nightModeEnableclose successful"
               else:
                  print "send  nightModeEnableclose failure"
                  failcount +=1
        if failcount >= 1:
          
               self.fail("  nightModeEnableclose FAILURE")
           
    def test_zglongcnndefenceStateclose(self):
        """    AlarmCenter/defenceStateclose test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('defenceStateclose')
               result = longcnn.sendlongcnn(strdata,strresult,"defenceStateclose",10)
               if(result == 0):
                  print "send  defenceStateclose successful"
               else:
                  print "send  defenceStateclose failure"
                  failcount +=1
        if failcount >= 1:
           
               self.fail("  defenceStateclose FAILURE")
           
    def test_zhlongcnndefenceStateopen(self):
        """    AlarmCenter/defenceStateopen test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('defenceStatecloseopen')
               result = longcnn.sendlongcnn(strdata,strresult,"defenceStatecloseopen",10)
               if(result == 0):
                  print "send  defenceStatecloseopen successful"
               else:
                  print "send  defenceStatecloseopen failure"
                  failcount +=1
        if failcount >= 1:
          
               self.fail("  defenceStatecloseopen FAILURE")
           
    def test_zilongcnnuserEnterRemindopen(self):
        """    VideoMaster/userEnterRemindopen test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('userEnterRemindopen')
               result = longcnn.sendlongcnn(strdata,strresult,"userEnterRemindopen",10)
               if(result == 0):
                  print "send  userEnterRemindopen successful"
               else:
                  print "send  userEnterRemindopen failure"
                  failcount +=1
        if failcount >= 1:
               self.fail("  userEnterRemindopen FAILURE")
           
    def test_zjlongcnnuserEnterRemindclose(self):
        """    VideoMaster/userEnterRemindclose test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('userEnterRemindclose')
               result = longcnn.sendlongcnn(strdata,strresult,"userEnterRemindclose",10)
               if(result == 0):
                  print "send  userEnterRemindclose successful"
               else:
                  print "send  userEnterRemindclose failure"
                  failcount +=1
        if failcount >= 1:
          
               self.fail("  userEnterRemindclose FAILURE")
           
    def test_zkclgchangeSpeakernana(self):
        """    VoiceServer/changeSpeakernana test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('changeSpeakernannan')
               result = longcnn.sendlongcnn(strdata,strresult,"changeSpeakernannan",10)
               if(result == 0):
                  print "send  changeSpeakernannan successful"
               else:
                  print "send  changeSpeakernannan failure"
                  failcount +=1
        if failcount >= 1:
          
               self.fail("  changeSpeakernannan FAILURE")
           
    def test_zllongcnnchangeSpeakerrooboboy(self):
        """    VoiceServer/changeSpeakerroobo_boy test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('changeSpeakerrooboboy')
               result = longcnn.sendlongcnn(strdata,strresult,"changeSpeakerrooboboy",10)
               if(result == 0):
                  print "send  changeSpeakerrooboboy successful"
               else:
                  print "send  changeSpeakerrooboboy failure"
                  failcount +=1
        if failcount >= 1:
          
               self.fail("  changeSpeakerrooboboy FAILURE")
               
    def test_zmlongcnnFaceTrackStateclose(self):
        """    VideoMaster/FaceTrackStateclose test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('FaceTrackStateclose')
               result = longcnn.sendlongcnn(strdata,strresult,"FaceTrackStateclose",10)
               if(result == 0):
                  print "send  FaceTrackStateclose successful"
               else:
                  print "send  FaceTrackStateclose failure"
                  failcount +=1
        if failcount >= 1:
          
               self.fail("  FaceTrackStateclose FAILURE")
           
    def test_znlongcnnFaceTrackStateopen(self):
        """   VideoMaster/FaceTrackStateopen  test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('FaceTrackStateopen')
               result = longcnn.sendlongcnn(strdata,strresult,"FaceTrackStateopen",10)
               if(result == 0):
                  print "send  FaceTrackStateopen successful"
               else:
                  print "send  FaceTrackStateopen failure"
                  failcount +=1
        if failcount >= 1:
                 
               self.fail("  FaceTrackStateopen FAILURE")
               
    
           
    def test_zplongcnnStartTinyVideoState(self):
        """   VideoMaster/StartTinyVideoState  test
        """
        failcount = 0
        for i in range(3):
               time.sleep(15)
               strdata,strresult = MyUtil.Getlongcnncase('StartTinyVideoState')
               result = longcnn.sendlongcnn(strdata,strresult,"StartTinyVideoState",10)
               if(result == 0):
                  print "send  StartTinyVideoState successful"
               else:
                  print "send  StartTinyVideoState failure"
                  failcount +=1
        if failcount >= 1:
                 
               self.fail("  StartTinyVideoState FAILURE")    
    def test_zqlongcnnweather(self):
        """   VoiceServer/aiActions weather test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('weather')
               result = longcnn.sendlongcnn(strdata,strresult,"weather",20)
               if(result == 0):
                  print "send  weather successful"
               else:
                  print "send  weather failure"
                  failcount +=1
        if failcount >= 1:
               self.fail("  weather FAILURE")
           
    def test_zrlongcnnPM(self):
        """   VoiceServer/aiActions PM test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('PM')
               result = longcnn.sendlongcnn(strdata,strresult,"PM",20)
               if(result == 0):
                  print "send  PM successful"
               else:
                  print "send  PM failure"
                  failcount +=1
        if failcount >= 1:
          
               self.fail("  PM FAILURE")
           
    def test_zzdlongcnnsong(self):
        """   VoiceServer/aiActions song test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('song')
               result = longcnn.sendlongcnn(strdata,strresult,"song",15)
               if(result == 0):
                  print "send  song successful"
                  strdata,strresult = MyUtil.Getlongcnncase('stopsong')
                  result = longcnn.sendlongcnn(strdata,strresult,"stopsong",10)
                  if(result == 0):
                         print "send  stopsong successful"
                  else:
                         print "send  stopsong failure"
                         failcount +=1
               else:
                  print "send  song failure"
                  failcount +=1
        if failcount >= 1:
               self.fail("  song/stopsong FAILURE")
                                                               
##    def test_zzelongcnnstopsong(self):
##        """   VoiceServer/aiActions stopsong test
##        """
##        failcount = 0
##        for i in range(3):
##               time.sleep(5)
##               strdata,strresult = MyUtil.Getlongcnncase('stopsong')
##               result = longcnn.sendlongcnn(strdata,strresult,"stopsong",10)
##               if(result == 0):
##                  print "send  stopsong successful"
##               else:
##                  print "send  stopsong failure"
##                  failcount +=1
##        if failcount >= 1:
##          
##               self.fail("  stopsong FAILURE")
               
    def test_zulongcnnstartSoundWaveMode(self):
        """   VoiceServer/startSoundWaveMode test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('startSoundWaveMode')
               result = longcnn.sendlongcnn(strdata,strresult,"startSoundWaveMode",10)
               if(result == 0):
                  print "send  startSoundWaveMode successful"
               else:
                  print "send  startSoundWaveMode failure"
                  failcount +=1
               time.sleep(180)
        if failcount >= 1:
          
               self.fail("  startSoundWaveMode FAILURE")

    def test_zvlongcnnupdateApp(self):
        """   AppUpdater/updateApp   test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('updateApp')
               result = longcnn.sendlongcnn(strdata,strresult,"updateApp",10)
               if(result == 0):
                  print "send  updateApp successful"
               else:
                  print "send  updateApp failure"
                  failcount +=1
        if failcount >= 1:
          
               self.fail("  updateApp FAILURE")
               
    def test_zwlongcnnmotorRotate(self):
        """   DeviceManage/motorRotate test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('motorRotate')
               result = longcnn.sendlongcnn(strdata,strresult,"motorRotate",10)
               if(result == -10001 or result == 0):
                  print "send  motorRotate successful"
               else:
                  print "send  motorRotate failure"
                  failcount +=1
        if failcount >= 1:
          
               self.fail("  motorRotate FAILURE")
               
    def test_zxlongcnndelremind(self):
        """   VoiceServer/Delremind   test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('delremind')
               result = longcnn.sendlongcnn(strdata,strresult,"delremind",10)
               if(result == 0):
                  print "send  delremind successful"
               else:
                  print "send  delremind failure"
                  failcount +=1
        if failcount >= 1:
          
               self.fail("  delremind FAILURE")

    def test_zylongcnncloseRangeTTSHeartbeat(self):
        """   VoiceServer/closeRangeTTSHeartbeat  test
        """
        failcount = 0
        for i in range(3):
               time.sleep(20)
               strdata,strresult = MyUtil.Getlongcnncase('closeRangeTTSHeartbeat')
               result = longcnn.sendlongcnn(strdata,strresult,"closeRangeTTSHeartbeat",10)
               if(result == 0):
                  print "send  closeRangeTTSHeartbeat successful"
               else:
                  print "send  closeRangeTTSHeartbeat failure"
                  failcount +=1
        if failcount >= 1:
          
               self.fail("  closeRangeTTSHeartbeat FAILURE")
                         
    def test_zzlongcnnexitCloseRangeTTS(self):
        """   VoiceServer/exitCloseRangeTTS   test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('exitCloseRangeTTS')
               result = longcnn.sendlongcnn(strdata,strresult,"exitCloseRangeTTS",10)
               if(result == 0):
                  print "send  exitCloseRangeTTS successful"
               else:
                  print "send  exitCloseRangeTTS failure"
                  failcount +=1
        if failcount >= 1:
          
               self.fail("  exitCloseRangeTTS FAILURE")



    def test_zzalongcnnceremony(self):
        """   VoiceServer/ceremony   test
        """
        failcount = 0
        for i in range(3):
               time.sleep(20)
               strdata,strresult = MyUtil.Getlongcnncase('ceremony')
               result = longcnn.sendlongcnn(strdata,strresult,"ceremony",10)
               if(result == 0):
                  print "send  ceremony successful"
               else:
                  print "send  ceremony failure"
                  failcount +=1
        if failcount >= 1:
          
               self.fail("  ceremony FAILURE")

    
    def test_zzblongcnnsetVoiceParams(self):
        """   VoiceServer/setVoiceParams test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('setVoiceParams')
               result = longcnn.sendlongcnn(strdata,strresult,"setVoiceParams",10)
               if(result == 0):
                  print "send  setVoiceParams successful"
               else:
                  print "send  setVoiceParams failure"
                  failcount +=1
        if failcount >= 1:
          
               self.fail("  setVoiceParams FAILURE")
			   
    def test_zzclongcnnAddEngAlarm(self):
        """   VoiceServer/AddEngAlarm test
        """
        failcount = 0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getlongcnncase('AddEngAlarm')
               result = longcnn.sendlongcnn(strdata,strresult,"AddEngAlarm",10)
               if(result == 0):
                  print "send  AddEngAlarm successful"
               else:
                  print "send  AddEngAlarm failure"
                  failcount +=1
        if failcount >= 1:
          
               self.fail("  AddEngAlarm FAILURE")
    def test_aspeechturnright(self):
        """  pudding speech turn right test
        """
        failcount=0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getspeechcase(u'向右转')
               result = speech.sendspeech(strdata,strresult,"turnright",40)
               if(result == 0):
                  print "Pudding speech turn right  successful"
               else:
                  print "Pudding speech turn right failure"
                  failcount +=1
                  
        if failcount >= 1:
               self.fail("Pudding turn right FAILURE")
               
    def test_bspeechturnleft(self):
        """  pudding speech turn left  test
        """
        failcount=0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getspeechcase(u'向左转')
               result = speech.sendspeech(strdata,strresult,"turnleft",40)
               if(result == 0):
                  print "Pudding speech turn left  successful"
               else:
                  print "Pudding speech turn left failure"
                  failcount +=1
                  
                  	
        if failcount >= 1:
              self.fail("Pudding turn left FAILURE")
               
		   	   
    def test_cspeechminvolume(self):
        """    pudding speech minvolume test
        """
        failcount=0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getspeechcase(u'最小声')
               result = speech.sendspeech(strdata,strresult,"minvolume",40)
               if(result == 0):
                  print "Pudding speech minvolume  successful"
               else:
                  print "Pudding speech minvolume  failure"
                  failcount +=1
                  
                  	
        if failcount >= 1:
              self.fail("Pudding minvolume  FAILURE")

    def test_dspeechmaxvolume(self):
        """   pudding speech maxvolume test
        """
        failcount=0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getspeechcase(u'最大声')
               result = speech.sendspeech(strdata,strresult,"maxvolume",40)
               if(result == 0):
                  print "Pudding speech maxvolume  successful"
               else:
                  print "Pudding speech maxvolume  failure"
                  failcount +=1
                  
                  	
        if failcount >= 1:
              self.fail("Pudding maxvolume  FAILURE")

    def test_espeechlowvolume(self):
        """   pudding speech lowvolume test
        """
        failcount=0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getspeechcase(u'小点声')
               result = speech.sendspeech(strdata,strresult,"lowvolume",40)
               if(result == 0):
                  print "Pudding speech lowvolume  successful"
               else:
                  print "Pudding speech lowvolume  failure"
                  failcount +=1
                  
                  	
        if failcount >= 1:
              self.fail("Pudding lowvolume  FAILURE")
           
    def test_fspeechupvolume(self):
        """   pudding speech upvolume test
        """
        failcount=0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getspeechcase(u'大点声')
               result = speech.sendspeech(strdata,strresult,"upvolume",40)
               if(result == 0):
                  print "Pudding speech upvolume  successful"
               else:
                  print "Pudding speech upvolume  failure"
                  failcount +=1
                  
                  	
        if failcount >= 1:
              self.fail("Pudding upvolume  FAILURE")

    
    def test_gspeechwhen(self):
        """   pudding speech when test
        """
        failcount=0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getspeechcase(u'现在几点了')
               result = speech.sendspeech(strdata,strresult,"when",40)
               if(result == 0):
                  print "Pudding speech when  successful"
               else:
                  print "Pudding speech when  failure"
                  failcount +=1
                  
                  	
        if failcount >= 1:
              self.fail("Pudding when  FAILURE")	
    	   
    def test_hspeechweather(self):
        """   pudding speech weather test
        """
        failcount=0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getspeechcase(u'天气预报')
               result = speech.sendspeech(strdata,strresult,"weather",40)
               if(result == 0):
                  print "Pudding speech weather  successful"
               else:
                  print "Pudding speech weather  failure"
                  failcount +=1
                  
                  	
        if failcount >= 1:
              self.fail("Pudding weather  FAILURE")		
		   
    def test_ispeechpm(self):
        """   pudding speech pm test
        """
        failcount=0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getspeechcase(u'空气质量')
               result = speech.sendspeech(strdata,strresult,"pm",40)
               if(result == 0):
                  print "Pudding speech pm  successful"
               else:
                  print "Pudding speech pm  failure"
                  failcount +=1
                  
                  	
        if failcount >= 1:
              self.fail("Pudding pm  FAILURE")
		   
    
		   
    def test_jspeechsign(self):
        """   pudding speech sign test
        """
        failcount=0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getspeechcase(u'摩羯座星座运势')
               result = speech.sendspeech(strdata,strresult,"sign",120)
               if(result == 0):
                  print "Pudding speech sign  successful"
               else:
                  print "Pudding speech sign  failure"
                  failcount +=1
                  
                  	
        if failcount >= 1:
              self.fail("Pudding sign  FAILURE")
              
    def test_kspeechsilent(self):
        """   pudding speech silent test
        """
        failcount=0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getspeechcase(u'静音')
               result = speech.sendspeech(strdata,strresult,"silent",40)
               if(result == 0):
                  print "Pudding speech silent  successful"
               else:
                  print "Pudding speech silent  failure"
                  failcount +=1
                  
                  	
        if failcount >= 1:
              self.fail("Pudding silent  FAILURE")

    def test_lspeechschedule(self):
        """   pudding speech schedule test
        """
        failcount=0
        for i in range(3):
               time.sleep(5)
               strdata,strresult = MyUtil.Getspeechcase(u'一小时后提醒我测试')
               result = speech.sendspeech(strdata,strresult,"schedule",40)
               if(result == 0):
                  print "Pudding speech schedule  successful"
               else:
                  print "Pudding speech schedule  failure"
                  failcount +=1
                  
                  	
        if failcount >= 1:
              self.fail("Pudding schedule  FAILURE")
    def test_mspeechsong(self):
        """   pudding speech song test
        """
        time.sleep(5)
        strdata,strresult = MyUtil.Getspeechcase(u'唱首歌')
        result = speech.sendspeech(strdata,strresult,"song",40)
        if(result == 0):
           print "Pudding speech song  successful"
        else:
           print "Pudding speech song failure"
          
           self.fail("Pudding speech song FAILURE")	
		  	
		   
# This is the main test on HTMLTestRunner

class Test_HTMLTestRunner(unittest.TestCase):

    def test0(self):
        self.suite = unittest.TestSuite()
        buf = StringIO.StringIO()
        runner = HTMLTestRunner.HTMLTestRunner(buf)
        runner.run(self.suite)
        # didn't blow up? ok.
        self.assert_('</html>' in buf.getvalue())

    def test_main(self):
        # Run HTMLTestRunner. Verify the HTML report.

        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Pudding1sTest),
            ])

        # Invoke TestRunner
        strname = 'pudding2.0'
        pudding2oldnum = GetOldNumber(strname)
        fp=file(wwwserver+"testreport.html",'wb')
        print "Testreport website:" + report + str(pudding2oldnum) + "/testreport.html"
        runner = HTMLTestRunner.HTMLTestRunner(
                    stream=fp,
                    title='<Pudding1s Test>',
                    description='Pudding1s test report'
                    )
        runner.run(self.suite)
       


import unittest
if __name__ == "__main__":
       if len(sys.argv) > 1:
              argv = sys.argv
       else:
              argv=['test_HTMLTestRunner.py', 'Test_HTMLTestRunner']

       #初始化
       os.system("adb -s "+ sn + " shell \" rm  /sdcard/ve/recorder/normal/* \"")
       time.sleep(3)
       os.system("adb -s "+ sn + " shell \"am broadcast -a test.action --es key \"test_iat\" --es value \"false\"\"")
       time.sleep(3)
       os.system("adb -s "+ sn + " shell \" busybox pkill com.roobo* \"")
       print "kill com.roobo*"
       time.sleep(120)    
       os.system("adb -s "+ sn + " shell \" busybox pkill com.juan* \"")
       print "kill com.juan*"
       time.sleep(60)               
       cmd = "adb -s " + sn + " shell \" busybox pkill sh \""
       os.system(cmd)
       time.sleep(1)
       cmd = "adb -s " + sn + " shell \" rm -r  /sdcard/memoryresult \""
       os.system(cmd)
       time.sleep(1)
       cmd = "adb -s " + sn + " push  " + memoryscript + " /sdcard/"
       os.system(cmd)
       time.sleep(3)
       cmd = "adb -s " + sn + " shell \" rm -r  /sdcard/autotestlog \""
       os.system(cmd)
       time.sleep(3)
       cmd = "adb -s " + sn + " shell \" rm -rf  /sdcard/pudding/log/* \""
       os.system(cmd)
       time.sleep(3)
       #执行内存脚本
       while(True):
           
       ##        os.system("adb shell \"sh /sdcard/procrank.sh &\"")
              print "sh /sdcard/procrank.sh"
              cmd = "adb -s " + sn + " shell \"sh /sdcard/procrank.sh &\""
              sub1 = subprocess.Popen(cmd, shell=True)
              time.sleep(10)
              print "ls /sdcard/memoryresult "
              cmd = "adb -s " + sn + " shell \"ls /sdcard/memoryresult \""
              test = os.popen(cmd)
              text = test.read()
              time.sleep(2)
              test.close()
              print text
              if "No such file" in text:
                     continue
              else:
                     break
##       cmd = "python memoryresult.py"
##       sub2 = subprocess.Popen(cmd, shell=True)  
       unittest.main(argv=argv)
       time.sleep(60)
       
