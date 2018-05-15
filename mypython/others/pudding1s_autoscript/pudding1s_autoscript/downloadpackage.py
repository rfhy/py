#encoding: utf-8
import urllib2
import urllib
import cookielib
import json
import os
import sys
import string
import time
import ConfigParser
import MyUtil
# Get new build number
##reload(sys)
##sys.setdefaultencoding('utf-8')
##root = MyUtil.get_root('D:\\script\\puddingsmain.xml')
docadress = MyUtil.Getfile('doc')
buildadress = MyUtil.Getfile('build')
reportadress = MyUtil.Getfile('server')
sn = MyUtil.Getsn()
def GetNewNumber(Uri):
##       Uri = "http://jenkins.365jiating.com:8080/job/pudding2.0/lastSuccessfulBuild/buildNumber";
       reqs = urllib2.Request(Uri)
       ress = urllib2.urlopen(reqs)
       stringnumber = ress.read()
       newnumber = int(stringnumber)
       return newnumber
      # print "newnumber", newnumber
#Get old build number
def GetOldNumber(strname):
       cf = ConfigParser.ConfigParser()
       cf.read(docadress)
       oldnumber = cf.getint("apkname", strname)
       return oldnumber

def SetOldNumber(strname,value):
       cf = ConfigParser.ConfigParser()
       cf.read(docadress)
       cf.set("apkname", strname, value)
       cf.write(open(docadress,"w"))
#check new build status
def CheckNewBuildStatus(Uri):
##       jsonurl="http://jenkins.365jiating.com:8080/job/pudding2.0/lastSuccessfulBuild/api/json?depth=1"
       reqs = urllib2.Request(Uri)
       ress = urllib2.urlopen(reqs)
       try:
              response = ress.read();
              resultjson = json.loads(response)
              result = resultjson['result']
              if 'SUCCESS' in result:
                      # print 'New build status is successful';
                     return True
              else:
                       #print 'New build status is failed';
                       #exit(1);
                     return False

       except urllib2.HTTPError,e:
              print 'error resultcode:',e.code;
              print 'error msg:',(e.read().decode('utf-8'))

#compare with new build number and old build number
def DownloadAPK(Uri,downloadurl,newnum,dirname):
       dirpath =buildadress+ dirname + "/" + newnum
       if os.path.exists(dirpath)  == False:
              os.mkdir(dirpath)
       reqs = urllib2.Request(Uri)
       ress = urllib2.urlopen(reqs)
       response = ress.read()
       resultjson = json.loads(response)
       artifactslist = resultjson['artifacts']
       for i in artifactslist:
              if '.apk' in i['relativePath'] and 'alpha' in i['relativePath']:
                     urllib.urlretrieve(downloadurl+i['relativePath'], dirpath+'\\'+i['fileName'])
              elif 'Voice-debug'in i['relativePath']:
                     urllib.urlretrieve(downloadurl+i['relativePath'], dirpath+'\\'+i['fileName'])
                     
# install to device
def InstallAPK():
       
       ps_downurl,ps_infourl,ps_buildnumurl,ps_buildnum,ps_branch = MyUtil.Geturl('pudding1s')
       ve_downurl,ve_infourl,ve_buildnumurl,ve_buildnum ,ve_branch = MyUtil.Geturl('puddingve')
       if ps_buildnum == '0':
               pudding2newnum = GetNewNumber(ps_buildnumurl)   
       else:
              pudding2newnum = ps_buildnum
              
       if ve_buildnum == '0':
               puddingVEnewnum = GetNewNumber(ve_buildnumurl)
       else:
              puddingVEnewnum = ve_buildnum
              
       pudding2oldnum = GetOldNumber(ps_branch)
       puddingVEoldnum = GetOldNumber(ve_branch)
       print "pudding2oldnum: "+str(pudding2oldnum)
       print "pudding2newnum: "+str(pudding2newnum)
       print "puddingVEoldnum: "+str(puddingVEoldnum)
       print "puddingVEnewnum: "+str(puddingVEnewnum)
       if CheckNewBuildStatus(ps_infourl) :
              if pudding2newnum > pudding2oldnum:
                     #pudding report dir
                     print "Create report dir"
                     reportpath=reportadress + str(pudding2newnum)
                     print "reportpath: ",reportpath
                     if os.path.exists(reportpath)  == False:
                            os.mkdir(reportpath)
                     #pudding2.0
##                            Uri = "http://jenkins.365jiating.com:8080/job/pudding2.0/lastSuccessfulBuild/api/json?depth=1"
##                            downloadurl = "http://jenkins.365jiating.com:8080/job/pudding2.0/lastSuccessfulBuild/artifact/"
##                            dirname = 'pudding2.0'
                     DownloadAPK(ps_infourl,ps_downurl,str(pudding2newnum),ps_branch)
                     print "Download pudding1s APK succeed"
                     # if VE build successed
                     if CheckNewBuildStatus(ve_infourl):
                            if puddingVEnewnum > puddingVEoldnum:
                                   #puddingVE
##                                          Uri = "http://jenkins.365jiating.com:8080/job/VoiceEngin_Voice/lastSuccessfulBuild/api/json?depth=1"
##                                          downloadurl = "http://jenkins.365jiating.com:8080/job/VoiceEngin_Voice/lastSuccessfulBuild/artifact/"
##                                          dirname = 'puddingve'
                                   DownloadAPK(ve_infourl,ve_downurl,str(puddingVEnewnum),ve_branch)
                                   print "Download puddingVE APK succeed"
                                   #write config。。。
##                                          strname = ve_branch
                                   SetOldNumber(ve_branch,str(puddingVEnewnum))
                                   print "Modify puddingve build number ", puddingVEnewnum
                                   #install。。。。。。
                                   path= buildadress + ve_branch+"/" + str(puddingVEnewnum)
                                   print path
                                   os.chdir(path)
                                   listfile=os.listdir(os.getcwd())
                                   apk0 = "adb -s " + sn + " install -r " + listfile[0]
                                   print apk0
                                   os.system(apk0)
                                   time.sleep(180)
                    
       
                     dirpath= buildadress + ps_branch +"/" + str(pudding2newnum)
                     print "install apk.."
                     parents = os.listdir(dirpath)
                     for parent in parents:
                            path = os.path.join(dirpath,parent)
                            apkcmd = "adb -s "+ sn +" install -r " + path
                            print apkcmd
                            os.system(apkcmd)
                            time.sleep(30)
                     os.system("adb -s " + sn +" devices")
                      #write config。。。              
##                            strname = 'pudding2.0'
                     SetOldNumber(ps_branch,str(pudding2newnum))
                     print "Modify pudding2.0 build number ", pudding2newnum
                     os.system("adb -s "+ sn + "shell \" busybox pkill com.roobo* \"")
                     print "busybox pkill com.roobo* "
                     os.system("adb -s "+ sn + "shell \" busybox pkill com.juan* \"")
                     print "busybox pkill com.juan* "
                     time.sleep(120)
                      
                     

InstallAPK()



	  
