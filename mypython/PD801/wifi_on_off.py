# -*- encoding: UTF-8 -*-

import os,sys,time
from datetime import datetime

from useriface import device
from useriface import hostpc
from useriface import logger

import multiprocessing

sn = '1510000100000022'
ip = '192.168.1'

dev = device.Device(sn)
ui = dev.uidevice
pc = hostpc.Host(sn)
log = logger.Logger(__file__)
log.addLog2file('PD801_wifi_on_off_EVT.log')


on = ui(packageName='com.android.settings',text=u'关闭',className='android.widget.Switch')
off = ui(packageName='com.android.settings',text=u'开启',className='android.widget.Switch')


def Gowifi():

    ui.wakeup()

    log.info("open settings")
    os.popen("adb -s " + sn + " shell am start com.android.settings/.Settings")
    time.sleep(5)
    ui(scrollable=True).scroll.toBeginning()
    time.sleep(2)
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
        time.sleep(5)
        if off.wait.exists():
            log.info("turn on wifi sucess")
            time.sleep(5)
            for i in range(0,101):
                s = os.popen("adb -s " + sn + " shell busybox ifconfig wlan0").read()
                if s.find(ip) != -1:
                    log.info("wifi auto connect sucess\n")
                    break
                else:
                    t = i + 1
                    log.info("wifi auto connect fail,retry: %d"%t)
                    time.sleep(3)
    time.sleep(1)
    

def Offw():
        
    if off.wait.exists():
        log.info("try to turn off wifi")
        off.click()
        time.sleep(3)
        
        if on.wait.exists():
            log.info("turn off wifi sucess")
        #if off.wait.exists():
            #log.info("error: turn on wifi fail")
            
    time.sleep(1)

    

def watchrcrash():

    for i in range(0,604800):
        anr = ui(text='ANR')
        crash = ui(text=u'崩溃')

        if crash.wait.exists(timeout=1000):
            log.info("-------------- crash happend! fail! save screencap to /sdcard/" + str(i) + ".png")
            os.popen("adb -s " + sn + " shell screencap -p /sdcard/" + str(i) + ".png")
            ui(text=u'确定').click()
        if anr.wait.exists(timeout=1000):
            log.info("-------------- anr happend! fail! save screencap to /sdcard/" + str(i) + ".png")
            os.popen("adb -s " + sn + " shell screencap -p /sdcard/" + str(i) + ".png")
            ui(text=u'确定').click()
        if i % 3600 == 0:
            t = i / 3600
            log.info("watch run %d h"%t)




def Conw(ssid,pwd,ip):
    
    log.info("********** test connect wifi")
    log.info("scroll to ssid:%s"%ssid)
    ui(scrollable=True).scroll.to(text=ssid)
    log.info("select ssid:%s"%ssid)
    ui(className='android.widget.TextView',text=ssid,packageName='com.android.settings',resourceId='android:id/title').click()
    time.sleep(3)

    p = ui(className='android.widget.EditText',resourceId='com.android.settings:id/password')
    if p.wait.exists(timeout=2000):
        log.info("input password:%s"%pwd)
        dev.inputText(pwd)
        time.sleep(2)
        log.info("select connect %s"%ssid)
        ui(className='android.widget.Button',resourceId='android:id/button1',text=u'连接').click()
        time.sleep(10)

        for i in range(1,101):
        
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
            


if __name__ == '__main__':

    Gowifi()
    Onw()
    #Conw('PD801','roobo.2018',ip)

    for i in range(1,3001):
        log.info("================= test turn on and off wifi: %d"%i)
        Offw()
        Onw()
    log.info("=================trun on/off wifi test finish.\n")
            







    
