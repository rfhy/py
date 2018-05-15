# -*- coding: UTF-8 -*-

import os,time
from datetime import datetime
import multiprocessing

sn = '151000010000002C'

def logs(str):
    c1=datetime.now().strftime('%Y%m%d-%H:%M:%S')
    lirun=open('PD801_ft_reboot.log','a+')
    lirun.write(c1 + " " + str + "\n")
    lirun.flush()
    lirun.close()
    print(c1 + " "  + str)

def reboot():
    os.system("adb -s " + sn + " wait-for-device")
    logs("reboot device")
    os.system("adb -s " + sn + " shell reboot")
    os.system("adb -s " + sn + " wait-for-device")
    logs("after reboot,find device: "+sn)
    time.sleep(3.5)

def tf():
    for i in range(0,1000):
        df1 = os.popen("adb -s " + sn + " shell \"df | grep internal\"").read()
        df2 = os.popen("adb -s " + sn + " shell \"df | grep external\"").read()
        if df2.find("/mnt/external_sd") != -1:
           logs("reboot sucess,find internal_sd and external_sd")
           d1 = df1.split('\r\n')[-2]
           logs(d1)
           d2 = df2.split('\r\n')[-2]
           logs(d2+"\n")
           break
        time.sleep(0.1)
    
if __name__ == '__main__':
    
    for i in range(1,8001):
        logs("================================== reboot and find tf times: %d"%i)
        reboot()
        tf()
    logs("==== reboot and find tf test finish")
