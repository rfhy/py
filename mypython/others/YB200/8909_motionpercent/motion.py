#-*- encoding: UTF-8 -*-
import sys
import os
reload(sys)
sys.setdefaultencoding( "utf-8" )


def logfile(str):

    f = open(u'MotionPercant1122_led.txt','a+')
    f.write(str+"\n")
    f.flush()
    f.close()
    print(str)

def test():
    
    logfile(u"\n夜间入侵:\n")
    for line in sys.stdin:
        #if line.find('motionPercent=') != -1:
        if line.find('motionPercent') != -1 and line.find('SecurityEngine') != -1:
            '''
            log = line.split('}')[0].split(',')[-4]
            s = int(log.split('=')[1])
            time = line.split('D/GestureControlState')[0]

            '''
            log = line.split('):')[1]
            m = log.split()[-2]
            s = int(log.split()[-1])
            time = line.split('D/SecurityEngine')[0]
            
            result = ''
            if s >= 0:
                #result = u'  大于变化范围，触发警报'
                logfile(time + m + " : " + str(s) + result)


if __name__ == '__main__':

    test()
