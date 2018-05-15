# -*- coding: UTF-8 -*-

import os,sys,time
from datetime import datetime
import xlrd
import xlwt
from pyExcelerator import *

SN = '50a99b07'
#SN = '1011000000110037'
#SN = '1011000000110021'
#SN = '1011000000101059'
#SN='302000f10008a5983343'
#SN='100000f30108a99ccc43'
#SN='1014010000000086'
testtimes = 100000
#logname = ''
global m
m = 0

w = Workbook()
ws = w.add_sheet('8009 top mem')

curtime = datetime.now().strftime('%Y%m%d_%H%M%S')


def Logfile(str):

    lirun = open(curtime + "_top_mem.txt","a+")
    
    lirun.write(str)
    lirun.flush()
    lirun.close()
    
    print(str)

    

def Top(mem):

    total = 0
    strs = []

    curtime2 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    strs.append(curtime2)
    
    tops = os.popen("adb -s " + SN + " shell top -n 1").read()

    if tops.find("PID") != -1:

        for s in mem:

            try:

                num = tops.split().index(s)

                cpu = tops.split()[num - 7]

                strs.append(cpu)

                if mem.index(s) == 0:

                    Logfile(curtime2 + " " + s + ":  " + cpu + "    ")
                    
                else:
                    
                    Logfile(s + ":  " + cpu + "    ")
                    
            except Exception ,e:

                Logfile(s + ":  " + "error    ")

                print e

                strs.append('error')

        for i in range(0,2):
            
            alls = tops.split(',')[i].split()
            
            strs.append(alls[1])

            Logfile(alls[0] + ":  " + alls[1] + "    ")

            total += int(alls[1].split('%')[0])

        Logfile("total cpu is : %d%%"%total)

        strs.append(str(total) + '%')
        
        
        Logfile("\n")


        title = ['time'] + mem + ['User','System','Total']

        for n in range(0,len(title)):

            global m

            if m == 0:

                ws.write(m,n,title[n])

            else:

                ws.write(m,n,strs[n])

        w.save(curtime + "_top_mem.xls")
    
        m += 1

        time.sleep(6.5)


    else:

        Logfile("can't find top files, sleep 10s and then try again.\n")

        time.sleep(10)
        Logfile("check device status\n")
        os.popen("adb -s " + SN + " wait-for-device")
        Logfile("find devices\n")

        Top(mem)


if __name__ == '__main__':

    mem = ['com.roobo.ioe.smartcontrol','/system/bin/mm-qcamera-daemon','/system/bin/mediaserver','/system/bin/surfaceflinger']   

#    os.popen("adb -s " + SN + " shell am start -n com.roobo.cameraapp/.CameraActivity")

    for i in range(1,testtimes):          

        Top(mem)

#        if i % 60 == 0:

#            os.popen("adb -s " + SN + " shell am start -n com.roobo.cameraapp/.CameraActivity")



        

        
