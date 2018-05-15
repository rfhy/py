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

    
    nr = '-- 这是一个纯文本邮件 --'    
    message = MIMEText(nr, _subtype='plain', _charset='utf-8')

    message['From'] = sender

    message['To'] = tolist    

    subject = 'OTA测试报告'

    message['subject'] = Header(subject, 'utf-8')
    


    try:
        
        s = smtplib.SMTP()

        s.connect(mail_host, 25)

        s.login(mail_user, mail_pass)

        s.sendmail(sender, rece, message.as_string())

        print("Send sucess")

    except Exception, e:
        
        print str(e) 

        print("Send fail")


if __name__ == '__main__':

    Sendmail()

        

    
