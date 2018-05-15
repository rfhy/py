# -*- coding: UTF-8 -*-

import os,sys
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart  #attach
from email.mime.image import MIMEImage #picture


def Sendmail():

    mail_host="smtp.163.com"
    mail_user="roobosz"
    mail_pass="ROOBOSZ2016"

    sender = 'roobosz@163.com'
    rece = ['jianglirun@roobo.com']
    tolist = ";".join(rece)

    message = MIMEText("附件邮件的正文", _subtype='html', _charset='utf-8')
 

    fujian = MIMEMultipart()

    fujian['From'] = sender

    fujian['To'] = tolist    

    subject = 'OTA测试报告'

    fujian['subject'] = Header(subject, 'utf-8')
    

    fujian.attach(message)
    

    att1 = MIMEText(open('d:\\reset.rar', 'rb').read(), 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="rename.rar"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
    fujian.attach(att1)
    

    att2 = MIMEText(open('d:\\180_180.txt', 'rb').read(), 'base64', 'gb2312')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="180_180.txt"'
    fujian.attach(att2)


    try:
        
        s = smtplib.SMTP()

        s.connect(mail_host, 25)

        s.login(mail_user, mail_pass)

        s.sendmail(sender, rece, fujian.as_string())

        print("Send sucess")

    except Exception, e:
        
        print str(e) 

        print("Send fail")


if __name__ == '__main__':

    Sendmail()

        

    
