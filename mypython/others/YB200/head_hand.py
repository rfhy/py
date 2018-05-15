#-*- encoding: utf-8 -*-

import os,sys,time
reload(sys)
sys.setdefaultencoding('utf-8')

fn = 'head_hand4.log'
tag = 'headCount=1'
tag2= 'hasHand=1'

n = 0
m = 0

def logfile(str):

    f = open(u'手掌头肩比_5m.txt','a+')
    f.write(str+"\n")
    f.flush()
    f.close()
    print(str)
   

def bfb():

    f = open(fn).readlines()
    for i in range(0,len(f)):
        try:            
            if f[i].find(tag) != -1 and f[i].find(tag2) != -1:            
                a = f[i].split('rectHand=Rect(')[1].split(')')[0]
                b = a.split(',')
                c = int(b[0])
                d = int(b[1].split()[-1])
                t = d - c
           
                a1 = f[i].split('rectHeads=[Rect(')[1].split(')')[0]
                b1 = a1.split(',')
                c1 = int(b1[0])
                d1 = int(b1[1].split()[-1])
                t1 = d1 - c1
                logfile("hand:%d head:%d"%(t,t1))

                s = float(t)/t1
                logfile("percent: %.3f\n"%s)
                global n,m
                n = s + n
                m = m + 1

            else:
                pass

                #print("--------------------")
            
        except Exception,e:
            print e

    ave = float(n)/m
    logfile("ave percent: %.3f\n"%ave)

if __name__ == '__main__':

    bfb()

            
            
