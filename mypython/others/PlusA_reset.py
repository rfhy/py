# -*- coding: UTF-8 -*-

import os,sys,time
import multiprocessing
import subprocess
import threading
from datetime import datetime

from uiautomator import Device

SN='101502000000004D'
ui = Device(SN)


def logs(str):

    curtime=datetime.now().strftime('%Y%m%d %H:%M:%S')
    lirun=open('PlusA_eset.log','a+')
    lirun.write(curtime + " " + str + "\n")
    lirun.flush()
    lirun.close()
    print(curtime + " "  + str)



def flow():

    
    #s1 = ui(packageName='com.android.launcher3',index='3',className='android.widget.Button',text=u'确定')
    #s1.wait.exists()
    #s1.click()

    #s2 = ui(packageName='com.android.launcher3',className='android.widget.Button',index='2',text=u'确定')
    #s2.wait.exists()
    #s2.click()

    logs("open settings")
    settings = os.popen("adb -s " + SN + " shell am start com.android.settings/.Settings")
    time.sleep(3)   

    logs("scrool to reset and backup")
    ui(scrollable=True).scroll.to(text=u'备份和重置')
    time.sleep(3)
   
    logs("click reset and backup")
    ui(packageName='com.android.settings',className='android.widget.TextView',text=u'备份和重置').click()
    time.sleep(3)

    logs("select reset")
    ui(packageName='com.android.settings',className='android.widget.TextView',text=u'恢复出厂设置').click()
    time.sleep(3)
    
    logs("select sd card")
    ui(packageName='com.android.settings',className='android.widget.CheckBox',index='0').click()
    time.sleep(3)
    
    logs("select reset tablet")
    ui(packageName='com.android.settings',className='android.widget.Button',text=u'重置平板电脑').click()
    time.sleep(3)
    
    logs("earse all things")
    ui(packageName='com.android.settings',className='android.widget.Button',text=u'清除全部内容').click()
    time.sleep(3)
    


    

if __name__ == '__main__':

    for i in range(1,10000):
        
        logs("============================= test times : %d" %i)
        
        flow()



