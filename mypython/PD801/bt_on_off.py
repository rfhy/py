# -*- encoding: UTF-8 -*-

import os,sys,time
from datetime import datetime

from useriface import device
from useriface import hostpc
from useriface import logger

sn = '1510000100000038'

dev = device.Device(sn)
ui = dev.uidevice
pc = hostpc.Host(sn)
log = logger.Logger(__file__)
log.addLog2file('PD801_bt_on_off_EVT.log')


on = ui(packageName='com.android.settings',text=u'其他蓝牙设备检测不到此设备',className='android.widget.TextView')
off = ui(packageName='com.android.settings',text=u'开启蓝牙后，您的设备可以与附近的其他蓝牙设备通信。',className='android.widget.TextView')


def gobt():
    ui.wakeup()

    log.info("open settings")
    os.popen("adb -s " + sn + " shell am start com.android.settings/.Settings")
    time.sleep(5)
    bt = ui(packageName='com.android.settings',text=u'蓝牙',className='android.widget.TextView')
    if bt.wait.exists():
        log.info("enter bt sttings")
        bt.click()
        time.sleep(2)
    else:
        log.info("can not find bt item")
        time.sleep(3)
        gobt()   
    

def offbt():   
    if on.wait.exists():
        log.info("try to turn off bt")
        os.popen("adb -s " + sn + " shell input tap 400 220")
        time.sleep(3)
        if off.wait.exists():
            log.info("turn off bt sucess")
        if on.wait.exists():
            log.info("error: turn off bt fail") 
    time.sleep(0.5)
    

def onbt():   
    if off.wait.exists():
        log.info("try to turn on bt")
        os.popen("adb -s " + sn + " shell input tap 400 220")
        time.sleep(5.5)
        if on.wait.exists():
            log.info("turn on bt sucess")
        if off.wait.exists():
            log.info("error: turn on bt fail") 
    time.sleep(0.5)


if __name__ == '__main__':
    gobt()
    if on.wait.exists():
        for i in range(1,2001):
            log.info("================= test turn on and off bt: %d"%i)
            offbt()
            onbt()
        exit()
            
    if off.wait.exists():
        for i in range(1,2001):
            log.info("================= test turn on and off bt: %d"%i)
            onbt()
            offbt()
        exit()
