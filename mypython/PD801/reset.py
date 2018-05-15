# -*- coding: UTF-8 -*-

import os,time,sys
from useriface import device
from useriface import hostpc
from useriface import logger
from datetime import datetime

testtime = 501
SN = '1510000100000022'
dev = device.Device(SN)
pc = hostpc.Host(SN)
ui = dev.uidevice
log = logger.Logger(__file__)
log.addLog2file('PD801_reset_EVT.log')

f = 'resettest.txt'
os.popen("mkdir resetlog")

def Create():
    log.info("remount devcice: %s"%SN)
    os.popen("adb -s " + SN + " remount")
    time.sleep(2)
    for p in ['/cache/','/data/','/sdcard/']:
        os.popen("adb -s " +SN+" shell touch %sresettest.txt"%p)
        ls = os.popen("adb -s " +SN+ " shell ls -l %s%s"%(p,f)).read()
        if ls.find("rw") != -1:
            log.info("create %s%s sucess"%(p,f))
            time.sleep(0.5)
        else:
            Create()

def Reset(str='reset'):
    log.info("open settings...")
    os.popen("adb -s " + SN + " shell am start com.android.settings/.Settings")
    time.sleep(3)

    log.info("swipe to reset page")
    os.popen("adb -s " + SN + " shell input swipe 200 550 200 200")
    time.sleep(2)
    os.popen("adb -s " + SN + " shell input tap 120 620")
    time.sleep(1)

    log.info("select reset in settings")
    time.sleep(2)
    os.popen("adb -s " + SN + " shell input tap 628 144")
    
    if str == 'sd':
        log.info("select format SD card")
        time.sleep(2)
        os.popen("adb -s " + SN + " shell input tap 576 420")
    
    log.info("select reset device")
    time.sleep(2)
    os.popen("adb -s " + SN + " shell input tap 890 742")

    log.info("confirm reset")
    time.sleep(2)
    os.popen("adb -s " + SN + " shell input tap 900 250")
    time.sleep(2)

def Recovery():
    for i in range(201):
        time.sleep(0.5)
        s = os.popen("adb devices").read()
        if '0123456789ABCDEF' and 'recovery' in s:
            log.info("device in recovery mode")
            break
        if i == 200:
            log.info("device not enter recovery mode")
    os.popen("adb -s " +SN +" wait-for-device")
    log.info("find device: %s "%SN)
    time.sleep(60)
        

def Check(str='reset'):
    ct=datetime.now().strftime('%Y%m%d_%H%M%S')
    log.info("pull /cache/recovery/last_log to ./resetlog/%s.log"%ct)
    os.popen("adb -s " + SN + " pull /cache/recovery/last_log ./resetlog/%s.log"%ct)
    for p in ['/cache/','/data/']:
        ls = os.popen("adb -s " +SN+ " shell ls -l %s%s"%(p,f)).read()
        
        if ls.find("rw") == -1:
            log.info("format %s sucess"%p)
        else:
            log.info("format %s fail"%p)

    if str == 'sd':
        ss = os.popen("adb -s " +SN+ " shell ls -l /sdcard/%s"%f).read()
        if ss.find("rw") == -1:
            log.info("format /sdcard/ sucess")
        else:
            log.info("format /sdcard fail")


if __name__ == '__main__':

    for i in range(1,testtime):
        log.info("=============== testtimes: %d ===============" %i)
        Create()

        if i%2 == 1:
            Reset()
            Recovery()
            Check()

        if i%2 == 0:
            Reset('sd')
            Recovery()
            Check('sd')           
