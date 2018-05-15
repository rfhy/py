# -*- coding: UTF-8 -*-

import os,sys,time
import multiprocessing
import subprocess
import threading
from datetime import datetime
SN='1011010000200E1B'
#SN='10110000002037C8'
allsize = 289382033
defalut_md5 = 'FDFF8E3F25ACDFC47F55E22627F969D0'

curtime=datetime.now().strftime('%Y%m%d_%H%M%S')


def logs(str):

    curtime1=datetime.now().strftime('%Y%m%d %H:%M:%S')

    lirun=open(curtime + '_ota_crash_check.log','a+')
    lirun.write(curtime1 + " " + str + "\n")
    lirun.flush()
    lirun.close()
    print(curtime1 + " "  + str)
    

def connect():

    os.popen("adb -s " + SN + " wait-for-device")

    for i in range(0,6):

        ls1 = os.popen("adb -s " + SN + " shell ls").read()

        if i <= 4:

            if ls1.find("sdcard") != -1:
                
                logs("adb connect sucess")

                break
            
        if i == 5:

            logs("connect fail")
            


def reboot():

    logs("reboot device and sleep 5s")

    os.popen("adb -s " + SN + " reboot")

    time.sleep(5)
    
    
def Remount():

    for items in ['root','remount']:

        for g in range(0,6):

            item1 = {'remount':'succeeded','root':'adbd is already running as root'}

            item2 = {'remount':'remount succeeded','root':'restarting adbd as root'}
    
            remount = os.popen("adb -s " + SN + " " + items).read()

            if remount.find(item1[items]) != -1 or remount.find(item2[items]) != -1:

                logs(items + " succeeded")

                time.sleep(2)

                break
            
            else:

                if g <= 4:

                    logs(items + " fail")
                    time.sleep(2)    

                else:
                
                    logs(items + " fail, exit!")
                    exit()

    
def removeota():

    for l in range(0,6):
        
        os.popen("adb -s " + SN + " shell rm /system/app/OtaUpgrade.apk")
       
        xml = os.popen("adb -s " + SN + " shell ls /system/app/").read()

        if xml.find("OtaUpgrade.apk") == -1:
            logs("remove OtaUpgrade.apk ok")
            break
        else:
            if l <= 4:
                logs("remove OtaUpgrade.apk fail")
                time.sleep(2)
            else:
                log.info("remove OtaUpgrade.apk fail, exit!")
                exit()

def Pushota():

    for l in range(0,6):
        
        os.popen("adb -s " + SN + " push OtaUpgrade11.apk /system/app/OtaUpgrade.apk")
       
        xml = os.popen("adb -s " + SN + " shell ls /system/app/").read()

        if xml.find("OtaUpgrade.apk") != -1:
            logs("push OtaUpgrade.apk ok")
            break
        else:
            if l <= 4:
                logs("push OtaUpgrade.apk fail")
                time.sleep(2)
            else:
                logs("push OtaUpgrade.apk fail, exit!")
                exit()
                
def Chmodota():

    for l in range(0,6):

        logs("chmod 777 /system/app/OtaUpgrade.apk")
        os.popen("adb -s " + SN + " shell chmod 777 /system/app/OtaUpgrade.apk")
        time.sleep(3)
        ch7 = os.popen("adb -s " + SN + " shell ls -l /system/app/OtaUpgrade.apk").read()
        if l <= 4:
            if ch7.find('rwxrwxrwx') != -1:
                logs("chmod sucess")
                break
        else:
            logs("chmod fail, exit!")
            exit()
    

if __name__ == '__main__':

    connect()

    Remount()

    removeota()

    Pushota()

    Chmodota()

    reboot()


    
