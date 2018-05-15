# -*- encoding: UTF-8 -*-

import os,sys,time
from datetime import datetime

from useriface import device
from useriface import hostpc
from useriface import logger

sn = '4000105800000013'

dev = device.Device(sn)
ui = dev.uidevice
pc = hostpc.Host(sn)
log = logger.Logger(__file__)
log.addLog2file('PD801_camera_EVT.log')

pkg = 'com.android.camera2/com.android.camera.CameraLauncher'


def OnC():
    log.info("open camera")
    os.popen("adb -s " + sn + " shell am start " + pkg)
    time.sleep(2)
       

def OffC():    
    log.info("exit camera")
    ui.press.back()
    time.sleep(1.5)
    ui.press.back()
    time.sleep(1)


def Capture():
    log.info("capture picture")
    c = ui(packageName='com.android.camera2',className='android.widget.ImageView',resourceId='com.android.camera2:id/shutter_button')
    c.wait.exists()
    c.click()
    time.sleep(2)
    

def Switch(str):
    l = {'record':u'切换到视频模式','capture':u'切换到拍照模式'}
    log.info("switch %s"%str)
    c = ui(packageName='com.android.camera2',className='android.widget.ImageView',resourceId='com.android.camera2:id/camera_switcher')
    c.wait.exists()
    c.click()
    time.sleep(2)    

    log.info("select %s"%str)
    c = ui(packageName='com.android.camera2',className='android.widget.ImageView',description=l[str])
    c.wait.exists()
    c.click()
    time.sleep(2)

    

def Record():

    log.info("start recording")
    c = ui(packageName='com.android.camera2',className='android.widget.ImageView',resourceId='com.android.camera2:id/shutter_button')
    c.wait.exists()
    c.click()
    time.sleep(600)


    log.info("stop recording")
    c = ui(packageName='com.android.camera2',className='android.widget.ImageView',resourceId='com.android.camera2:id/shutter_button')
    c.wait.exists()
    c.click()
    time.sleep(2)

    

if __name__ == '__main__':


    for i in range(1,3001):
        log.info("============ test open and close camera: %d"%i)

        OnC()
        OffC()
        
    log.info("********** test open and close camera finish\n")    


    OnC()
    Switch('capture')
    for i in range(1,5001):

        log.info("============ test capture: %d"%i)
        Capture()
        if i % 100 == 0 and i < 4100:
            log.info("============ delete all jpg in /sdcard/DCIM/Camera/")
            os.popen("adb -s " + sn + " shell rm -rf /sdcard/DCIM/Camera/*.jpg")

    log.info("********** test capture finish\n")              


    OnC()
    Switch('record')
    for i in range(1,61):

        log.info("============ test recording: %d"%i) 
        Record()
        if i % 5 == 0 and i < 58:
            log.info("============ delete all mp4 in /sdcard/DCIM/Camera/")
            os.popen("adb -s " + sn + " shell rm -rf /sdcard/DCIM/Camera/*.mp4")
        
    log.info("********** test record finish\n")        


    OnC()
    for i in range(1,301):

        time.sleep(60)
        log.info("============ preview time: %dmin"%i)
        
    log.info("********** test preview finish\n")
        







    
