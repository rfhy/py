# -*- coding: UTF-8 -*-

import os,time,sys
import subprocess
import multiprocessing
from datetime import datetime

import xlrd
import xlwt
from pyExcelerator import *


SN = '0123456789ABCDEF'

pid = 'com.roobo.ioe.smartac.gree'

testtimes = 100000
global m
m = 0

w = Workbook()
ws = w.add_sheet('8009 smartcontrol and all mem')

curtime = datetime.now().strftime('%Y%m%d_%H%M%S')


def Logfile(str):

    lirun = open(curtime + "_ram.txt","a+")
    
    lirun.write(str)
    lirun.flush()
    lirun.close()
    
    print(str)

    

def ram():

    total = 0
    strs = []
    ioe = []

    curtime2 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print curtime2
    strs.append(curtime2)
    
    ram = os.popen("adb -s " + SN + " shell dumpsys meminfo").read()

    f0 = open("ram_tmp.txt","w+")

    f0.write(ram)

    f0.flush()

    line = open("ram_tmp.txt").readlines()

    if ram.find("Used RAM:") != -1:

        item = ['Total RAM','Free RAM','Used RAM','Lost RAM']

        try:

            for s in range(0,len(item)):

                strs.append(line[s - 6].split(": ")[1].split(" (")[0])

                print (line[s-6])
                    
        except Exception ,e:

            print e

            strs.append('error')

    else:

        print("can't find dumpsys meminfo, sleep 10s and then try again.\n")

        time.sleep(10)
        print("check device status\n")
        os.popen("adb -s " + SN + " wait-for-device")
        print("find devices\n")

        ram()


    if ram.find(pid) != -1:

        try:

            r = ram.split(pid)[0].split("\r\n")[-1].split(":")[0].strip()

            ioe.append(r)

            print (pid + ": %s\n" %r)

        except Exception ,e:

            print e

            strs.append('error')
        
    

    title = ['time'] + item + [pid]

    meminfo = strs + ioe

    for n in range(0,len(title)):

        global m

        if m == 0:

            ws.write(m,n,title[n])

        else:

            ws.write(m,n,meminfo[n])

    w.save(curtime + "_smartcontrol_ram.xls")
    
    m += 1

    time.sleep(5)




if __name__ == '__main__':
  

    for i in range(1,testtimes):          

        ram()

