#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os,time
from datetime import datetime
from useriface import device
from useriface import logger
from useriface import hostpc
from datetime import datetime

#SN = '192.168.40.125:5555'
SN = '0123456789ABCDEF'
testtime = 1001
retry = 100002
retry1 = 100000
dev = device.Device(SN)
pc = hostpc.Host(SN)
log = logger.Logger(__file__)


def CheckConnect(wifiusb):

    connecttype = {'wifi':'wifi','usb':'usb'}

    for w in range(1,retry):

        if wifiusb == 'wifi':
            
            os.popen("adb connect " + SN).read()
 
        adbls = os.popen("adb -s " + SN + " shell ls").read()

        if adbls.find("sdcard") != -1:

            log.info(connecttype[wifiusb] + " adb connect succeeded")

            break
            
        else:

            if w <= retry1:

                log.info(connecttype[wifiusb] + " adb connect fail, retry : %d" %w)
                time.sleep(2)

            else:
                
                log.info(connecttype[wifiusb] + " adb connect fail, exit!")
                exit()        
          

def Remount():

    for items in ['root','remount']:

        for g in range(1,retry):

            item1 = {'remount':'succeeded','root':'adbd is already running as root'}

            item2 = {'remount':'remount succeeded','root':'restarting adbd as root'}
    
            remount = os.popen("adb -s " + SN + " " + items).read()

            if remount.find(item1[items]) != -1 or remount.find(item2[items]) != -1:

                log.info(items + " succeeded")

                time.sleep(2)

                break
            
            else:

                if g <= retry1:

                    log.info(items + " fail, retry : %d" %g)
                    time.sleep(2)    

                else:
                
                    log.info(items + " fail, exit!")
                    exit()


def CheckFile(check,path1='/sdcard/'):
    
    for m in range(1,retry):

        if check == 'mcu_utils':
            
            path1 = '/system/bin/'

        if check == 'stm32':

            path1 = '/cache/DAROS/Recovery/inf/'
       
        pc.adbPush(os.getcwd() + "\\" + check,path1)
        
        pushfile = os.popen("adb -s " + SN + " shell ls " + path1).read()
        
        if pushfile.find(check) != -1:
            
            log.info("already has " + check)
            log.addPass("push " + check + " success.")
            break
        
        else:
            
            if m <= retry1:
                log.info("can't find " + check + " : %d" %m)
                time.sleep(2)
                
            else:
                log.info("can't find " + check + " , exit!")
                log.addFail("push " + check + " fail.")
                exit()


# Push and Check otaipgrade.xml

def CheckXML():

    for l in range(1,retry):
        pc.adbPush('D:\\otaupgrade.xml','/sdcard/pudding/config/')
       
        xml = os.popen("adb -s " + SN + " shell cat /sdcard/pudding/config/otaupgrade.xml").read()
        if xml.find('''value="1"''') != -1:
            log.info("already has otaupgrade.xml")
            break
        else:
            if l <= retry1:
                log.info("can't find otaupgrade.xml: %d" %l)
                time.sleep(2)
            else:
                log.info("can't find otaupgrade.xml, exit!")
                exit()

                
def ChmodUtils():
    
    os.popen("adb -s " + SN + " shell chmod 777 /system/bin/mcu_utils")
    log.info("chmod 777 /system/bin/mcu_utils")


#Send Command MCU

def SendCommand(otaitem,path4='/cache/recovery/command'):

    item5 = {'zigbee':'--update_mcu=/storage/emulated/legacy/update_mcu.bin',
             'rom':'--update_package=/storage/emulated/legacy/update_rom.zip',
             'stm32':'--update_stm32=/cache/DAROS/Recovery/inf/update_stm32.bin',
             'fpga':'--update_fpga=/storage/emulated/legacy/fpga_fea_algo.iea'
             }

    for e1 in range(1,retry):
        os.popen("adb -s " + SN + " shell " +  '"' + "echo " + item5[otaitem] +" > " + path4 + '"')
        log.info("echo " + item5[otaitem] + " > " + path4)
        time.sleep(3)
        commandmcu = os.popen("adb -s " + SN + " shell cat " + path4).read()

        if commandmcu.find(item5[otaitem]) != -1:
            log.info(otaitem + " command send ok")
            break
        else:
            if e1 <= retry1:
                
                log.info(otaitem + " command send fail: %d" %e1)
                time.sleep(2)
            else:
                log.info(otaitem + " command send fail, exit!")
         

