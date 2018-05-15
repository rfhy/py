# -*- coding: UTF-8 -*-

import os,sys,time
from datetime import datetime


SN='1234567890AUTOBB'


def logs(str):

    curtime=datetime.now().strftime('%Y%m%d %H:%M:%S')

    lirun=open('reboot_log.log','a+')
    lirun.write(curtime + " " + str + "\n")
    lirun.flush()
    lirun.close()
    print(curtime + " "  + str) 


def reboot():

    os.popen("adb -s " + SN + " wait-for-device")
    time.sleep(1)
    
    logs("find device: " + SN)
    time.sleep(1)
    
    logs("reboot device")
    os.popen("adb -s " + SN + " reboot")
    
    logs("wait for device reboot")
    os.popen("adb -s " + SN + " wait-for-device")
    
    time.sleep(20)
    
    for i in range(0,100):
        ls = os.popen("adb -s " + SN + " shell ls -l /sdcard/").read()
        if ls.find('Download') != -1:
            logs("reboot sucess.\n")
            break
        else:
            time.sleep(3)
            if i == 99:
                logs("reboot fail.\n")


if __name__ == '__main__':

    for i in range(1,10000):
        
        logs("================= reboot times : %d" %i)
        
        reboot()



