# -*- coding: UTF-8 -*-

import os,time
from datetime import datetime
import multiprocessing

a= []
b = [a]

fl = 'log_done'

def logs(str):
    curtime=datetime.now().strftime('%Y%m%d %H:%M:%S')
    lirun=open('PD801_save_log_1.log','a+')
    lirun.write(curtime + " " + str + "\n")
    lirun.flush()
    lirun.close()
    print(curtime + " "  + str)


def wsn(str):
    f=open('sn.txt','a+')
    f.write(str + "\n")
    f.flush()
    f.close()  

 
def ser():
        global sn
        sn = []
        log = []
        s = os.popen("adb devices").read()
        s1 = s.split('\n')
        if len(s1) > 3:
            for i in range(1,len(s1)-2):
                s2 = s1[i].split('\t')[0]
                sn.append(s2)

        for i in range(len(sn)):
            if str(sn[i]) in b[-1]:
                try:
                    log.remove(str(sn[i]))
                except Exception,e:
                    pass
            elif str(sn[i]) not in b[-1]:
                log.append(str(sn[i]))
        for ii in range(len(b[-1])):
            if b[-1][ii] not in sn:
                logs("warning: %s is disconnect\n"%b[-1][ii])
        os.popen("del sn.txt")
        b[-1]=sn
        time.sleep(0.1)
        for t in range(len(log)):
            wsn(log[t])

        
def logcat(sn1):
    logs("================ %s ==================="%sn1)
    ct = datetime.now().strftime('%Y%m%d_%H%M%S')
    logs("save logcat: " + ct + "_logcat_PD801_" +sn1+".log")
    os.popen("adb -s " + sn1 + " shell logcat -v threadtime > ./"+fl+"/" + ct + "_logcat_PD801_" +sn1+".log")

def kmsg(sn1):
    ct = datetime.now().strftime('%Y%m%d_%H%M%S')
    logs("save kmsg: " + ct + "_kmsg_PD801_" +sn1+".log\n")
    os.popen("adb -s " + sn1 + " shell cat /proc/kmsg > ./"+fl+"/" + ct + "_kmsg_PD801_" +sn1+".log")
  


if __name__ == '__main__':

    logs("create folder %s"%fl)
    os.popen("mkdir %s"%fl)
    os.popen("copy nul sn.txt")
    time.sleep(0.5)
    
    for i in range(0,999999):
        try:
            ser()
            for str1 in open('sn.txt').readlines():
                sn1 = str1.split('\n')[0]
                
                m1 = multiprocessing.Process(target=logcat,args=(sn1,))
                m2 = multiprocessing.Process(target=kmsg,args=(sn1,))
                m1.start()
                ss = os.popen("adb -s " +sn1+" shell getprop ro.build.type").read().split('\r\n')[0]
                if ss == 'eng':
                    m2.start()
                elif ss == 'user':
                    time.sleep(1)
                    logs("user version,no need kmsg\n")
                else :
                    logs("**************************\n")
                    print ss
        except Exception,e:
            pass#print(e)
        time.sleep(0.5)
        
