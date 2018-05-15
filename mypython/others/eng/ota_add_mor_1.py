# -*- coding: UTF-8 -*-

import os,sys,time
import multiprocessing
import subprocess
import threading
from datetime import datetime
SN='10110000002037C8'   

#curtime=datetime.now().strftime('%Y%m%d_%H%M%S')

def logs(str):

    curtime1=datetime.now().strftime('%Y%m%d %H:%M:%S')

    #lirun=open(curtime + '_ota.log','a+')
    lirun=open('D034C00_eng_ota.log','a+')
    lirun.write(curtime1 + " " + str + "\n")
    lirun.flush()
    lirun.close()
    print(curtime1 + " "  + str)


def waring():

    player = r'"C:\Program Files (x86)\Windows Media Player\wmplayer.exe"'

    music = r"D:\Roobo\Project\dingdong.wav"

    os.popen(player + " " + music)

def watchplayer(name='wmplayer.exe'):

    for i in range(0,10000000):

        kills = os.popen("tasklist | findstr " + name).read()
        if kills.find(name) != -1:
            time.sleep(5)
            pid_player = kills.split()[1]
            print("wmplayer pid is: " + pid_player)
            os.popen("taskkill /PID " + pid_player + " -f")
            time.sleep(2)
            check = os.popen("tasklist | findstr " + name).read()
            if check.find(name) == -1:
                print("kill " + name + " sucess.")
        time.sleep(30)


def connect():

    for i in range(0,5):

        os.popen("adb -s " + SN + " wait-for-device")
        
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

    logs("reboot device and sleep 20s")

    os.popen("adb -s " + SN + " reboot")

    time.sleep(20)
    
    

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

def enwifi():

    for i in range(0,11):

        time.sleep(3)
     
        catwifi3 = os.popen("adb -s " + SN + " shell busybox ifconfig").read()

        if catwifi3.find("wlan0") != -1:

            logs("already enable wifi")
            break

        else:
                
            if i <= 9:

                os.popen("adb -s " + SN + " svc wifi enable")

                time.sleep(5)
                    
                catwifi4 = os.popen("adb -s " + SN + " shell busybox ifconfig").read()

                if catwifi4.find("wlan0") != -1:

                    logs("enable wifi sucess")
                    break
                
            else:

                logs("enable wifi fail")


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

                if g <= 3:

                    logs(items + " fail, retry : %d" %g)
                    time.sleep(2)    

                else:
                
                    logs(items + " fail")


def mvcore(apk1='CoreServer.apk',apk2='mvcore.ap'):

    for i in range(0,6):

        core = os.popen("adb -s " + SN + " shell ls /system/app/").read()

        if core.find(apk1) != -1:

            if i <= 4:

                os.popen("adb -s " + SN + " shell mv /system/app/"  + apk1 + " /system/app/" + apk2)

                mv = os.popen("adb -s " + SN + " shell ls /system/app/").read()

                if mv.find(apk1) == -1 and mv.find(apk2) != -1:

                    logs("mv " + apk1 + " to " + apk2 + " sucess")

                    break
            if i == 5:

                logs("mv " + apk1 + " to " + apk2 + " fail")

        else:
            if core.find(apk2) != -1:

                logs("no " + apk1 + " and already have " + apk2)
                break
                

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

        time.sleep(3)

        lswifi = os.popen("adb -s " + SN + " shell busybox ifconfig").read()

        if i <= 4:
            if lswifi.find("wlan0") == -1:

                logs("disable wifi sucess")
                break
            
        if i == 5:

            logs("disable wifi fail")
            time.sleep(2)


def result0():

    os.popen("adb -s " + SN + " shell rm /sdcard/logcat.txt")
    os.popen("adb -s " + SN + " shell logcat -c")

    #subprocess.Popen("adb -s " + SN + " shell logcat -f /sdcard/logcat.txt &")
    os.popen("adb -s " + SN + " shell logcat -v threadtime -f /sdcard/logcat.txt")
     


