# -*- coding: UTF-8 -*-

import os,time,sys
from useriface import device
from useriface import hostpc
from useriface import logger

testtime = 1000
SN = '0123456789ABCDEF'
dev = device.Device(SN)
pc = hostpc.Host(SN)
ui = dev.uidevice
log = logger.Logger(__file__)
log.addLog2file('T1_reset.log')


def Reset():

    log.info("circle start")

    ui.press.home()
    

    log.info("zhidaole and mtklog watcher")
    
    ui.watcher("zhidaole").when(resourceId='com.android.launcher3:id/cling_dismiss_longpress_info').click(resourceId='com.android.launcher3:id/cling_dismiss_longpress_info')

    ui.watcher("mtklog").when(text='Tag Log').when(text='All log tools are stopped! Would you like to start all enabled log tools?').click(resourceId='android:id/button1')    


    log.info("Open setting in home page")

    time.sleep(5)

    ui(className='android.widget.TextView')[1].click()
    
    
    log.info("Swipe to reset page")

    time.sleep(3)
    
    ui(scrollable=True).scroll.to(text='备份和重置')
    

    log.info("Select reset in settings")
    
    time.sleep(3)

    ui(resourceId='com.android.settings:id/title')[5].click()
    
    
    '''  
    ui.swipe(100, 450, 100, 100, 30)

    time.sleep(3)

    ui.swipe(100, 450, 100, 100, 30)
    

    log.info("Select reset in settings")

    time.sleep(5)

    ui(resourceId='com.android.settings:id/title')[4].click()
    '''

    log.info("Select reset item")

    time.sleep(5)

    ui(className='android.widget.RelativeLayout')[1].click()
    

    log.info("select reset")

    time.sleep(5)

    ui(className='android.widget.Button').click()


    log.info("confirm reset")
    
    time.sleep(5)

    ui(className='android.widget.Button').click()

    

    log.info("wait for reset 150s")

    time.sleep(150)

    log.info("circle end\n")


if __name__ == '__main__':

    for i in range(1,testtime):

        log.info("============testtimes: %d ============" %i)

        Reset()

else:

    for i in range(1,testtime):

        log.info("============testtimes: %d ============" %i)

        Reset()
