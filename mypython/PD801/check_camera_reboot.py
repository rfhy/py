# -*- encoding: UTF-8 -*-

import os,sys,time
from datetime import datetime

from useriface import device
from useriface import hostpc
from useriface import logger
import random

sn = '1510000100000022'

dev = device.Device(sn)
ui = dev.uidevice
pc = hostpc.Host(sn)
log = logger.Logger(__file__)
log.addLog2file('8909_camera_reboot.log')

pkg = 'com.android.camera2/com.android.camera.CameraLauncher'


def OnC():
    log.info("open camera")
    os.popen("adb -s " + sn + " shell am start " + pkg)
    time.sleep(2)

def Capture():
    log.info("capture picture")
    c = ui(packageName='com.android.camera2',className='android.widget.ImageView',resourceId='com.android.camera2:id/shutter_button')
    c.wait.exists()
    c.click()
    time.sleep(3)
    
def check():
    a = os.popen("adb devices").read()
    if a.find(sn) != -1:
        log.info("device not reboot,try again")
        os.popen("adb -s " + sn + " reboot")
        os.popen("adb  -s " + sn + " wait-for-device")
        t = random.randrange(66,166)
        log.info("sleep time: %ds"%t)
        time.sleep(t)
    else:
        log.info("device reboot!!!")
        exit()

if __name__ == '__main__':

    for i in range(1,1001):

        log.info("== test open camera and capture: %d"%i)

        OnC()
        Capture()
        time.sleep(3)
        check()
