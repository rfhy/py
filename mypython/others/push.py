# -*- coding: UTF-8 -*-

import os,sys,time
import multiprocessing
import subprocess
import threading
from datetime import datetime
SN='10110000002037C8'

def connect():

    for i in range(0,5):
        
        time.sleep(3)

        ls1 = os.popen("adb -s " + SN + " shell ls").read()

        if i <= 3:

            if ls1.find("sdcard") != -1:
                
                print("adb connect sucess")

                break
            
        if i == 4:

            if ls1.find("sdcard") != -1:
                
                print("adb connect sucess")

                break
            
            else:
                
                print("connect fail")


def Remount():

    for items in ['root','remount']:

        for g in range(0,5):

            item1 = {'remount':'succeeded','root':'adbd is already running as root'}

            item2 = {'remount':'remount succeeded','root':'restarting adbd as root'}
    
            remount = os.popen("adb -s " + SN + " " + items).read()

            if remount.find(item1[items]) != -1 or remount.find(item2[items]) != -1:

                print(items + " succeeded")

                time.sleep(2)

                break
            
            else:

                if g <= 3:

                    print(items + " fail, retry : %d" %g)
                    time.sleep(2)    

                else:
                
                    print(items + " fail")
                    

def CheckFile(check,path1='/system/app/'):
    
    for m in range(1,5):

        if check == 'libroobo_breakpad.so':
            
            path1 = '/system/lib/'

        print ("rm " + path1 + check)

        os.popen("adb -s " + SN + " shell rm " + path1 + check)

        rmfile = os.popen("adb -s " + SN + " shell ls " + path1).read()

        print ("push " + path1 + check)
       
        os.popen("adb -s " + SN + " push " + os.getcwd() + "\\" + check+ " " + path1)
        
        pushfile = os.popen("adb -s " + SN + " shell ls " + path1).read()
        
        if rmfile.find(check) == -1 and pushfile.find(check) != -1:

            print ("chmod 777 " + path1 + check)
            
            os.popen("adb -s " + SN + " shell chmod 777 " + path1 + check)

            break
        
        else:

            print ("push fail " + path1 + check)



def PushFile(check,path1='/system/etc/firmware/mcu_version.cfg'):
    


        print ("push " + path1)
       
        os.popen("adb -s " + SN + " push " + os.getcwd() + "\\" + check+ " " + path1)
        
        pushfile = os.popen("adb -s " + SN + " shell cat " + path1).read()
        
        if pushfile.find("65") != -1:

            print ("push pass ")


def reboot():

    print("reboot device")

    os.popen("adb -s " + SN + " reboot")

if __name__ == '__main__':

    connect()
    Remount()
    CheckFile('libroobo_breakpad.so')
    CheckFile('CoreServer.apk')
    CheckFile('OtaUpgrade.apk')
    #PushFile('mcu_version.cfg')
    PushFile('mcu_version_68.cfg')
    #os.popen("adb -s " + SN + " shell svc wifi ssid: roobo_test1234 passwd: roobo@1234")
    time.sleep(10)
    reboot()



