# -*- encoding: UTF-8 -*-

import os,sys,time
from datetime import datetime

from useriface import device
from useriface import hostpc
from useriface import logger

import multiprocessing

sn = '151000010000002C'

global num
num = 0
test = 501

dev = device.Device(sn)
ui = dev.uidevice
pc = hostpc.Host(sn)
log = logger.Logger(__file__)
log.addLog2file('8909_wifi_ping2.log')

count = 60

on = ui(packageName='com.android.settings',text=u'关闭')
off = ui(packageName='com.android.settings',text=u'开启')


def Gowifi():

    log.info("open settings")
    os.popen("adb -s " + sn + " shell am start com.android.settings/.Settings")
    time.sleep(5)
    wifi = ui(packageName='com.android.settings',text='WLAN')
    if wifi.wait.exists():
        log.info("enter wifi sttings")
        wifi.click()
        time.sleep(2)
    else:
        log.info("can not find wifi item")
        time.sleep(3)
        Gowifi()   
    

def Onw():
        
    if on.wait.exists():
        log.info("try to turn on wifi")
        on.click()
        time.sleep(3)
        if off.wait.exists():
            log.info("turn on wifi sucess")
        if on.wait.exists():
            log.info("error: turn on wifi fail")
            Onw()
    time.sleep(1)


def Conw(ssid,pwd,ip):
    
    log.info("********** test connect wifi")
    log.info("scroll to ssid:%s"%ssid)
    ui(scrollable=True).scroll.to(text=ssid)
    log.info("select ssid:%s"%ssid)
    ui(className='android.widget.TextView',text=ssid,packageName='com.android.settings',resourceId='android:id/title').click()
    time.sleep(2.5)

    p = ui(className='android.widget.EditText',resourceId='com.android.settings:id/password')
    if p.wait.exists(timeout=2000):
        log.info("input password:%s"%pwd)
        dev.inputText(pwd)
        time.sleep(2)
        log.info("select connect %s"%ssid)
        ui(className='android.widget.Button',resourceId='android:id/button1',text=u'连接').click()
        time.sleep(5)

        for i in range(1,61):
        
            b = os.popen("adb -s " + sn + " shell busybox ifconfig wlan0").read()

            if b.find(ip) != -1:

                log.info("%s connect sucess"%ssid)
                break
            else:
                log.info("after connect %s can not find ip,retry."%ssid)
                time.sleep(3)
        
    else:
        log.info("can not find line to input password")
        Gowifi()
        Onw()
        Conw(ssid,pwd,ip)
    
def Ping():

    p = os.popen("adb -s " + sn + " shell ping -c %d www.baidu.com"%count).read()

    if p.find("0% packet loss") != -1:
        log.info("connect ok,ping %d times,lost 0"%count)
    else:
        lost = count - int(p.split("transmitted, ")[1].split(" received")[0])
        log.info("warning: ping lost: %d times"%lost)
        global num
        num = num + lost
    #log.info(p)

         


if __name__ == '__main__':

    #Gowifi()
    #Onw()
    #Conw('Lirun','roobo.8888','192.168.3')
    for i in range(1,test):
        log.info("======================== test ping time: %dmin"%i)
        Ping()
    total = (test-1) * count
    log.info("total test ping  %d times, lost %d times."%(total,num))

            







    
