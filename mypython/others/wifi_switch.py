# -*- coding: UTF-8 -*-

import os,sys,time
import multiprocessing
import subprocess
import threading
from datetime import datetime

SN='101502000000004D'



def logs(str):

    curtime=datetime.now().strftime('%Y%m%d %H:%M:%S')

    lirun=open('wifi_switch.log','a+')
    lirun.write(curtime + " " + str + "\n")
    lirun.flush()
    lirun.close()
    print(curtime + " "  + str)

def wifi():

    os.popen("adb -s " +SN+ " shell wait-for-device")

    logs("find device: " +SN)

    ip = os.popen("adb -s " +SN+ " shell busybox ifconfig").read()

    if ip.find("wlan0") == -1:

        logs("status: wifi is closed")
        logs("try to open wifi")

        os.popen("adb -s " +SN+ " shell am start com.android.settings/.Settings")

        time.sleep(3)
        
        os.popen("adb -s " +SN+ " shell input tap 300 200")

        return "open wifi"

    if ip.find("wlan0") != -1:

        logs("status: wifi is opened")
        logs("try to close wifi")

        os.popen("adb -s " +SN+ " shell am start com.android.settings/.Settings")

        time.sleep(3)
        
        os.popen("adb -s " +SN+ " shell input tap 300 200")

        return "close wifi"

if __name__ == '__main__':

    for i in range(1,100):

        logs("==================== test times : %d" %i)
        print wifi()
