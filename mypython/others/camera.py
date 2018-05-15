# -*- coding: UTF-8 -*-

import os,time,sys
from useriface import device
from useriface import logger
from useriface import hostpc
from datetime import datetime
from sendemail_attach_import import Sendmail
import multiprocessing

#SN = '192.168.40.133:5555'
SN = '0123456789ABCDEF'
dev = device.Device(SN)
ui = dev.uidevice
pc = hostpc.Host(SN)
log = logger.Logger(__file__)


def Logfile():

    curtime0 = datetime.now().strftime('%Y%m%d_%H%M%S')

    global file1
    file1 = curtime0 +'_camera.log'
    log1 = log.addLog2file(file1)


#待机唤醒，进入applist，打开相机，拍照，进入图库，删除刚刚拍摄的照片，返回Home，待机


def WatcherRun():

    try:
        
        for i in range(1,30000001):
        
            ui.watcher("button").when(resourceId='com.android.gallery3d:id/right_btn').when(className='android.widget.Button').when(text='确定').click(text='确定')
            ui.watcher("crashs").when(className='android.widget.FrameLayout').when(packageName='android')

            if ui.watcher("button").triggered == True:

                log.info("button watcher triggered!")

                
            if ui.watcher("crashs").triggered == True:

                log.info("crashs watcher triggered!")

                test1 = ui(resourceId='android:id/button1')
                
                test2 = ui(className='android.widget.TextView',packageName='android',resourceId='android:id/message')

                print test2.text

                test1.click()

            ui.watchers.reset()

            time.sleep(1)
                
    except Exception,e:

        print e

        WatcherRun()
            
    
def Capture():

    curtime1 = datetime.now().strftime('%Y%m%d_%H%M%S')

    try:
        
        log.info("wakeup device")
        ui.wakeup()
        time.sleep(2)
    
        log.info("go to app list")
        ui(index='0',className='android.widget.TextView',longClickable='false').click()
        time.sleep(2)
    
        log.info("open camera")
        dev.startActivity(component='com.android.gallery3d/com.android.camera.CameraLauncher')
        time.sleep(8)
    
        log.info("capture")
        ui(index='0',className='android.widget.ImageView',resourceId='com.android.gallery3d:id/shutter_button_photo').click()
        time.sleep(5)
    
        log.info("open thumbnail")
        ui(resourceId='com.android.gallery3d:id/thumbnail').click()
        time.sleep(1.3)
    
        log.info("open more select")
        ui(index='1',className='android.widget.ImageButton').click()
        time.sleep(2)
    
        log.info("delete...")
        ui(text='删除').click()
        time.sleep(2)
    
        log.info("confirm delete")
        ui(resourceId='android:id/button1').click()
        time.sleep(2)
    
        log.info("back to home")
        ui.press.back()
        time.sleep(1)
        ui.press.home()
        time.sleep(1)
    
        log.info("device sleep\n")
        ui.sleep()
        time.sleep(5)

    except Exception ,e1:

        print e1

        try:
        
            log.info('test fail and stop')
            log.info('screencap')
            os.popen("adb -s " + SN + " shell screencap -p /sdcard/test.png")

            time.sleep(1)
            log.info(os.getcwd() + "\\" + curtime1 +"_%d.png"%t)
            os.popen("adb -s " + SN + " pull /sdcard/test.png " + os.getcwd() + "\\" + curtime1 +"_%d.png"%t)
        
            log.info('back to home and restart test again')
            ui.press.back()
            time.sleep(1)
            ui.press.back()
            time.sleep(1)
            ui.press.home()
            time.sleep(1)

        except Exception,e1:

            print e1

            log.info("--- try save picture fail ---")
        
        Capture()
        


if __name__ == '__main__':
   
    m2 = multiprocessing.Process(target=WatcherRun)
    m2.daemon = True #主进程结束，m2也结束
    m2.start()
    #m2.join() #加上后，m2会一直等待执行完

    Logfile()


    for t in range(1,501):
        
        log.info('============ testtime: %s ============' %t)

        Capture()
        
        t = t + 1
            
    ui.stop()
    

    log.info("test finish.\n")

    Sendmail('T1 camera capture test finish.','T1 camera capture test report',os.getcwd() + "\\" + file1)

    exit()



    

    

