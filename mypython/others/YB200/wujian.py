# -*- coding: UTF-8 -*-

import os,time,sys
import subprocess
import multiprocessing
from datetime import datetime

global g
g = 5 #5分钟检测一次结果

SN='100000f30108a99ccc43'
logname = 'wujiance.log'
local = 'area:2' #图像所在区间


def prints(str):

    t = datetime.now().strftime('%Y%m%d %H:%M:%S')
    print(t + " " + str)


def logs():

    os.popen("adb -s " + SN + " shell logcat -c")#清除log缓存
    
    time.sleep(0.5)
    
    t1 = datetime.now().strftime('%Y%m%d %H:%M:%S')
    prints("start catch log")

    #subprocess.Popen("adb -s " + SN + " logcat -v time -s roobosmart | findstr /c:\"people out\" /c:\"head\" > " + logname)

    os.popen("adb -s " + SN + " shell \"logcat -v time -s roobosmart | grep -e 'people out' -e 'head'\" > " + logname + " &")


def kill():
    
    time.sleep(g * 60)

    pids = os.popen("adb -s " + SN + " shell ps | findstr logcat").read()

    if "logcat" in pids:

        u = pids.split()
        
        for i in range(0,len(u)):
            
            if u[i] == "logcat":

                pid = u[i-7]

                os.popen("adb -s " + SN + " shell kill " + pid)
                
    prints("stop catch log")
    

def tofile(name,str):
    
    f1 = open(name,"a+")
    f1.write(str)
    f1.flush()
    f1.close()
    
    global f0
    f0 = open(name).readlines()
    return len(f0)   

def wrifile(file2):

    a = ['area:1','area:2','area:3','area:4','area:5','area:12','area:23','area:34','area:45','area:13','area:24','area:35','area:14','area:25','area:15']

    if local in a:

        a.remove(local)
    
    f2 = open(logname)
    f3 = open(file2,"a+")

    for line in f2.readlines():

        if file2 == 'area':
         
            if 'head[1-0]' in line:
            
                for i in range(0,13):
                
                    if a[i] in line: 
                
                        f3.write(line)
                        f3.flush()
                        
        if file2 == 'nopeople':
        
            if 'people out' in line:
                
                f3.write(line)
                f3.flush()

        if file2 == 'oktime':
        
            if 'head[1-0]' in line and local in line:
                
                f3.write(line)
                f3.flush()       
    
    f3.close()
    f2.close()

    global f0
    f0 = open(file2).readlines()
    return len(f0)
    
    

def head():
    #检测到超过一个头肩

    head = os.popen("findstr /c:-1] " + logname).read()

    tofile("head.txt",head)
    
    prints("head check is wrong: %d times."%len(f0))
    

def area():
    #只检测到一个头肩，但是区间不对

    wrifile('area.txt')
    prints("area is wrong: %d times."%len(f0))


def nopeople():
    #没有检测到头肩

    wrifile('nopeople.txt')
    prints("can't find people: %d times."%len(f0))


def oktime():
    #只检测到一个头肩，并且区间正确

    wrifile('nopeople.txt')
    prints("pass time is: %d times."%len(f0))


if __name__ == '__main__':

    for i in range(1,10001):
        
        ti = g * i
        m = ti % 60
        h = ti / 60

        print("\n++++++++++++++++ %d: %dh %dmin +++++++++++++++"%(i,h,m))
        

        m = multiprocessing.Process(target=kill)
        m.start()

        logs()

        head()

        area()

        nopeople()

        oktime()
            
