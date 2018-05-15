# -*- encoding: UTF-8 -*-

import os,sys,time
from datetime import datetime

from useriface import device
from useriface import hostpc
from useriface import logger

import multiprocessing

sn = 'testmode'
#sn = '50a99b07'

dev = device.Device(sn)
ui = dev.uidevice
pc = hostpc.Host(sn)
log = logger.Logger(__file__)
log.addLog2file('8909_camera_watch.log')



def OnC():

    log.info("open camera")
    os.popen("adb -s " + sn + " shell am start org.codeaurora.snapcam/com.android.camera.CameraLauncher")
    time.sleep(3)
    
    

def OffC():
    
    log.info("exit camera")
    ui.press.back()
    time.sleep(3)
    

def Capture():
    
    log.info("capture picture")
    c = ui(packageName='org.codeaurora.snapcam',className='android.widget.ImageView',resourceId='org.codeaurora.snapcam:id/shutter_button')
    c.wait.exists()
    c.click()
    time.sleep(3)
    
    

def Switch(str):

    l = {'record':u'切换到视频模式','capture':u'切换到拍照模式'}
    log.info("switch %s"%str)
    c = ui(packageName='org.codeaurora.snapcam',className='android.widget.ImageView',resourceId='org.codeaurora.snapcam:id/camera_switcher')
    c.wait.exists()
    c.click()
    time.sleep(3)    

    log.info("select %s"%str)
    c = ui(packageName='org.codeaurora.snapcam',className='android.widget.ImageView',description=l[str])
    c.wait.exists()
    c.click()
    time.sleep(3)

    

def Video():

    log.info("select settings")
    c = ui(packageName='org.codeaurora.snapcam',className='android.widget.ImageView',resourceId='org.codeaurora.snapcam:id/menu')
    c.wait.exists()
    c.click()
    time.sleep(3)
    
    log.info("select recording time")
    c = ui(packageName='org.codeaurora.snapcam',className='android.widget.TextView',text=u'视频时长')
    c.wait.exists()
    c.click()
    time.sleep(3)
    
    log.info("select no limit")
    c = ui(packageName='org.codeaurora.snapcam',className='android.widget.TextView',text=u'无限制')
    c.wait.exists()
    c.click()
    time.sleep(2)

    ui.press.back()
    time.sleep(2)    
    ui.press.back()
    time.sleep(2)
    

def Record():

    log.info("start recording")
    c = ui(packageName='org.codeaurora.snapcam',className='android.widget.ImageView',resourceId='org.codeaurora.snapcam:id/shutter_button')
    c.wait.exists()
    c.click()
    time.sleep(1800)


    log.info("stop recording")
    c = ui(packageName='org.codeaurora.snapcam',className='android.widget.ImageView',resourceId='org.codeaurora.snapcam:id/shutter_button')
    c.wait.exists()
    c.click()
    time.sleep(3)

    

if __name__ == '__main__':


    for i in range(1,2001):

        log.info("============ test open and close camera: %d"%i)

        OnC()
        OffC()
        
    log.info("********** test open and close camera finish\n")    

    OnC()
    Switch('capture')

    for i in range(1,2001):

        log.info("============ test capture: %d"%i)
        Capture()
        if i % 100 == 0:
            log.info("============ delete all files in /sdcard/DCIM/Camera/")
            os.popen("adb -s " + sn + " shell rm -rf /sdcard/DCIM/Camera/*")

    log.info("********** test capture finish\n")              


    OnC()
    Switch('record')
    Video()

    for i in range(1,49):

        log.info("============ test recording: %d"%i) 
        Record()
        log.info("============ delete all files in /sdcard/DCIM/Camera/")
        os.popen("adb -s " + sn + " shell rm -rf /sdcard/DCIM/Camera/*")
        
    log.info("********** test record finish\n")        

    OnC()

    for i in range(1,4320):

        time.sleep(60)
        log.info("============ preview time: %dmin"%i)
        
    log.info("********** test preview finish\n")
        







    
