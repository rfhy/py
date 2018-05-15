#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os,time
from datetime import datetime

SN = '4000105800000011'
path='/data/'
command = '--update_package='
path1='/cache/recovery/command'
path2 = '/sdcard/rom_ota_log'


def logs(str):
    curtime=datetime.now().strftime('%Y%m%d %H:%M:%S')
    lirun=open('PD801_ota_self.log','a+')
    if str == '\n':
        lirun.write("\n")
        print("\n")
    else:
        lirun.write(curtime + " " + str + "\n")
        print(curtime + " "  + str)
    lirun.flush()
    lirun.close()
    

def Remount():
    for items in ['root','remount']:
        for g in range(1,12):
            item1 = {'remount':'succeeded','root':'adbd is already running as root'}
            item2 = {'remount':'remount succeeded','root':'restarting adbd as root'}
            remount = os.popen("adb -s " + SN + " " + items).read()
            if remount.find(item1[items]) != -1 or remount.find(item2[items]) != -1:
                logs(items + " succeeded")
                time.sleep(1)
                break
            else:
                if g <= 10:
                    logs(items + " fail, retry : %d" %g)
                    time.sleep(2)    
                else:                
                    logs(items + " fail")

def Connect(check,md5):
    logs("wait for device")
    os.popen("adb -s " + SN + " wait-for-device")
    logs("find device: " + SN)

    for i in range(1,12):
        logs("push " + check + " to " + path + check)
        os.popen("adb -s " + SN + " push " + check + " " + path + check)
        time.sleep(1)
        adbls = os.popen("adb -s " + SN + " shell ls -l " + path + check).read()
        if adbls.find("root") != -1:
            logs("find rom ota file: " + path + check)
            m5 = os.popen("adb -s " + SN + " shell busybox md5sum " + path + check).read() 
            if m5.find(md5.upper()) != -1 or m5.find(md5.lower()) != -1:
                logs("rom ota file md5 is ok")
                break
            else:
                s = m5.split()[0]
                logs("rom ota file md5 is wrong: " + s)         
        else:
            if i <= 10:
                logs("can not find rom ota file, retry : %d" %i)
                time.sleep(3)
            else:
                logs("can not find rom ota file, exit")
                exit()


def SendCommand(check):
    for i in range(1,12):
        ls = os.popen("adb -s " + SN + " shell ls -l /cache/").read()
        if ls.find("recovery") == -1:
            logs("create floder /cache/recovery/")
            os.popen("adb -s " +SN+ " shell mkdir /cache/recovery")
            time.sleep(1)
        else:
            os.popen("adb -s " + SN + " shell \"echo " + command + path + check +" > " + path1 + "\"")
            logs("echo " + command + path + check + " > " + path1)
            time.sleep(1)
            checkcommand = os.popen("adb -s " + SN + " shell cat " + path1).read()
            if checkcommand.split("\r\n")[0] == command + path + check:
                logs("rom update command send ok")
                break
            else:
                if i <= 10:
                    logs("rom update command send fail: %d" %i)
                    time.sleep(3)       
                else:
                    logs("rom update command send fail, exit!")
                    exit()
        time.sleep(1)
         

def Recovery():
    logs("reboot device to recovery")
    os.popen("adb -s "  + SN + " shell reboot recovery")
    logs("wait ota update ...")
    time.sleep(12)


def VersionROM(str):
    versionrom = os.popen("adb -s " + SN + " shell getprop ro.roobo.version.release").read()
    logs(str + " update , rom version is: " + versionrom.split('\r\n')[0])


def Result():
    os.popen("adb -s " + SN + " wait-for-device")
    logs("find device: " + SN)
    time.sleep(75)
    curtime = datetime.now().strftime('%Y%m%d_%H%M%S')
    os.popen("adb -s " + SN + " shell mkdir " + path2)
    resultsrom = os.popen("adb -s " + SN + " shell cat /cache/recovery/last_log").read()
    os.popen("adb -s " + SN + " shell cp /cache/recovery/last_log " + path2 + "/" + "%s.log" %curtime)
    logs("cp /cache/recovery/last_log TO " + path2 + "/%s.log" %curtime) 
    if resultsrom.find("script succeeded:") != -1:
        logs("rom update success")
    if resultsrom.find("Installation aborted.") != -1:
        logs("rom update fail")


def ROM(name,md5):
    Connect(name,md5)
    VersionROM("before")  
    SendCommand(name)
    Recovery()
    Result()
    VersionROM('after')
    logs("\n")

         
if __name__ == '__main__':

    for i in range(1,200):
        logs("======================= testtimes: " + str(i) + " =======================")                   
        #ROM('update-diff.zip','627FB820114C5CAF8DE6DC7BFDFD0CFA')
        ROM('update-eng.zip','47953A66BC2EA7CC2D0425890132B7BA')
        time.sleep(5)
          
