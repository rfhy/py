# -*- coding: UTF-8 -*-

import hashlib
import os,sys,time
from datetime import datetime

#SN = '192.168.40.125:5555'
SN = '0123456789ABCDEF'
localmd5 = 'CD573CFAACE07E7949BC0C46028904FF'
testtimes = 2000

curtime0 = datetime.now().strftime('%Y%m%d_%H%M%S')

def Logfile(str):
   
   lirun = open(curtime0 + "_reboot_check_usbtf.log","a+")

   print(str)

   lirun.write(str + "\n")
   
   lirun.flush()

   lirun.close()
   

#测试前检查设备是否在线
start = os.popen("adb devices").read()
      
if start.find(SN) != -1:

   pass
      
else:
         
   Logfile("can't find device, please check!")

   exit()

#测试前检查是否有TF卡或OTG
def RebootCheck(usbtf):
   
   items = {'otg' : '/storage/usbotg/' , 'tf' : '/storage/sdcard1/'}

   select = items[usbtf]

   count1 = 0
   count2 = 0
   
   mkdirf = os.popen("adb -s " + SN + " shell mkdir " + select + "testf").read()
      
   if mkdirf.find("mkdir failed") == -1 or mkdirf.find("File exists") !=-1:

      pass
      
   else:
    
      Logfile("\ncan not find " + usbtf + " before test, pls check and then start test again!")

      exit()

#重启1分钟后检查设备在不在线


   for i in range(1,testtimes):

      curtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

      Logfile("\n========== " + curtime + " reboot and check " + usbtf + " test, times: %d ==========" %i)
      
      Logfile("start reboot")

      os.popen("adb -s " + SN + " shell reboot")

      Logfile("wait 60s")

      time.sleep(60)     
      
      reboot = os.popen("adb devices").read()
      
      if reboot.find(SN) != -1:

         Logfile("reboot sucess")
    
      else:
         
         Logfile("reboot fail")

         exit()

#重启后检查TF卡或者OTG是否挂载
      mkdirf = os.popen("adb -s " + SN + " shell mkdir " + select + "testf").read()
      
      if mkdirf.find("mkdir failed") == -1 or mkdirf.find("File exists") !=-1:

         Logfile("find " + usbtf + " after reboot")

         count1 += 1
      
      else:
    
         Logfile("can not find " + usbtf + " after reboot")

         count2 += 1

#打印测试成功失败的次数

   Logfile("\n\n%d times pass." %count1)

   Logfile("%d times fail.\n\n" %count2)



if __name__ =='__main__':

   RebootCheck('tf')
