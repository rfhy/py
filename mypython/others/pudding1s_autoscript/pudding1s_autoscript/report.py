#encoding: utf-8
import urllib2
import urllib
import cookielib
import json
import os
import sys
import string
import smtplib
import datetime
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.mime.base import MIMEBase
import email.MIMEMultipart# import MIMEMultipart  
import email.MIMEText# import MIMEText  
import email.MIMEBase# import MIMEBase  
import ConfigParser
import shutil
import MyUtil
# Get new build number
##reload(sys)
##sys.setdefaultencoding('utf-8')
#初始化参数
sn = MyUtil.Getsn()
memoryscript = MyUtil.Getfile("memoryscript")
wwwserver = MyUtil.Getfile("server")
report = MyUtil.Getfile("report")

#获得老的版本
def GetOldNumber(strname):
       cf = ConfigParser.ConfigParser()
       cf.read(MyUtil.Getfile("doc"))
       oldnumber = cf.getint("apkname", strname)
       return oldnumber

#发送邮件
def emailmsgtodev(sendmsg):
        
##        #nowtime
##        now = datetime.datetime.now()
##        NowStyleTime = now.strftime("%H:%M:%S")
##        #7dayago
##        DayAgo = (datetime.datetime.now() - datetime.timedelta(days = 1))
##        DayAgoStyleTime = DayAgo.strftime("%Y-%m-%d")

        sender = 'test@roo.bo'
        ##    receiver = ['swtest@roo.bo','develop@roo.bo']
        receiver=['wanglibin@roo.bo','mashuai@roo.bo','xushengqi@roo.bo','liuxin@roobo.com','liuxin01@roobo.com','zhanghailong@roo.bo','lizhenguo@roo.bo']
        subject = 'Pudding1s Test report'
        smtpserver = 'mail.roo.bo'

##
##        crashdata = 'Hi，all 服务器上<b>布丁1s所有版本</b>  '+DayAgoStyleTime+'--今天'+NowStyleTime+' 的 NativeCrash 信息统计如下,请仔细查看：\n\n'
##        crashdata = crashdata + resultnativep1sall
##        crashdata = crashdata.replace('\n','<br/>')
##
        #5.设置并发送邮件
        sendmsg = sendmsg.replace('\n','<br/>')
        msg = MIMEMultipart('related')
        msgText = MIMEText(sendmsg,'html','utf-8')
        msg.attach(msgText)
##        ## 发送附件－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－ 
##        contype = 'application/octet-stream'  
##        maintype, subtype = contype.split('/', 1)  
##        for ll in zipfilelist:
##                data = open(ll, 'rb')  
##                file_msg = MIMEBase(maintype, subtype)  
##                file_msg.set_payload(data.read())  
##                data.close( )  
##                email.Encoders.encode_base64(file_msg)#把附件编码  
##                ## 设置附件头  
##                basename = os.path.basename(ll)
##                print '附件头：' +basename
##                file_msg.add_header('Content-Disposition','attachment', filename = basename)#修改邮件头  
##                msg.attach(file_msg)
##        #－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－  
        msg['Subject'] = Header(subject, 'utf-8')
##        msg['Cc'] = 'wanglibin@roo.bo,mashuai@roo.bo,xushengqi@roo.bo,liuxin@roobo.com,liuxin01@roobo.com,zhanghailong@roo.bo,lizhenguo@roo.bo'
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver,"465")
        smtp.starttls()
        smtp.login('test', 'roobo@2015')
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()


#发送邮件
def emailmsgtotest(sendmsg):
        
##        #nowtime
##        now = datetime.datetime.now()
##        NowStyleTime = now.strftime("%H:%M:%S")
##        #7dayago
##        DayAgo = (datetime.datetime.now() - datetime.timedelta(days = 1))
##        DayAgoStyleTime = DayAgo.strftime("%Y-%m-%d")

        sender = 'test@roo.bo'
        ##    receiver = ['swtest@roo.bo','develop@roo.bo']
        receiver=['pdswtest@roo.bo']
        subject = 'Pudding1s Test report'
        smtpserver = 'mail.roo.bo'

