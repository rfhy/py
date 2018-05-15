# -*- coding: UTF-8 -*-

import os,sys,time
import multiprocessing
import subprocess
import threading
from datetime import datetime
SN='10110000002037C8'   


def logs(str):

    curtime1=datetime.now().strftime('%Y%m%d %H:%M:%S')

    lirun=open('logs.log','a+')
    lirun.write(curtime1 + " " + str + "\n")
    lirun.flush()
    lirun.close()
    print(curtime1 + " "  + str)

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



def result0():
    
    t2 = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    logs(t2 + "_" + SN + "_logcat.txt")

    os.popen("adb -s " + SN + " shell logcat -v threadtime > " + t2 + "_" + SN + "_logcat.txt")


if __name__ == '__main__':

    for i in range(1,10001):

        connect()
        
        result0()


    



