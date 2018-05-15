#encoding:utf-8

import os,sys,time
from lirun import logg as logs

fn = '2018_05_07_10_14_56angle.txt'
f = open(fn).read()

def num(str,n):
    a = 0
    for i in range(len(str)):
        if str[i] <= n:
            a += 1
    logs("<= %d count: %d"%(n,a))
    
def result():
    re = f.split('******* test angel:')
    for i in range(1,len(re)):
        a1 = []
        an = re[i].split('\n')[0]
        logs("test angle is : %s\n"%an)
        moto = re[i].split("after wake,angle:")
        for j in range(1,len(moto)):
            mo = int(moto[j].split(',')[0].strip())
            a1.append(abs(mo))
        print(a1)
        num(a1,5)
        num(a1,10)
        num(a1,15)
        num(a1,20)
        num(a1,25)
        num(a1,30)
        num(a1,35)
        num(a1,40)
        num(a1,45)
        num(a1,50)
        num(a1,55)
        num(a1,60)
        num(a1,65)
        num(a1,70)
        num(a1,75)
        num(a1,80)
        num(a1,150)
        
        ave = float(sum(a1))/len(a1)
        logs("average deviation: %.2f\n"%ave)
                 
            
if __name__ == '__main__':
    result()
