# -*- coding: UTF-8 -*-

import hashlib
import os,sys,time
from datetime import datetime

#SN = '0123456789ABCDEF'
SN = '192.168.40.125:5555'
localmd5 = 'CD573CFAACE07E7949BC0C46028904FF'
testtimes = 3

file1 = '/sdcard/'
name = '1G.txt'

curtime0 = datetime.now().strftime('%Y%m%d_%H%M%S')

def Logfile(str):
   
   lirun = open(curtime0 + "_checkmd5.log","a+")

   print(str)

   lirun.write(str + "\n")
   
   lirun.flush()

   lirun.close()


def CopyCheck(usbtf):
   
   items = {'otg' : '/storage/usbotg/' , 'tf' : '/storage/sdcard1/'}

   select = items[usbtf]

   count1 = 0
   count2 = 0
   
   for i in range(1,testtimes):

      curtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

      Logfile("\n========== " + curtime + " copy file to " + usbtf + " test, times: %d ==========" %i)

      mkdirf = os.popen("adb -s " + SN + " shell mkdir " + select + "testf").read()
      
      if mkdirf.find("mkdir failed") == -1 or mkdirf.find("File exists") !=-1:

         pass
      
      else:
         
         Logfile("Please insert " + usbtf + " and then start test again!")

         exit()

      Logfile("start copy " + file1 + name + " to " + select)

      os.popen("adb -s " + SN + " shell cp " +  file1 + name + " " + select)

      time.sleep(3)

      Logfile("copy file finish, wait for check md5...")

      cpmd5 = os.popen("adb -s " + SN + " shell busybox md5sum " + select + name).read()

      cpmd51 = cpmd5.split()[0].upper()

      Logfile("local file md5 is : " + localmd5)
      Logfile("copy  file md5 is : " + cpmd51)
   
      if cpmd51 == localmd5:

         Logfile("md5 check pass, so copy pass!")

         count1 += 1

      else:

         Logfile ("md5 check pass, so copy fail!")

         count2 += 1

   Logfile("\n\n%d times pass." %count1)

   Logfile("%d times fail.\n\n" %count2)


if __name__ =='__main__':

   CopyCheck('tf')

   CopyCheck('otg')
