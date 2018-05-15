# -*- coding: UTF-8 -*-

import os,sys,time
from datetime import datetime

#puddings

SN= '1011010000200E1B'
t = 3
testtimes = 100
#testtimes = input("Pls input testtimes: ")

def RXCheck():

    RX = []

    for i in range(0,testtimes):

        file1 = open("pingcheck.log","a+")

        time1 = datetime.now().strftime('%y-%m-%d %H:%M:%S')

        ifconfig = os.popen("adb -s " + SN + " shell busybox ifconfig").read()
        #\r\n空行也算一个
        test = ifconfig.split('\r\n')
        
        if ifconfig.find("bytes") != -1:

            str1 = test[24]

            str2 =str1.split()[1].split(':')[1]
            
#            str2 =str1.split()[2].strip('(') 
#            str3 =str1.split()[3].strip(')')      
            
            RX.append(str2)
            
#            print RX

            if i >= 1:

                n = (int(RX[i]) - int(RX[i-1])) / t / 1024
                
                print(time1 + " RX is: %d kb/s" %n)
                file1.write(time1 + " RX is: %d kb/s \n" %n)
                file1.close()


#            print str3
            time.sleep(t)
        
        else:

            print ("Can't find RX")

def OnlineCheck():

    online1 = os.popen("adb devices").read()
    
    for l in range(1,20):
        
        if online1.find(SN) != -1 and online1.find("device") != -1:
            break
        else:
            if l <= 6:                
                print ("can't find device")
                time.sleep(10)
            else:
                print("can't find device in 60s, exit!")
                exit()


def PingCheck():
    
    for m in range(1,20):
                
        ping1= os.popen("adb -s " + SN + " shell ping -c 3 www.baidu.com").read()
#        print "adb -s " + SN + " shell ping -c 3 ping www.baidu.com"
#        print ping1
        
        if ping1.find("0% packet loss") != -1:
            break
        else:
            if m <= 6:                
                print ("can't ping")
                time.sleep(10)
            else:
                print("can't ping in 60s, exit!")
                exit()
                

if __name__ == '__main__':

    for i in range(0,5):
        
        OnlineCheck()
        PingCheck()
        RXCheck()
