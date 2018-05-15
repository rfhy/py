# -*- encoding: UTF-8 -*-

from useriface import device
from useriface import hostpc
from useriface import logger

import time,os


SN='0123456789ABCDEF'
IP='192.168.40.185'

device = device.Device(SN)
daros = device.daros.connect(IP)
log = logger.Logger(__file__)
pc = hostpc.Host(SN)
log.addLog2file('daros.txt')


def DisableApks(path='/system/priv-app/'):

    for apks in ['RooboBoot','RooboDarosService']:

        findapk = os.popen("adb -s " + SN + " shell ls " + path + apks + "/").read()

        if findapk.find(apks + ".apk") != -1:

            os.popen("adb -s " + SN + " shell mv " + path + apks + "/" + apks + ".apk " + path + apks + "/" + apks)

            log.info("mv apks: " + path + apks + "/" + apks + ".apk")

            log.info("reboot and wait 60s")
            os.popen("adb -s " + SN + " shell reboot")
            time.sleep(60)

        else:

            log.info("no apks: " + path + apks + "/" + apks + ".apk")


def InstallAPK():

    checkapk = os.popen("adb -s " + SN + " shell ls /data/app/").read()

    if checkapk.find("com.roobo.testt1api-1") != -1:

        log.info("already install daros test apk")

    else:

        log.info("install test apk")
        os.popen("adb -s " + SN + " install D:\\automation\\framework\\libs\\t1daros.apk")
        time.sleep(2)

        log.info("start test apk")
        os.popen("adb -s " + SN + " shell am startservice -a com.roobo.testt1api.mservice")
        time.sleep(2)
    

def Remount():

    for items in ['root','remount']:

        for g in range(1,10002):

            item1 = {'remount':'succeeded','root':'adbd is already running as root'}

            item2 = {'remount':'remount succeeded','root':'restarting adbd as root'}
    
            remount = os.popen("adb -s " + SN + " " + items).read()

            if remount.find(item1[items]) != -1 or remount.find(item2[items]) != -1:

                log.info(items + " succeeded")

                break
            
            else:

                if g <= 10000:

                    log.info(items + " fail, retry : %d" %g)
                    time.sleep(2)    

                else:
                
                    log.info(items + " fail, exit!")
                    exit()

def CheckLED():
    

    log.info("open all led")
    print daros.LEDFUN_Async_Start(True, True, True, True, True)
    time.sleep(2)

    log.info("home led")
    print daros.LEDFUN_Async_Start(True, False, False, False, False)
    time.sleep(2)

    log.info("right rear")
    print daros.LEDFUN_Async_Start(False, True, False, False, False)
    time.sleep(2)

    log.info("left rear")
    print daros.LEDFUN_Async_Start(False, False, True, False, False)
    time.sleep(2)

    log.info("right front")
    print daros.LEDFUN_Async_Start(False, False, False, True, False)
    time.sleep(2)

    log.info("left front")
    print daros.LEDFUN_Async_Start(False, False, False, False, True)
    time.sleep(2)

    log.info("close all led")
    print daros.LEDFUN_Async_Start(False, False, False, False, False)
    time.sleep(2)


if __name__ == '__main__':

    Remount()

    DisableApks()
                        
    InstallAPK()
    CheckLED()



