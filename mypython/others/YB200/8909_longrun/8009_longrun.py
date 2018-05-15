#coding:utf-8

import os
import datetime,time

tag = 'clientId'
sn = ['21122250731610403A0148','21122250731610403A0149','21122250731610403A0150','21122250731610403A0151','21122250731610403A0152','21122250731610403A0153','211222507317928026002Z','211222507337420026001Z','2112225073169190280003','211222507316C10028010Z']
fn = 'log.txt'
a = []
ota = 18000 #4小时 加 1小时，正常OTA请求4小时1次

def logs(str):
    f = open('longrun_10pcs.log','a+')
    if str != '\n':
        f.write(str+"\n")
    else:
        f.write(str)
    f.flush()
    f.close()
    print(str)


def check(d):

    #December 25th 2017; 07:04:51.827
    t1 = d.split()[2].split(';')[0]
    t3 = d.split()[1][0:-2]
    t4 = d.split()[3].split('.')[0]
    if d.split()[0] == 'December':
        t2 = '12'
    t5 = t1 + "-" + t2 + "-" + t3 + " " + t4
    t6 = time.strptime(t5, '%Y-%m-%d %H:%M:%S')
    t7 = time.mktime(t6)
    t0 = time.time() - t7
    if t0 < ota:
        return 'pass'
    else:
        return 'fail'
   

def longrun():

    f = open(fn).readlines()
    for i in range(0,len(f)):
        try:           
            if f[i].find(tag) != -1:            
                s = f[i].split(tag)[1].split('"')[2]
                if s in sn and s not in a:
                    
                    t = f[i].split(',')[0]
                    result = check(t)
                    a.append(s)
                    logs(t + ": " + s + " " + result)
            else:
                pass
            
        except Exception,e:
            print e

    for t1 in range(0,len(sn)):
        if sn[t1] not in a:
            logs("\n error: " + sn[t1] + " is lost.")

    logs("\n")
            

if __name__ == '__main__':

    curtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logs("curtime is: " + curtime)
    longrun()
    
