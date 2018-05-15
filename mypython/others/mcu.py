# -*- coding: UTF-8 -*-

import os,sys,time
import multiprocessing
import subprocess
import threading
from datetime import datetime
SN='192.168.10.104:6666'

curtime=datetime.now().strftime('%Y%m%d_%H%M%S')

def logs(str):

    curtime1=datetime.now().strftime('%Y%m%d %H:%M:%S')

    lirun=open(curtime + '_boot.log','a+')
    lirun.write(curtime1 + " " + str + "\n")
    lirun.flush()
    lirun.close()
    print(curtime1 + " "  + str)
    

def check():   

    for i in range(0,5):

        ls = os.popen("adb -s " + SN + " shell getprop | findstr mcu").read().strip()

        logs(ls)
        
        if ls.find("[sys.mcu.boot]: [1]") != -1:         

            logs("mcu in boot mode")
            
            break
        
        elif ls.find("[sys.mcu.coord.version]:") != -1:

            logs("mcu in app mode")
            
            break
        
        else:

            logs("Fail to communicate with MCU!")
            
            break           
        

def connect():

    for i in range(0,5):

        os.popen("adb connect " + SN)
        time.sleep(0.5)
        os.popen("adb connect " + SN)

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
                
                logs("adb connect fail,so can't get mcu mode after send 0x70 and reboot in this test times")
                logs("reason: before connect adb , device do mcu update?")
                break
            
    

def boot():

    logs("send 0x70 and reboot device")

    os.popen("adb -s " + SN + ''' shell "echo -e '\\x5a\\x00\\x00\\x01\\x02\\x03\\x04\\x05\\x06\\x07\\x70\\x00\\x70\\xa5' > /dev/skel0"''').read()
    time.sleep(1)

    subprocess.Popen("adb -s " + SN + " reboot")
    time.sleep(1)


def disconnect(n):
    
    logs("disconnect wifi adb and sleep %ds"%n)

    #subprocess.Popen("adb disconnect")
    os.popen("adb disconnect " + SN)
    time.sleep(n)

    

if __name__ == '__main__':

    disconnect(3)

    for i in range(1,100000):

        logs("================ testtimes: %d ==============\n"%i)

        connect()
        check()
    
        boot()
        disconnect(15)
        
        connect()
        check()
        disconnect(180)
        
        
        
