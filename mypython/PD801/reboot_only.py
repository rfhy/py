# -*- coding: UTF-8 -*-

import os,time
from datetime import datetime
import multiprocessing

sn = '1510000100000037'

def logs(str):
    c1=datetime.now().strftime('%Y%m%d-%H:%M:%S')
    lirun=open('PD801_reboot.log','a+')
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
    time.sleep(15)


def check():
    data = os.popen("adb -s " + sn + " shell mount").read()
    for s in ['/data','/mnt/internal_sd','/system','/cache']:
        if data.count(s) > 0:
            logs("after reboot,%s mount sucess"%s)
    time.sleep(2)

    
if __name__ == '__main__':
    
    for i in range(1,1201):
        logs("=========================== reboot and check mount times: %d"%i)
        reboot()
        check()
    logs("==== reboot and check mount test finish")
