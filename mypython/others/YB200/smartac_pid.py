#-*- encoding: utf-8 -*-

import os,sys,time
from datetime import datetime

#sn = '4001000C00000037'
sn = '4001000C000001BE'
pid = 'com.roobo.ioe.smartac.midea'

n = 0
a = []

def logs(str):
    t = datetime.now().strftime('%Y%m%d %H:%M:%S')
    f = open('smartac_pid.txt','a+')
    f.write(t + " " + str + "\n")
    f.flush()
    f.close()
    print(t + " " + str + "\n")

    
def pids():

    os.popen("adb -s " + sn + " wait-for-device")
    ps = os.popen("adb -s " + sn + " shell ps").read()
    pids = ps.split('\r\n')
    
    global n
    n = n + 1

    for i in range(0,len(pids) - 1):

        try:

            if pids[i].split()[-1] == pid:
                p1 = pids[i].split()[1]
                    
                if n == 1:
                    logs(pid + " before test , pid is: " + p1)
                    a.append(p1)
                    
                if n > 1 and a[-1] != p1:

                    a.append(p1)
                    t = len(a) - 1
                    logs(pid + " is crash , new pid is: " + p1 + " , time: %d"%t)
                    break
           
        except Exception , e :
            print(e)


if __name__ == '__main__':

    for i in range(0,1000000):
        pids()
        time.sleep(5)
    
    
    
    