##
##        crashdata = 'Hi，all 服务器上<b>布丁1s所有版本</b>  '+DayAgoStyleTime+'--今天'+NowStyleTime+' 的 NativeCrash 信息统计如下,请仔细查看：\n\n'
##        crashdata = crashdata + resultnativep1sall
##        crashdata = crashdata.replace('\n','<br/>')
##
        #5.设置并发送邮件
        sendmsg = sendmsg.replace('\n','<br/>')
        msg = MIMEMultipart('related')
        msgText = MIMEText(sendmsg,'html','utf-8')
        msg.attach(msgText)
##        ## 发送附件－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－ 
##        contype = 'application/octet-stream'  
##        maintype, subtype = contype.split('/', 1)  
##        for ll in zipfilelist:
##                data = open(ll, 'rb')  
##                file_msg = MIMEBase(maintype, subtype)  
##                file_msg.set_payload(data.read())  
##                data.close( )  
##                email.Encoders.encode_base64(file_msg)#把附件编码  
##                ## 设置附件头  
##                basename = os.path.basename(ll)
##                print '附件头：' +basename
##                file_msg.add_header('Content-Disposition','attachment', filename = basename)#修改邮件头  
##                msg.attach(file_msg)
##        #－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－  
        msg['Subject'] = Header(subject, 'utf-8')
##        msg['Cc'] = 'pdswtest@roo.bo,wanglibin@roo.bo,mashuai@roo.bo,xushengqi@roo.bo,liuxin@roobo.com,liuxin01@roobo.com,zhanghailong@roo.bo,lizhenguo@roo.bo'
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver,"465")
        smtp.starttls()
        smtp.login('test', 'roobo@2015')
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
#复制测试报告
def SendReport():
       ps_downurl,ps_infourl,ps_buildnumurl,ps_buildnum,ps_branch = MyUtil.Geturl('pudding1s')
       pudding2oldnum = GetOldNumber(ps_branch)
       path= wwwserver + str(pudding2oldnum)
       os.chdir(path)
       os.system("adb pull /sdcard/autotestlog . ")
       time.sleep(60)
       os.system("adb pull /sdcard/pudding/log . ")
       time.sleep(60)
       shutil.move(wwwserver+'testreport.html','./testreport'+str(pudding2oldnum)+".html")
       shutil.move('d:\\www\\memoryresult.xls','./memoryresult'+str(pudding2oldnum)+".xls")

       print "Testreport website:" + report + str(pudding2oldnum) + "/testreport" + str(pudding2oldnum) + ".html"
       print "MemoryResult website:" + report + str(pudding2oldnum) + "/memoryresult" + str(pudding2oldnum) + ".xls"
       
       sendmsg = "TestCase website: " + report + str(pudding2oldnum) + "/testreport" + str(pudding2oldnum) + ".html\n"
       sendmsg += "MemoryResult website: " + report + str(pudding2oldnum) + "/memoryresult" + str(pudding2oldnum) + ".xls\n"
       sendmsgtodev = "TestCase website: " + report + str(pudding2oldnum) + "/testreport" + str(pudding2oldnum) + ".html\n"
       
       fhtml = open("D:/www/report/Pudding1sreport/"+ str(pudding2oldnum)+"/testreport" + str(pudding2oldnum) + ".html")
       flines =fhtml.readlines( )
       for line in flines:
              if "Failure" in line:
                     emailmsgtodev(sendmsgtodev)
##                     if "Error" in line:
##                            ss = line.split(" ")[-3]
##                            if int(ss)>0:
##                                   print "Failure : "+ss
##                                   print "send emailmsgtodev"
##                                   emailmsgtodev(sendmsgtodev)
##                     else:
##                            ss = line.split(" ")[-1].split("<")[0]
##                            if int(ss)>0:
##                                   print "Failure : "+ss
##                                   print "send emailmsgtodev"
##                                   emailmsgtodev(sendmsgtodev)
                            
       print "send emailmsgtotest "
       emailmsgtotest(sendmsg)
       fhtml.close()

   
SendReport()
