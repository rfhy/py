# -*- coding: UTF-8 -*-

import os,sys,time
import multiprocessing
import subprocess
import threading
from datetime import datetime
SN='10110000002037C8'

curtime=datetime.now().strftime('%Y%m%d_%H%M%S')

def logs(str):

    curtime1=datetime.now().strftime('%Y%m%d %H:%M:%S')

    lirun=open(curtime + '_ota.log','a+')
    lirun.write(curtime1 + " " + str + "\n")
    lirun.flush()
    lirun.close()
    print(curtime1 + " "  + str)

def connect():

    for i in range(0,5):
        
        time.sleep(3)

        ls1 = os.popen("adb -s " + SN + " shell ls").read()

        if i <= 3:

            if ls1.find("sdcard") != -1:
                
                logs("adb connect sucess")

                break
            
        if i == 4:

            if ls1.find("sdcard") != -1:
                
                logs("adb connect sucess")

                break
            
            else:
                
                logs("connect fail")

    

def reboot():

    logs("reboot device and sleep 23s")

    os.popen("adb -s " + SN + " reboot")

    time.sleep(23)
    
    

def wifi1():

    for i in range(0,6):
    
        logs("connect wifi roobo_test1234")

        os.popen("adb -s " + SN + ''' shell am startservice -a com.roobo.ACTION_CONFIG_WIFI_BY_CMD --es ssid "roobo_test1234" --es pwd "roobo@1234" --es from "ps:47409f9c85c4524d286197360ce78094"''')

        time.sleep(20)
        
        catwifi = os.popen("adb -s " + SN + " shell cat /data/misc/wifi/wpa_supplicant.conf").read()

        if i <= 4:
            if catwifi.find("roobo_test1234") != -1:

                logs("connect wifi sucess")
                break
            
        if i == 5:

            logs("connect wifi fail")

def wifi():

    for i in range(0,6):
    
        logs("svc connect wifi roobo_test1234")

        os.popen("adb -s " + SN + " svc wifi enable")

        time.sleep(5)

        os.popen("adb -s " + SN + " shell svc wifi ssid: roobo_test1234 passwd: roobo@1234")

        time.sleep(15)
        
        catwifi = os.popen("adb -s " + SN + " shell busybox ifconfig").read()

        if i <= 4:
            if catwifi.find("UP BROADCAST RUNNING MULTICAST") != -1:

                logs("connect wifi sucess")
                break
            
        if i == 5:

            logs("connect wifi fail")


def killota(pidnum='com.android.ota'):

    for i in range(0,5):

        pids = os.popen("adb -s " + SN + " shell ps | findstr " + pidnum).read()

        if pids.find(pidnum) != -1:
            a =  pids.split().index(pidnum)
        
            if a != -1:

                str1 = pids.split()[a -7]

                logs(pidnum + " pid is: " + str1)

                logs("kill ota")

                os.popen("adb -s " + SN + " shell kill " + str1)

                break

        else:

            logs("can't find " + pidnum)
            time.sleep(3)


def Remount():

    for items in ['root','remount']:

        for g in range(0,5):

            item1 = {'remount':'succeeded','root':'adbd is already running as root'}

            item2 = {'remount':'remount succeeded','root':'restarting adbd as root'}
    
            remount = os.popen("adb -s " + SN + " " + items).read()

            if remount.find(item1[items]) != -1 or remount.find(item2[items]) != -1:

                logs(items + " succeeded")

                time.sleep(2)

                break
            
            else:

                if g <= retry1:

                    logs(items + " fail, retry : %d" %g)
                    time.sleep(2)    

                else:
                
                    logs(items + " fail")


def mvcore(apk1='CoreServer.apk',apk2='mvcore.ap'):

    for i in range(0,6):

        core = os.popen("adb -s " + SN + " shell ls /system/app/").read()

        if i <= 4:

            if core.find(apk1) != -1:

                os.popen("adb -s " + SN + " shell mv /system/app/"  + apk1 + " /system/app/" + apk2)

                mv = os.popen("adb -s " + SN + " shell ls /system/app/").read()

                if mv.find(apk1) == -1 and mv.find(apk2) != -1:

                    logs("mv " + apk1 + " to " + apk2 + " sucess")

                    break
        if i == 5:

            logs("mv " + apk1 + " to " + apk2 + " fail")