#Send MCU in Boot

def CommandBoot():
    os.popen("adb -s " + SN + " shell mcu_utils 112")
    log.info("mcu_utils 112")
    time.sleep(3)



# Reboot recovery

def Recovery():

    log.info("reboot device to recovery")
    dev.recovery()
    
    log.info("sleep 300s")
    time.sleep(300)


# Chech version

def VersionMCU(otastep):

    steps = {'before':'before zigbee update , ','after':'after zigbee update, '}

    for a in range(1,retry):
        
        utils = log.addLogcap('utils.log','adb -s ' + SN + ' shell logcat -v threadtime -s utils')
        os.popen("adb -s " + SN + " shell mcu_utils 92")
        utils.start()
        time.sleep(1)
        utils.startCap()
        time.sleep(1)
        os.popen("adb -s " + SN + " shell mcu_utils 92")
        time.sleep(5)
        utils.stopCap()
        pc.adbPush('utils.log','/sdcard/')

        versionmcu = os.popen("adb -s " + SN + " shell cat //sdcard//utils.log | findstr version").read()
        
        if versionmcu.find("version number is") != -1:

            log.info(steps[otastep] + " zigbee version is: %s" %versionmcu.split(':')[3].split()[4])

            log.info("delete utils.log")
            rmutils = os.popen("adb -s " + SN + " shell rm //sdcard//utils.log")
            delutil = os.popen("del utils.log")
            
            break

        else:

            if a <= retry1:

                log.info("can't find zigbee version: %d" %a)
                time.sleep(2)
            else:
                log.info("can't find zigbee version, exit!")
                exit()


# Chech version

def VersionROM(steps):
    
    versionrom = os.popen("adb -s " + SN + " shell getprop ro.mediatek.version.release").read()
    log.info(steps + " update , rom version is: " + versionrom.split('\r\n')[0])
    


def ResultCheck(otatype):

    logpath = {'rom':'rom_log','zigbee':'mcu_log','stm32':'stm32_log','fpga':'fpga_log'}
    resultslog = {'rom':'script result was [pass]','zigbee':'set persist.sys.upmcu status: 1','stm32':'set persist.sys.upstm32 status: 1','fpga':'set persist.sys.upfgpa status: 1'}

    curtime = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    os.popen("adb -s " + SN + " shell mkdir /sdcard/" + logpath[otatype])
    resultsrom = os.popen("adb -s " + SN + " shell cat /cache/recovery/last_log").read()
    os.popen("adb -s " + SN + " shell cp /cache/recovery/last_log /sdcard/" + logpath[otatype] + "/" + "%s.log" %curtime)
    log.info("cp /cache/recovery/last_log TO /sdcard/" + logpath[otatype] + "/%s.log" %curtime) 

    if resultsrom.find(resultslog[otatype]) != -1:
        log.info(otatype + " update success\n")
    else:
        log.info(otatype + " update fail\n")

