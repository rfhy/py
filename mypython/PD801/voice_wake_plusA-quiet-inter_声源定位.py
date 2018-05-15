#coding=utf-8
import os,time,glob
from voice_pdsa import PDSA_HD_WAKE
from voice_pdsa import PDSA_SOFT_WAKE
import os.path
from useriface import device
from datetime import datetime
import useriface.device
curtime=datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

device_list='1510000100000040'

from useriface import device
from useriface import logger
testtime=2
pa = "D:\\lirun\\py\\audio_angel\\py\\"

log = logger.Logger(__file__)
lgcxdish =log.addLogcap(pa + "log\\cxdish.log", "adb -s "+device_list+" shell logcat -v time -s CXDISH ")
lgcall =log.addLogcap(pa + "log\\logcat.log", "adb -s "+device_list+" shell logcat -v time -s Dispatcher")
def myprint(str,logname='angle.txt'):
    logs=open(pa + 'output\\' + curtime+logname,'a+')
    logs.write(str + "\n")
    logs.flush()
    logs.close()
    print(str)

def angle():
    angle = os.popen("adb -s %s shell cat /sys/class/pwm_moto/pwm"%device_list).read().split('\r\n')[0]
    res = angle.split(",")
    if int(res[0]) in range(-15,16):
        res1 = 'pass'
    else:
        res1 = 'fail'
    myprint("after wake,angle: %s  result: %s"%(angle,res1))

def moto(a,s):
    os.popen("adb -s %s shell \"echo %s,%s > /sys/class/pwm_moto/pwm\""%(device_list,a,s))
    myprint("moto device to angel: %s\n"%a)
    time.sleep(3.5)
    
def test_hd_wake(i): 
    num=str(i)
    curtime2=datetime.now().strftime('%m_%d_%H_%M_%S')
    pathL=pa+'log\\'+curtime2
    #update threshold value
    d = PDSA_HD_WAKE('adb -s '+device_list+' shell "logcat -c;logcat -v time -s Dispatcher | grep RokidWakeupTranslator', "output\\"+curtime+'angle.txt', 5)
    d.start()
    pm = pa+"music\\"
    if os.path.exists(pa + 'result\\'+num):
        myprint("file exit")
    else:
        os.mkdir(pa + 'result\\'+num+'\\')
    pathE=pa + 'result\\'+num+'\\'+curtime2

    songs=['kbkb.wav']
    volume=['11500']
    exl = ['conbow.xlsx']
    for an in ['0','-30','30','-45','45','-90','90','-150','150']:
        myprint("******* test angel: %s"%an)
        for i in range(0,len(exl)):
            d.setExcel(pathE+exl[i])
            os.system('nircmd setsysvolume '+volume[i])
            for j in range(1,101):
                myprint("==================== test wake up time: "+str(j))
                d.playSound(pm+songs[i])
                time.sleep(4.5)
                angle()
                moto(an,1)
    time.sleep(1)
    d.stop()
   
    
if __name__ == '__main__':
    dev =device.Device(device_list)
    lgcxdish.start()
    lgcall.start()
    lgcall.startCap()
    for y in range(1,testtime):
        myprint("================= " + curtime + " ; testtimes: " + str(y) + " =================")
        dev.startActivity(component='com.android.music/.MediaPlaybackActivity')
        test_hd_wake(y)
    lgcall.stopCap()
