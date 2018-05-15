# -*- encoding: UTF-8 -*-

import os,sys,time
from datetime import datetime

from useriface import device
from useriface import hostpc
from useriface import logger

import multiprocessing

sn = 'testmode'
#sn = '50a99b07'

dev = device.Device(sn)
ui = dev.uidevice
pc = hostpc.Host(sn)
log = logger.Logger(__file__)
log.addLog2file('8909_wifi_ping.log')

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


def Conw():

    pass
    
def Ping():

    p = os.popen("adb -s " + sn + " shell ping -c %d www.baidu.com"%count).read()

    if p.find("0% packet loss") != -1:
        log.info("connect ok,ping %d times,lost 0"%count)
    else:
        log.info("connect error")
        for i in range(1,count + 1):
            if 'icmp_seq=' + str(i) not in p:
                log.info("ping lost: icmp_seq=" + str(i))
    #log.info(p)

         


if __name__ == '__main__':

    #Gowifi()
    #Onw()
    #Conw()
    for i in range(1,1441):
        log.info("======================== test ping time: %dmin"%i)
        Ping()

            







    
