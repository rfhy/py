# -*- coding: UTF-8 -*-

import os,sys,time
import multiprocessing
import subprocess
import threading
from datetime import datetime
SN='10110000002037C8'   

#curtime=datetime.now().strftime('%Y%m%d_%H%M%S')

def logs(str):

    curtime1=datetime.now().strftime('%Y%m%d %H:%M:%S')

    #lirun=open(curtime + '_ota.log','a+')
    lirun=open('alls_ota.log','a+')
    lirun.write(curtime1 + " " + str + "\n")
    lirun.flush()
    lirun.close()
    print(curtime1 + " "  + str)


def waring():

    player = r'"C:\Program Files (x86)\Windows Media Player\wmplayer.exe"'

    music = r"D:\Roobo\Project\dingdong.wav"

    os.popen(player + " " + music)

def watchplayer(name='wmplayer.exe'):

    for i in range(0,10000000):

        kills = os.popen("tasklist | findstr " + name).read()
        if kills.find(name) != -1:
            time.sleep(5)
            pid_player = kills.split()[1]
            print("wmplayer pid is: " + pid_player)
            os.popen("taskkill /PID " + pid_player + " -f")
            time.sleep(2)
            check = os.popen("tasklist | findstr " + name).read()
            if check.find(name) == -1:
                print("kill " + name + " sucess.")
        time.sleep(30)

if __name__ == '__main__':

    m1 = multiprocessing.Process(target=watchplayer,args=('wmplayer.exe',))
    m1.start()

    for i in range(0,10):
        time.sleep(10)
        waring()
        time.sleep(3)

        print "===================="
