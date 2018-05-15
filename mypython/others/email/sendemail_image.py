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

    nr = """
        <br>这是测试内嵌图片的邮件：\n</br>
        <br><img src='cid:6.jpg'></br>

    """

    message = MIMEText(nr, _subtype='html', _charset='utf-8')

    message['From'] = sender

    message['To'] = tolist    

    subject = 'OTA测试报告'

    message['subject'] = Header(subject, 'utf-8')
 

    fujian = MIMEMultipart()

    fujian['From'] = sender

    fujian['To'] = tolist    

    subject = 'OTA测试报告'

    fujian['subject'] = Header(subject, 'utf-8')
    

    fujian.attach(message)


    file1 = "D:\\6.jpg"
    image = MIMEImage(open(file1,'rb').read())
    image.add_header('Content-ID','<image1>')
    fujian.attach(image)

    

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

        

    
