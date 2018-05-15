# -*- coding: UTF-8 -*-

import os,time
from datetime import datetime
import multiprocessing

sn = '1510000100000022'

def logs(str):
    c1=datetime.now().strftime('%Y%m%d-%H:%M:%S')
    lirun=open('PD801_16G_reboot_while_write_EVT.log','a+')
    lirun.write(c1 + " " + str + "\n")
    lirun.flush()
    lirun.close()
    print(c1 + " "  + str)

def push():
    logs("push video1.mp4 to /sdcard/")
    os.system("adb -s " + sn + " push video1.mp4 /sdcard/")
    time.sleep(1)

def copy():
    logs("wait for device")
    os.system("adb -s " + sn + " wait-for-device")
    logs("copy /sdcard/video1.mp4 to /data/video1.mp4")
    os.system("adb -s " + sn + " shell cp /sdcard/video1.mp4 /data/video1.mp4")

def reboot():
    os.system("adb -s " + sn + " wait-for-device")
    logs("reboot device\n")
    os.system("adb -s " + sn + " shell reboot")
    
if __name__ == '__main__':
    
    for i in range(1,1001):
        try:
            m1 = multiprocessing.Process(target=push)
            m2 = multiprocessing.Process(target=reboot)
            logs("*** reboot device while push file: %d times"%i)
            m1.start()
            time.sleep(15)
            m2.start()
            time.sleep(45)
        except Exception,e:
            print("exception: " + e)
