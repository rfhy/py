# -*- coding: UTF-8 -*-

import hashlib
import os,sys,time
from datetime import datetime
from uiautomator import Device

#SN = '192.168.40.125:5555'
SN = '0123456789ABCDEF'
testtimes = 2000
ui = Device(SN)

curtime0 = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')


def Logfile(str):

   curtime3 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   
   lirun = open(curtime0 + "_reboot_times.log","a+")

   print(curtime3 + " " + str)

   lirun.write(curtime3 + " " + str + "\n")
   
   lirun.flush()

   lirun.close()

   
def CheckConnect(wifiusb='usb'):

    connecttype = {'wifi':'wifi','usb':'usb'}

    for w in range(1,1000):

         if wifiusb == 'wifi':
            
            os.popen("adb connect " + SN).read()
            
         if wifiusb == 'usb':

            os.popen("adb -s " + SN + " wait-for-device")
 
         adbls = os.popen("adb -s " + SN + " shell ls").read()

         if adbls.find("sdcard") != -1:

            break
            
         else:

            if w <= 998:

                time.sleep(2)

            else:
                
                Logfile(connecttype[wifiusb] + " adb connect fail, exit!")
                exit()        


def Remount():

    for items in ['root','remount']:

        for g in range(1,1000):

            item1 = {'remount':'succeeded','root':'adbd is already running as root'}

            item2 = {'remount':'remount succeeded','root':'restarting adbd as root'}
    
            remount = os.popen("adb -s " + SN + " " + items).read()

            if remount.find(item1[items]) != -1 or remount.find(item2[items]) != -1:

                time.sleep(2)

                break
            
            else:

                if g <= 998:

                    time.sleep(2)    

                else:
                
                    Logfile(items + " fail, exit!")
                    exit()


def BuildType():

   for r in range(1,1000):
   
      build_type = os.popen("adb -s " + SN + " shell getprop | findstr ro.build.type").read()

      if build_type.find('[ro.build.type]') != -1:

         #build = build_type.split(':')[1].replace('[','').replace(']','').strip()

         build = build_type.split(':')[1].strip().strip('[]')

         if build == 'eng':

            break

         if build == 'userdebug':

            Remount()
            break

         if build == 'user':

            Logfile("user version , can't test! exit!")         

            exit()

      else:

         if r <= 998:

            time.sleep(2)
            
         else:
            
            Logfile("can't find ro.build.type , exit!")
            exit()


def RebootTest():
   
   for i in range(1,testtimes):      

      Logfile("========== reboot test times: %d ==========" %i)

      t1 = time.time()

      os.popen("adb -s " + SN + " shell reboot")
      
      CheckConnect('usb')
      BuildType()
   
      settings = ui(packageName="com.android.launcher3",index="1")
      
      settings.wait.exists()

      t2 = time.time()
            
      tt = t2 - t1

      Logfile("reboot time is :  %d s\n" %tt)


if __name__ =='__main__':

   CheckConnect('usb')
   BuildType()

   RebootTest()