def Result_all():

    curtime = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    os.popen("adb -s " + SN + " shell mkdir /sdcard/alllog")
    resultsrom = os.popen("adb -s " + SN + " shell cat /cache/recovery/last_log").read()
    os.popen("adb -s " + SN + " shell cp /cache/recovery/last_log /sdcard/alllog/" + "%s.log" %curtime)
    log.info("cp /cache/recovery/last_log TO /sdcard/alllog" + "/%s.log" %curtime) 

    if resultsrom.find("mcu") != -1:
        if resultsrom.find("E:currentVersion == fileVersion") != -1:
            log.info("no need update zigbee , the version is same")

        elif resultsrom.find("I:start update mcu from -100") != -1:
            log.info("can't find mcu version in recovery")

        else:
            if resultsrom.find("set persist.sys.upmcu status: 0") != -1 or resultsrom.find("result_mcu=failed") != -1:
                log.info("zigbee update fail")
            
            elif resultsrom.find("set persist.sys.upmcu status: 1") != -1 or resultsrom.find("result_mcu=success") != -1:
                log.info("zigbee update sucess")
            
            else:
                log.info("unknow zigbee update log , pls check")
                
    if resultsrom.find("stm32") != -1:
        if resultsrom.find("set persist.sys.upstm32 status: 0") != -1 or resultsrom.find("result_stm32=failed") != -1:
            log.info("stm32 update fail")
            
        elif resultsrom.find("set persist.sys.upstm32 status: 1") != -1 or resultsrom.find("result_stm32=success") != -1:
            log.info("stm32 update sucess")
            
        else:
            log.info("unknow stm32 update log , pls check")
            
    if resultsrom.find("fpga") != -1:
        if resultsrom.find("set persist.sys.upfpga status: 0") != -1 or resultsrom.find("result_fpga=failed") != -1:
            log.info("fpga update fail")
            
        elif resultsrom.find("set persist.sys.upfpga status: 1") != -1 or resultsrom.find("result_fpga=success") != -1:
            log.info("fpga update sucess.")
            
        else:
            log.info("unknow fpga update log , pls check")

    if resultsrom.find("rom") != -1:
        if resultsrom.find("set persist.sys.uprom status: 0") != -1:
            log.info("rom update fail")
            
        elif resultsrom.find("set persist.sys.uprom status: 1") != -1:
            log.info("rom update sucess")
            
        else:
            log.info("unknow rom update log , pls check")
    

def OTA_ALL():

    CheckFile('update_rom.zip')
    CheckFile('mcu_utils')
    ChmodUtils()
    
    VersionROM('before')
    VersionMCU('before')
    
    SendCommand('rom')

    Recovery()
        
    CheckConnect('usb')
    Remount()

    CheckFile('mcu_utils')
    ChmodUtils()
        
    VersionROM('after')
    VersionMCU('after')
    Result_all()
    


def OTArom():

        CheckFile('update_rom.zip')
        VersionROM('before')
        SendCommand('rom')

        Recovery()
        
        CheckConnect('usb')
        Remount()
        
        VersionROM('after')
        
        ResultCheck('zigbee')



def OTAzigbee():

        CheckFile('mcu_utils')
        ChmodUtils()
        VersionMCU('before')
        CheckFile('update_mcu.bin')
        CheckFile('mcu_version.cfg')
        SendCommand('zigbee')
        CommandBoot()
        Recovery()
        CheckConnect('usb')
        Remount()
        VersionMCU('after')
        ResultCheck('zigbee')

def OTAstm32():

        CheckFile('update_stm32.bin','/cache/DAROS/Recovery/inf/')

        SendCommand('stm32')

        Recovery()
        
        CheckConnect('usb')
        Remount()

        ResultCheck('stm32')


def OTAfpga():

        CheckFile('fpga_fea_algo.iea')
        CheckFile('fpga_fea_data.ied')
        CheckFile('fpga_flash_algo.iea')
        CheckFile('fpga_flash_data.ied')
        CheckFile('fpg_version.cfg')
        SendCommand('fpga')
        Recovery()
        CheckConnect('usb')
        Remount()
        ResultCheck('fpga')



            
if __name__ == '__main__':


    curtime = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    log.addLog2file('%s_T1_OTA.log' %curtime)

    CheckConnect('usb')
    Remount()
       
    for p in range(1,testtime):
        
        log.info("======================= testtimes: " + str(p) + " =======================\n")
        
        try:
                        
            OTA_ALL()

        except:

            log.info("\n----- unknown error happened,restart test again -----\n")

            OTA_ALL()
            

        
