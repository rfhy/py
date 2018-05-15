# -*- coding: UTF-8 -*-

import os,sys,time
import multiprocessing
import subprocess
import threading
import sqlite3
from datetime import datetime
SN='1011010000200E1B'
#SN='10110000002037C8'
allsize = 289382033
defalut_md5 = 'FDFF8E3F25ACDFC47F55E22627F969D0'

#curtime=datetime.now().strftime('%Y%m%d_%H%M%S')


def logs(str):

    curtime1=datetime.now().strftime('%Y%m%d %H:%M:%S')

    #lirun=open(curtime + '_ota_crash_check.log','a+')
    lirun=open('all_ota_crash_check.log','a+')
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

    logs("reboot device and sleep 20s")

    os.popen("adb -s " + SN + " reboot")

    time.sleep(20)
    
    

def wifi1():

    for i in range(0,6):
        
        catwifi1 = os.popen("adb -s " + SN + " shell busybox ifconfig").read()

        if catwifi1.find("UP BROADCAST RUNNING MULTICAST") != -1:

            logs("already connect wifi")
            break

        else:
            
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
                


def wifi():

    for i in range(0,6):
        
        catwifi4 = os.popen("adb -s " + SN + " shell busybox ifconfig").read()

        if catwifi4.find("UP BROADCAST RUNNING MULTICAST") != -1:

            logs("already connect wifi")
            break

        else:
            
            enwifi()

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
            


def ResultCheck():

    resultsrom = os.popen("adb -s " + SN + " shell cat /cache/recovery/last_log_r").read()

    if resultsrom.find("fw_upgrade: status = 0") != -1:
        
        logs("rom update success\n")
        
    else:
        
        logs("rom update fail\n")



def power():
    
    #os.path.exists('settings.db')
    for i in range(0,11):

        if os.path.isfile('settings.db') == True:
            logs("delete settings.db")

            os.popen("del settings.db")

        if os.path.isfile('settings.db') == False:

            logs("push settings.db")
        
            os.popen("adb -s " + SN + " pull /data/data/com.android.providers.settings/databases/settings.db")
    
            if os.path.isfile('settings.db') == True:
                logs("push settings.db sucess")
                conn = sqlite3.connect('settings.db')
                c = conn.cursor()
                a = c.execute("select * from system where name='mcu_info'")
                b = a.fetchall()
                if b != []:
                    d = b[0][2]
                    logs("battery info is: " + d)
                    
                else:
                    d = ''
                    logs("can not find battery info in settings.db")
    
                c.close()
                conn.close()
                return d
                break
            
        if i == 10:

            logs("check battery status fail")
            


def Checksize():
    connect()
    wifi1()
    time.sleep(30)

    b = 1

    logs("=================== testtimes : %d ===================" %b)

    for i in range(0,100000):
        time.sleep(3)

        ls1 = os.popen("adb -s " + SN + " shell ls -l /sdcard/Download/").read()

        if ls1.find("update-") != -1:

            sz = int(ls1.split()[3])

            if 100000000 > sz > 0:

                logs("download size: " + ls1.split()[3] + " , total size: " + str(allsize))
                
                reboot()
                connect()
                time.sleep(30)
                wifi1()

                time.sleep(25)
                

            if 200000000 > sz >= 100000000:

                logs("download size: " + ls1.split()[3] + " , total size: " + str(allsize))

                rewifi1()

                time.sleep(3)

                rewifi()

                time.sleep(3)

                enwifi()

                time.sleep(20)

                wifi1()

                time.sleep(30)

            if allsize > sz >= 200000000:

                logs("download size: " + ls1.split()[3] + " , total size: " + str(allsize))

                time.sleep(2)

            if sz == allsize:

                logs("download size: " + ls1.split()[3] + " , total size: " + str(allsize))
                time.sleep(1.5)

                md5 = os.popen("adb -s " + SN + " shell busybox md5sum /sdcard/Download/*").read()

                logs(md5.strip('\r\n'))

                ls7 = os.popen("adb -s " + SN + " shell ls -l /sdcard/Download/").read()

                power()

                if ls7.find("update-") != -1:               

                    download_md5 = md5.split()[0]

                else:

                    download_md5 = 'none'

                logs("default md5 is: " + defalut_md5 + " , download file md5 is: " + download_md5)

                time.sleep(90)
                
                chde = os.popen("adb devices").read()

                if chde.find(SN) != -1:              

                    logs("device not upgrade...")
                    
                    if defalut_md5 != download_md5 or defalut_md5 != download_md5.upper():

                        logs("md5 is fail")

                    ls2 = os.popen("adb -s " + SN + " shell ls -l /sdcard/Download/").read()                  

                    if ls2.find(str(allsize)) == -1:

                        logs("download file is delete\n")
                        
                    else:
                        if d != '':
                            if int(d.split('&')[2].split('=')[1]) < 50 and d.split('&')[3].split('=')[1] != 'POWER_VBus':
                                logs("battery is low\n")
                        else:
                            logs("no battery info\n")

                    reboot()
                    connect()
                    
                    b += 1

                    logs("=================== testtimes : %d ===================" %b)

                    time.sleep(30)
                    wifi1()

                    time.sleep(30)

                if chde.find('0123456789ABCDEF') != -1 and chde.find('recovery') != -1:

                    logs("device is upgrading...")

                    connect()

                    ResultCheck()

                    b += 1

                    logs("=================== testtimes : %d ===================" %b)
                    time.sleep(30)
                    wifi1()

        if ls1.find("update-") == -1:
    
            logs("not start download")

            time.sleep(5)



