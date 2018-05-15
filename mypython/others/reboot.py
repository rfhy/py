# -*- coding: UTF-8 -*-

import os,sys,time
import multiprocessing
import subprocess
import threading
from datetime import datetime

from uiautomator import Device

SN='101502000000004D'
localmd5 = 'd8b61b2c0025919d5321461045c8226f'
ui = Device(SN)


def logs(str):

    curtime=datetime.now().strftime('%Y%m%d %H:%M:%S')

    lirun=open('reboot_log.log','a+')
    lirun.write(curtime + " " + str + "\n")
    lirun.flush()
    lirun.close()
    print(curtime + " "  + str)



def Copy():

    ls = os.popen("adb -s " + SN + " shell ls /mnt/external_sd/500M.txt").read()

    if ls.find("No such file or directory") != -1:

        logs("fail , can not find file in TF.\n")

    logs("copy 500M file : /mnt/external_sd -> /mnt/internal_sd")

    os.popen("adb -s " + SN + " shell cp /mnt/external_sd/500M.txt /mnt/internal_sd/")

    time.sleep(1)

    logs("copy file finish, wait for check md5...")


def md5(str):

    cpmd5 = os.popen("adb -s " + SN + " shell busybox md5sum /mnt/internal_sd/500M.txt").read()

    cpmd51 = cpmd5.split()[0]

    logs("local file md5 is : " + localmd5)
    logs("copy  file md5 is : " + cpmd51)
   
    if cpmd51 == localmd5:

        logs(str + " pass!")

    else:

        logs (str + " fail!")


    


def reboot():

    os.popen("adb -s " + SN + " wait-for-device")
    time.sleep(1)
    
    logs("find device: " + SN)
    time.sleep(1)

    Copy()
    md5("copy")
    
    logs("reboot device")
    os.popen("adb -s " + SN + " reboot")
    
    logs("wait for device reboot")
    os.popen("adb -s " + SN + " wait-for-device")
    
    time.sleep(20)
    
    settings = ui(packageName="com.android.launcher3",index="0")

    test = ui(packageName='com.htfyun.funtest',index='2')
    
    if settings.wait.exists() or test.wait.exists():

        logs("device reboot sucess\n")

        md5("after reboot,file md5")

        logs("delete copy file")

        os.popen("adb -s " + SN + " shell rm /mnt/internal_sd/500M.txt")

        time.sleep(1)

        ll = os.popen("adb -s " + SN + " shell ls /mnt/internal_sd/500M.txt").read()

        if ll.find("No such file or directory") != -1:

            logs("delete copy file sucess\n")

    

    

if __name__ == '__main__':

    for i in range(1,10000):
        
        logs("============================= test times : %d" %i)
        
        reboot()



