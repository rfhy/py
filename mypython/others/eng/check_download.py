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


def Checksize():

    ls1 = os.popen("adb -s " + SN + " shell ls -l /sdcard/Download/").read()

    logs(ls1)

    time.sleep(2)



if __name__ == '__main__':

    for i in range(1,1000000):

        logs("=================== testtimes : %d ===================" %i)

        connect()
        Checksize()
