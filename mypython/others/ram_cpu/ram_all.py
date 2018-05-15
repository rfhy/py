# -*- coding: UTF-8 -*-

import os,time,sys
import subprocess
import multiprocessing
from datetime import datetime

import xlrd
import xlwt
from pyExcelerator import *


SN = 'testmode'

testtimes = 1000
global m
m = 0

w = Workbook()
ws = w.add_sheet('8009 ram mem')

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

    curtime2 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print curtime2
    strs.append(curtime2)
    
    ram = os.popen("adb -s " + SN + " shell dumpsys meminfo").read()

    if ram.find("Used RAM:") != -1:

        f0 = open("ram_tmp.txt","w+")

        f0.write(ram)

        f0.flush()

        line = open("ram_tmp.txt").readlines()

        item = ['Total RAM','Free RAM','Used RAM','Lost RAM']

        try:

            for s in range(0,len(item)):

                strs.append(line[s - 6].split(": ")[1].split(" (")[0])

                print (line[s-6])
                    
        except Exception ,e:

            print e

            strs.append('error')
        


        title = ['time'] + item

        for n in range(0,len(title)):

            global m

            if m == 0:

                ws.write(m,n,title[n])

            else:

                ws.write(m,n,strs[n])

        w.save(curtime + "_ram.xls")
    
        m += 1

        time.sleep(1.5)


    else:

        print("can't find dumpsys meminfo, sleep 10s and then try again.\n")

        time.sleep(10)
        print("check device status\n")
        os.popen("adb -s " + SN + " wait-for-device")
        print("find devices\n")

        ram()


def push(config):

    os.popen("adb -s " + SN + " shell input keyevent 4")

    time.sleep(2)

    os.popen("adb -s " + SN + " push config.json /sdcard/Android/data/com.roobo.ioe.smartcontrol/files/")


if __name__ == '__main__':

    


    for i in range(1,testtimes):          

        ram()

