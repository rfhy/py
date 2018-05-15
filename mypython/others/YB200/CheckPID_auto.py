# -*- coding: UTF-8 -*-

import os,sys,time
from datetime import datetime


SN='0123456789ABCDEF'
testtimes = 10

def logfile(str):
    
    time0 = datetime.now().strftime('%y-%m-%d %H:%M:%S')
    lirun = open("checkpid.log","a+")
    lirun.write(time0 + " " + str + "\n")
    lirun.flush()
    print(time0 + " " + str)
    lirun.close()

def PidCheck(pidnum):
    
    pids = []
    changes =[]

    for i in range(1,testtimes):

        gallery = os.popen("adb -s " + SN + " shell ps | findstr " + pidnum).read()

        if gallery.find(pidnum) != -1:
            a =  gallery.split().index(pidnum)
        
            if a != -1:

                str1 = gallery.split()[a -7]

                pids.append(str1)

                time.sleep(3)

                if len(pids) == 1 and len(changes) == 0:

                    logfile("Before Test " + pidnum + " pid is: " + str1 + "\n")

                    changes.append(str1)

                if len(pids) >=2:

                    if pids[-1] == pids[-2]:

                        if i == 2:

                            logfile("testing , please wait...\n")
            
                    else:
                
                        logfile("pid is change , now " + pidnum + " pid is: " + str1 + "\n")

                        changes.append(str1)
            else:

                logfile("can't find process: " + pidnum)
                time.sleep(3)
        
        else:

            logfile("Can't find process: " + pidnum)
            time.sleep(3)

    if len(changes) == 0:

        logfile("\nit seemed can't fimd " + pidnum)
    
    if len(changes) == 1:

        logfile("\nafter test, " + pidnum + " pid not change")

    if len(changes) > 1:

        count = len(changes) - 1

        logfile("after test, " + pidnum + " pid change: %d times\nall pids are:" %count)

        print changes

        lirun = open("checkpid.log","a+")
        for items in changes:
            lirun.write(str(items) + ",")
            lirun.flush()
        lirun.close()



if __name__ == '__main__':
    

        PidCheck('com.android.gallery3d')



