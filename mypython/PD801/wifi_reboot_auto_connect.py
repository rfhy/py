# -*- encoding: UTF-8 -*-

import os,sys,time
from datetime import datetime

from useriface import device
from useriface import hostpc
from useriface import logger

import multiprocessing

sn = '4000105800000013'

dev = device.Device(sn)
ui = dev.uidevice
pc = hostpc.Host(sn)
log = logger.Logger(__file__)
log.addLog2file('PD801_reboot and auto connect_EVT.log')


on = ui(packageName='com.android.settings',text=u'关闭',className='android.widget.Switch')
off = ui(packageName='com.android.settings',text=u'开启',className='android.widget.Switch')


def Gowifi():

    ui.wakeup()

    log.info("open settings")
    os.popen("adb -s " + sn + " shell am start com.android.settings/.Settings")
    time.sleep(5)
    wifi = ui(packageName='com.android.settings',text='WLAN',className='android.widget.TextView')
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


def Conf(ssid,ip):

    log.info("scroll to ssid:%s"%ssid)
    ui(scrollable=True).scroll.toBeginning()
    log.info("select ssid:%s"%ssid)
    ui(className='android.widget.TextView',text=ssid,packageName='com.android.settings',resourceId='android:id/title').click()
    time.sleep(2.5)

    p = ui(className='android.widget.Button',resourceId='android:id/button1',text=u'连接')
    if p.wait.exists(timeout=2000):
        log.info("select connect ssid:%s"%ssid)
        p.click()

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
        log.info("can not find item to connect wifi")
        Gowifi()
        Onw()
        Conf(ssid,ip)
    
    
def Delw(ssid,ip):
    log.info("********** test forget wifi")
    log.info("scroll to ssid:%s"%ssid)
    ui(scrollable=True).scroll.toBeginning()
    log.info("select ssid:%s"%ssid)
    ui(className='android.widget.TextView',text=ssid,packageName='com.android.settings',resourceId='android:id/title').click()
    time.sleep(2)

    p = ui(className='android.widget.Button',resourceId='android:id/button3',text=u'取消保存')
    if p.wait.exists(timeout=2000):
        log.info("select forget ssid:%s"%ssid)
        p.click()
        time.sleep(3)
        for i in range(1,21):        
            b = os.popen("adb -s " + sn + " shell busybox ifconfig wlan0").read()

            if b.find(ip) == -1:

                log.info("%s del sucess"%ssid)
                break
            else:
                log.info("%s del fail,retry."%ssid)
                time.sleep(3)
        
    else:
        log.info("can not find item to forget wifi")
        Gowifi()
        Onw()
        Delw(ssid,ip)

def Ping(ssid,ip):
    for i in range(1,61):
        b = os.popen("adb -s " + sn + " shell busybox ifconfig wlan0").read()
        if b.find(ip) != -1:
            log.info("%s auto connect sucess"%ssid)
            time.sleep(2.5)
            p = os.popen("adb -s " + sn + " shell ping -c 2 www.baidu.com").read()
            if p.find("0% packet loss") != -1:
                log.info("after reboot,auto connect ping is ok")
                break
            else:
                log.info("after reboot,auto connect ping is error,retry")
                time.sleep(3)
        else:
            log.info("after reboot auto connect fail,retry.")
            time.sleep(3)



def reboot():
    log.info("reboot device: " +sn)
    os.popen("adb -s " + sn + " reboot")
    os.popen("adb -s " + sn + " wait-for-device")
    time.sleep(18)
         

if __name__ == '__main__':
    
    Gowifi()
    Onw()
    Conw('Lirun','roobo.8888','192.168.3')

    for i in range(1,2001):
        log.info("============== test reboot and auto connect wifi time: %d"%i)
        reboot()
        Ping('Lirun','192.168.3')
    log.info("============== test reboot and auto connect wifi finsh\n")
    
