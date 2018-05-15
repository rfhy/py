# -*- encoding: UTF-8 -*-

import os,sys,time
from datetime import datetime
import random
import multiprocessing

sn = '151000010000003B'
#pkg = 'com.android.camera2/com.android.camera.CameraLauncher'
#pkg = 'com.ijourney.keephealthy/com.cn.keephealthy.ui.MainActivity'
pkg = 'com.tencent.qqlivekid/.activity.WelcomeActivity'

def logs(str):
   c1 = datetime.now().strftime('%Y%m%d-%H:%M:%S')
   lirun = open("online_reboot_check_D007C40_xiaoqie.log","a+")
   print(c1 + " " + str)
   lirun.write(c1 + " " + str + "\n")
   lirun.flush()
   lirun.close()

def OnC():
    os.popen("adb  -s " + sn + " wait-for-device")
    time.sleep(5)
    logs("open online video")
    time.sleep(0.5)
    os.popen("adb -s " + sn + " shell am start " + pkg)
    time.sleep(8)

def Play():
    logs("play online video")
    #yangshengtang
    #os.popen("adb -s " + sn + " shell input tap 850 500")
    #xiaoqie
    os.popen("adb -s " + sn + " shell input tap 200 200")
    time.sleep(8)
    
def check():
    a = os.popen("adb devices").read()
    t = random.randrange(60,150)
    if a.find(sn) != -1:
        logs("device not reboot,try again")
        os.popen("adb -s " + sn + " reboot")
        os.popen("adb  -s " + sn + " wait-for-device")
        logs("sleep time: %ds"%t)
        time.sleep(t)
    else:
        logs("*************** device reboot!!!")
        logs("sleep time: %ds"%t)
        time.sleep(t)

def logcat():
    ct = datetime.now().strftime('%Y%m%d_%H%M%S')
    logs("save logcat: " + ct + "_logcat_PD801.log")
    os.popen("adb -s " + sn + " shell logcat -v threadtime > ./online/" + ct + "_logcat_PD801.log")

def kmsg():
    ct = datetime.now().strftime('%Y%m%d_%H%M%S')
    logs("save kmsg: " + ct + "_kmsg_PD801.log")
    os.popen("adb -s " + sn + " shell cat /proc/kmsg > ./online/" + ct + "_kmsg_PD801.log")
        

if __name__ == '__main__':

    #os.popen("mkdir online")
    #time.sleep(1)

    for i in range(1,1001):
        logs("=========================== test play online video: %d"%i)
        '''
        m1 = multiprocessing.Process(target=logcat)
        m2 = multiprocessing.Process(target=kmsg)
        m1.start()
        time.sleep(0.5)
        m2.start()
        time.sleep(2)
        '''
        
        OnC()
        Play()
        time.sleep(5)
        check()
