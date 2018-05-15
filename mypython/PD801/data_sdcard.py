# -*- coding: UTF-8 -*-

import os,sys,time
from datetime import datetime

SN = '151000010000002C'
localmd5 = 'cd573cfaace07e7949bc0c46028904ff'

f = '/mnt/internal_sd/'
t = '/data/'
name = '1G.txt'
a = []

c0 = datetime.now().strftime('%Y%m%d_%H%M%S')

def Logfile(str):
   c1 = datetime.now().strftime('%Y%m%d-%H:%M:%S')
   lirun = open(c0 + "_emmc.log","a+")
   print(c1 + " " + str)
   lirun.write(c1 + " " + str + "\n")
   lirun.flush()
   lirun.close()


def CopyCheck(p1,p2):

    Logfile("start copy " + p1 + name + " to " + p2)
    t1 = time.time()
    os.popen("adb -s " + SN + " shell cp " +  p1 + name + " " + p2)
    t2 = time.time()
    t3 = t2 - t1
    su = 1024/float(t3)
    a.append(su)
    
    Logfile("copy finish: %.2fM/s"%su)
    cpmd5 = os.popen("adb -s " + SN + " shell busybox md5sum " + p2 + name).read()
    cpmd51 = cpmd5.split()[0]

    if cpmd51 == localmd5:
        Logfile("md5 check pass")
    else:
        Logfile("local file md5 is : " + localmd5)
        Logfile("copy  file md5 is : " + cpmd51)
        Logfile ("md5 check fail")
        exit()
        
    Logfile ("delete " + p1 + name + "\n")
    os.popen("adb -s " + SN + " shell rm " + p1 + name)

if __name__ =='__main__':

   for i in range(1,201):
      Logfile ("========== testtime: %d"%i)
      CopyCheck(t,f)
      time.sleep(0.5)
      CopyCheck(f,t)

   ave = float(sum(a))/len(a)
   Logfile ("average: %.2fM/s"%ave)
   

