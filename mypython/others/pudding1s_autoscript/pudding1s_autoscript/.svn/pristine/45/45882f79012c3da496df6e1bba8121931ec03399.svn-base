# coding: utf-8 
try: 
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET 
import sys 
import os

path = "D:\\script\\puddingsmain.xml"
if os.path.exists(path):
  tree = ET.parse(path)
  root =  tree.getroot()
else:
  root =  None

yuyinpath = "D:\\script\\speechcase.xml"
if os.path.exists(yuyinpath):
  yuyintree = ET.parse(yuyinpath)
  yuyinroot =  yuyintree.getroot()
else:
  yuyinroot =  None

longcnnpath = "D:\\script\\longcnncase.xml"
if os.path.exists(longcnnpath):
  longcnntree = ET.parse(longcnnpath)
  longcnnroot =  longcnntree.getroot()
else:
  longcnnroot =  None
  
def  Getspeechcase(name): 
  strdata=''
  strresult=''
  try:
    if yuyinroot !=None:
      for case in yuyinroot.findall('case'):
      ##        print case.get('name')
        if name == case.get('name') :
          strdata = case.find('data').text.strip()
          strresult = case.find('result').text.strip()
  except Exception, e: 
    print "MyUtil.Getyuyincase Error: "+str(e)

  return strdata ,strresult

def  Getlongcnncase(name): 
  strdata=''
  strresult=''
  try:
    if longcnnroot !=None:
      for case in longcnnroot.findall('case'):
##        print case.get('name')
        if name == case.get('name') :
          strdata = case.find('data').text.strip()
          strresult = case.find('result').text.strip()
  except Exception, e: 
    print "MyUtil.Getlongcnncase Error: "+str(e)

  return strdata ,strresult
    
def  Getfile(name):
  adress=''
  try:
    if root !=None:
      adress = root.find('file').find(name).text
      
  except Exception, e: 
    print "MyUtil.Getfile Error :"+str(e)
    
  return adress
      
#暂时支持 pudding1s 和puddingve        
def Geturl(taskname):
    downurl     = ''
    infourl     = ''
    buildnumurl = '' 
    buildnum    = ''
    branch      = ''
    try:
        if root !=None:    
          for task in root.findall('task'):
            if taskname == task.get('name') :
              buildnum    = task.get('buildnum')
              branch      = task.get('branch')
              url         = task.get('url')
              #默认测试最大build版本号
              if '0' == buildnum:
                downurl     = url + '/' + branch + '/' + 'lastSuccessfulBuild/artifact/'
                infourl     = url + '/' + branch + '/' + 'lastSuccessfulBuild/api/json?depth=1'
                buildnumurl = url + '/' + branch + '/' + 'lastSuccessfulBuild/buildNumber'
                
                
              #测试指定版本号  
              else:
                downurl     = url + '/' + branch + '/' + buildnum + '/artifact/'
                infourl     = url + '/' + branch + '/' + buildnum + '/api/json?depth=1'
                buildnumurl = url + '/' + branch + '/' + buildnum + '/buildNumber'
                
    except Exception, e: 
        print "MyUtil.Getveurl Error: "+str(e)
          
    return  downurl, infourl ,buildnumurl,buildnum,branch
  
def Getsn():
    sn=''
    try:
        if root !=None:
          sn = root.get('sn')     
        
    except Exception, e: 
        print "MyUtil.Getsn Error: "+str(e)
    return sn
    
def Getphonenum():
    phonenum=''
    try:
        if root !=None:
          phonenum = root.get('phonenum')     
        
    except Exception, e: 
        print "MyUtil.Getsn Error: "+str(e)
    return phonenum

def Getpid():
    pid=''
    try:
        if root !=None:
          pid = root.get('pid')     
        
    except Exception, e: 
        print "MyUtil.Getsn Error: "+str(e)
    return pid

def Getpasswd():
    passwd=''
    try:
        if root !=None:
          passwd = root.get('passwd')     
        
    except Exception, e: 
        print "MyUtil.Getsn Error: "+str(e)
    return passwd



##print Getlongcnncase("textToSpeech_english")