def rewifi1():
    
    for i in range(0,6):
    
        logs("remove wifi conenct")

        os.popen("adb -s " + SN + " shell rm /data/misc/wifi/wpa_supplicant.conf")    

        lswifi = os.popen("adb -s " + SN + " shell ls /data/misc/wifi/").read()

        if i <= 4:
            if lswifi.find("wpa_supplicant.conf") == -1:

                logs("remove wifi sucess")
                break
            
        if i == 5:

            logs("remove wifi fail")

def rewifi():
    
    for i in range(0,6):
    
        logs("svc disable wifi conenct")

        os.popen("adb -s " + SN + " shell svc wifi disable")

        time.sleep(5)

        lswifi = os.popen("adb -s " + SN + " shell busybox ifconfig").read()

        if i <= 4:
            if lswifi.find("wlan0") == -1:

                logs("disable wifi sucess")
                break
            
        if i == 5:

            logs("disable wifi fail")
            time.sleep(2)

def result2(n):

    logfile = open('logcat.txt', 'a+')
    p = subprocess.Popen("adb -s " + SN + " shell logcat -v threadtime &", stdout=subprocess.PIPE)
    logfile.write(p.stdout.readline())
    print "1"
    time.sleep(n)
    print "2"
    logfile.flush()
    print "3"
    p.kill()
    p.wait()
    logfile.close()
    print "4"

def result0(n):

    #logs("start catch log")

    #subprocess.Popen("adb -s " + SN + " shell logcat -f /sdcard/logcat.txt")
    os.popen("adb -s " + SN + " shell logcat -v threadtime > logcat.txt &")
    time.sleep(n)
     

def result1():

    #time.sleep(60)
    print "5"

    logfile = open('logcat.txt','a+')

    res1 = logfile.read()

    pidota = os.popen("adb -s " + SN + " shell ps | findstr com.android.ota").read()

    if res1.find("coreserver start ota") != -1 and pidota.find("com.android.ota") != -1:

        logs("coreserver start ota")

    elif res1.find("boot start ota") != -1 and pidota.find("com.android.ota") != -1:

        logs("boot start ota")

    elif res1.find("act=com.roobo.ota.PULL_UP") != -1 and res1.find("coreserver start ota") == -1 and pidota.find("com.android.ota") != -1:

        logs("watchdog pull up ota")

    elif pidota.find("com.android.ota") == -1:

        logs("can't find ota process")

    else:

        logs("start ota fail ???")

    logfile.close()
    os.popen("del logcat.txt")
    os.popen("adb -s " + SN + " shell logcat -c")


if __name__ == '__main__':
  
    connect()
    
    for i in range(1,10000):

        logs("********** disconnect wifi and reboot devices **********")
        rewifi1()
        reboot()
        connect()
        m1 = multiprocessing.Process(target=result0,args=(60,))
        m1.daemon = True
        m1.start()
        print ('taskkill.exe /pid '+ str(m1.pid) + ' -f')
        os.popen('taskkill.exe /pid '+ str(m1.pid) + ' -f')
        result1()

        logs("********** after power on device , connect wifi **********")
        m1 = multiprocessing.Process(target=result0,args=(60,))
        m1.daemon = True
        m1.start()
        time.sleep(5)      
        wifi1()
        os.popen('taskkill.exe /pid '+ str(m1.pid) + ' -f')
        time.sleep(3)
        result1()

        '''
        logs("********** after connect wifi , kill ota **********")
        m1 = multiprocessing.Process(target=result0)
        m1.start()
        killota()
        result1()

        logs("********** disconnect wifi , remove coreserver and reboot **********")
        rewifi1()
        Remount()
        mvcore('CoreServer.apk','mvcore.ap')
        reboot()
        connect()
        m1 = multiprocessing.Process(target=result0)
        m1.start()
        time.sleep(120)
        result1()

        logs("********** connect wifi , no coreserver **********")
        m1 = multiprocessing.Process(target=result0)
        m1.start()
        wifi()
        result1()

        logs("********** no coreserver and kill ota **********")
        m1 = multiprocessing.Process(target=result0)
        m1.start()
        killota()
        time.sleep(15)
        result1()

        logs("********** reset to default status **********") 
        Remount()
        mvcore('mvcore.ap','CoreServer.apk')
        rewifi1()

        '''
    

    