def watchrwifi():

    for i in range(0,100000):

        #connect()
        os.popen("adb -s " + SN + " wait-for-device")
        time.sleep(5)
        s1 = os.popen("adb -s " + SN + " shell getprop ro.runtime.firstboot").read()
        pings = os.popen("adb -s " + SN + " shell ping -c 5 www.baidu.com").read()

        if pings.find("0% packet loss") == -1:

            os.popen("adb -s " + SN + " wait-for-device")
            time.sleep(5)
            s2 = os.popen("adb -s " + SN + " shell getprop ro.runtime.firstboot").read()

            if s1 == s2:
            #if int(s2) - int(s1) < 15000000:
            #2分钟内下载小于15M，重启    
                logs("network is bad reboot device")
                os.popen("adb -s " + SN + " shell reboot")
                connect()
                time.sleep(20)
                wifi1()

        time.sleep(120)


def watchrdl():

    for i in range(0,100000):

        #connect()
        os.popen("adb -s " + SN + " wait-for-device")
        time.sleep(5)

        s3 = os.popen("adb -s " + SN + " shell getprop ro.runtime.firstboot").read()

        dl = os.popen("adb -s " + SN + " shell ls -l /sdcard/Download/").read()
        #t1 = time.time()

        if dl.find("update-") != -1:

            s1 = int(dl.split()[3])
            time.sleep(120)
            os.popen("adb -s " + SN + " wait-for-device")
            time.sleep(5)
            ddd = os.popen("adb -s " + SN + " shell ls -l /sdcard/Download/").read()
            if ddd.find("update-") != -1:

                s2 = int(ddd.split()[3])
                if s1 == s2:
                    logs("download size not change more than 120s")
                    reboot()
                    connect()
                    time.sleep(20)
                    wifi1()
                    
        if dl.find("update-") == -1:
       
            time.sleep(120)
            os.popen("adb -s " + SN + " wait-for-device")
            time.sleep(5)
            s4 = os.popen("adb -s " + SN + " shell getprop ro.runtime.firstboot").read()
            
            dd = os.popen("adb -s " + SN + " shell ls -l /sdcard/Download/").read()
            if dd.find("update-") == -1 and s3 == s4:
                #t2 = time.time()
                #t3 = t2 - t1
                logs("not start download more than 120s")
                #print("**************  %d *****************"%t3)
                #print("s3: " + s3 + "s4: " + s4)
                #print("ddd: " + ddd)
                #print("dl: " + dl)
                reboot()
                connect()
                time.sleep(20)
                wifi1()
                   

if __name__ == '__main__':

    #m1 = multiprocessing.Process(target=watchrwifi)
    m1 = multiprocessing.Process(target=watchrdl)
    m1.start()

    Checksize()


    