def result1():

    time.sleep(75)

    res1 = os.popen("adb -s " + SN + " shell cat /sdcard/logcat.txt").read()

    pidota = os.popen("adb -s " + SN + " shell ps | findstr com.android.ota").read()


    if res1.find("RegWatchDog") != -1:

        logs("++++ RegWatchDog +++++")


    if res1.find("CatchExcep | ota caughtException die restart 10 seconds later") != -1:

        logs("ota application crash , restart")

       
    if res1.find("Start proc com.android.ota for service com.android.ota/.PullUpService") != -1:

        logs("Start proc com.android.ota for service com.android.ota/.PullUpService")


    if res1.find("PullUpService started") != -1:

        logs("PullUpService started")
        

    if res1.find("Start proc com.android.ota for broadcast com.android.ota/.udisk.UDiskReceiver") != -1:
            
        logs("Start proc com.android.ota for broadcast com.android.ota/.udisk.UDiskReceiver")
            

    if pidota.find("com.android.ota") != -1:

        logs("find ota process")

        if res1.find("coreserver start ota") != -1:

            logs("coreserver start ota")

            return "coreserver"

        if res1.find("boot start ota") != -1:

            logs("boot start ota")
            
            return "boot"

        #if res1.find("Start proc com.android.ota for service com.android.ota/.PullUpService") != -1 and res1.find("start ota") == -1:

            #logs("Start proc com.android.ota for service com.android.ota/.PullUpService")

                #return "watchdog"

        if res1.find("PullUpService started") != -1 and res1.find("start ota") == -1:

            logs("PullUpService started")

            return "watchdog"

        if res1.find("Start proc com.android.ota for broadcast com.android.ota/.udisk.UDiskReceiver") != -1 and res1.find("start ota") == -1 and res1.find("PullUpService started") == -1:
            
            logs("Start proc com.android.ota for broadcast com.android.ota/.udisk.UDiskReceiver")
            
            return "broadcast"
    

        if res1.find("start ota") == -1 and res1.find("Start proc com.android.ota for:") == -1 and res1.find("CatchExcep | ota caughtException die restart 10 seconds later") == -1:

            logs("can't find which process start ota in log")

            return "no"
            
    if pidota.find("com.android.ota") == -1:

        logs("can't find ota process")

        return "none"



def result4(str):

    curtime3=datetime.now().strftime('%Y%m%d_%H%M%S')

    if result1() == str:

        logs("pass\n")
        
    else:
        
        logs("fail")
        logs("mv /sdcard/logcat.txt to /sdcard/" + curtime3 + "_logcat.txt\n")        
        os.popen("adb -s " + SN + " shell mv /sdcard/logcat.txt /sdcard/" + curtime3 + "_logcat.txt")
        #waring()
        

if __name__ == '__main__':

    connect()      
    #m8 = multiprocessing.Process(target=watchplayer,args=('wmplayer.exe',))
    #m8.start()

    for i in range(1,10000):

        logs("====================== testtimes: %d ====================\n"%i)
        
        logs("********** reset to default status **********")        
        connect()      
        Remount()
        mvcore('mvcore.ap','CoreServer.apk')
        mvcore('bot.ap','Boot.apk')
        rewifi1()
        
        
        logs("********** reboot without wifi **********")       
        reboot()
        connect()
        m1 = multiprocessing.Process(target=result0)
        m1.start()
        result4('coreserver')


        logs("********** no wifi , kill ota **********")
        m1 = multiprocessing.Process(target=result0)
        m1.start()
        killota()
        result4('watchdog')
        

        logs("********** connect wifi **********")
        m1 = multiprocessing.Process(target=result0)
        m1.start()
        time.sleep(8)
        wifi1()
        time.sleep(12)
        result4('no')

        logs("********** after connect wifi , kill ota **********")
        m1 = multiprocessing.Process(target=result0)
        m1.start()
        killota()
        result4('watchdog')
        

        logs("********** reboot with wifi connected **********")
        reboot()
        connect()
        m1 = multiprocessing.Process(target=result0)
        m1.start()
        result4('coreserver')

        '''
        logs("********** after connect wifi , kill ota **********")
        m1 = multiprocessing.Process(target=result0)
        m1.start()
        killota()
        result4('watchdog')
        

        logs("********** disconnect wifi **********")
        m1 = multiprocessing.Process(target=result0)
        m1.start()
        time.sleep(8)
        rewifi1()
        rewifi()
        enwifi()
        time.sleep(12)
        result4('no')

        
        logs("********** disconnect wifi , remove coreserver and reboot **********")
        rewifi1()
        Remount()
        mvcore('CoreServer.apk','mvcore.ap')
        reboot()
        connect()
        m1 = multiprocessing.Process(target=result0)
        m1.start()
        time.sleep(135)
        result4('boot')

        logs("********** no wifi , no coreserver and kill ota **********")
        m1 = multiprocessing.Process(target=result0)
        m1.start()
        killota()
        time.sleep(15)
        result4('boot')

        logs("********** connect wifi , no coreserver **********")
        m1 = multiprocessing.Process(target=result0)
        m1.start()
        wifi()
        result4('boot')

        logs("********** no coreserver and kill ota **********")
        m1 = multiprocessing.Process(target=result0)
        m1.start()
        killota()
        time.sleep(15)
        result4('boot')

        logs("********** disconnect wifi , remove coreserver and boot and reboot **********")
        rewifi1()
        Remount()
        mvcore('Boot.apk','bot.ap')
        reboot()
        connect()
        m1 = multiprocessing.Process(target=result0)
        m1.start()
        time.sleep(15)
        result4('broadcast')
        
        logs("********** connect wifi , no coreserver and boot **********")
        m1 = multiprocessing.Process(target=result0)
        m1.start()
        wifi()
        result4('no')

        logs("********** connect wifi , no coreserver and boot , kill ota **********")
        m1 = multiprocessing.Process(target=result0)
        m1.start()
        killota()
        result4('none')
        '''
    



