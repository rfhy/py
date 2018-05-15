#-*- encoding: UTF-8 -*-
import sys
import os,time
from datetime import datetime
reload(sys)
sys.setdefaultencoding( "utf-8" )

a = []
sn = '4001000C00000136'

def logfile(str):
    t = datetime.now().strftime('%Y%m%d_%H%M%S')
    f = open(u'smartac_time_D013C01.txt','a+')
    f.write(t + " " + str + "\n")
    f.flush()
    f.close()
    print(t + " " + str)

def main():

    logfile("reboot device")
    t1 = time.time()
    os.popen("adb -s " + sn + " shell reboot")
    time.sleep(3)
    os.popen("adb -s " + sn + " wait-for-device")
    logfile("find device")
    
    for i in  range(0,1000):
        watchdog = os.popen("adb -s " + sn + " shell ps | findstr /c:\"com.roobo.watchdog\"").read()
        if watchdog.find("com.roobo.watchdog")!= -1:
            logfile("find com.roobo.watchdog")
            
            for t in range(0,1000):
                smartac = os.popen("adb -s " + sn + " shell ps | findstr /c:\"com.roobo.ioe.smartac.midea\"").read()
                if smartac.find("com.roobo.ioe.smartac.midea")!= -1:
                    logfile("find com.roobo.ioe.smartac.midea")
                    t2 = time.time()
                    t3 = t2 - t1
                    a.append(t3)
                    logfile("from reboot to smartac: %.2f s"%t3)
                    ave = sum(a)/float(len(a))
                    logfile("average reboot time is: %.2f s\n"%ave)
                    break
                else:
                    time.sleep(0.5)
            break
        else:
            time.sleep(0.5)
            
if __name__ == '__main__':

    for i in range(1,1001):

        logfile("========= reboot time: %d"%i)

        main()



        
