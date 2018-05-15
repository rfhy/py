# -*- coding: UTF-8 -*-

import os,sys
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart  #attach
from email.mime.image import MIMEImage #picture


def Sendmail(nr="附件邮件的正文",subject='OTA测试报告',at1='d:\\reset.rar'):

    mail_host="smtp.163.com"
    mail_user="roobosz"
    mail_pass="ROOBOSZ2016"

    sender = 'roobosz@163.com'
    rece = ['jianglirun@roobo.com']
    tolist = ";".join(rece)

    message = MIMEText(nr, _subtype='html', _charset='utf-8')
 

    fujian = MIMEMultipart()

    fujian['From'] = sender

    fujian['To'] = tolist    

    fujian['subject'] = Header(subject, 'utf-8')
    

    fujian.attach(message)
    

    att1 = MIMEText(open(at1, 'rb').read(), 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = "attachment; filename=" + at1.split('\\')[-1]
    fujian.attach(att1)
    

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

        

    
