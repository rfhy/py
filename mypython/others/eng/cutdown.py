# -*- coding: UTF-8 -*-

import os,time,sys

deadline = 1519466400


def two(i):

    if i / 10 == 0 :
        p = '0' + str(i)
    else:
        p = str(i)

    return str(p)
    

def mytime():

    t1 = time.time()
    n = deadline - int(t1)
    
    #if n % 600 == 0:
        #print("count down 10 min.")

    #GMT+8
    a1 = n % 60 #秒
    b1 = n / 60 % 60 #分钟
    c1 = (n / 3600) % 24 #小时
    e1 = (n / 3600) / 24 #总天数
    #print t1
    print("*******************************")
    print("* count down: %sd %sh %sm %ss *" %(two(e1),two(c1),two(b1),two(a1)))
    print("*******************************")

if __name__ == '__main__':

    os.system("cls")
    while(True):
        mytime()
        time.sleep(0.955)
        os.system("cls")
            
