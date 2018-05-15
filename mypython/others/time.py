# -*- coding: UTF-8 -*-

import os
#SN='1011010000200E1B'
#SN='192.168.10.214:6666'

def mytime():
    
    #s4 = os.popen("adb -s " + SN + " shell getprop ro.runtime.firstboot").read()

    #n= int(s4[0:10])

    n = input("pls input time: ")

    #GMT+8
    a1 = (n + 8*3600) % 60 #秒
    b1 = (n + 8*3600) / 60 % 60 #分钟
    c1 = (n / 3600 + 8) % 24 #小时
    e1 = (n / 3600 + 8) / 24 #总天数

    arr = [0]#1970-2050每年多少天
    arr1 = []#每年距离1970的总天数
    arr2 = []#1970-2050每年二月多少天
    
    for i in range(1970,9999):
        
        if i % 100 == 0:
            
            if i % 400 == 0:
                
                arr.append(366)
                arr2.append(29)
                
            else:
                arr.append(365)
                arr2.append(28)
                
        if i % 100 != 0:
            
            if i % 4 == 0:
                
                arr.append(366)
                arr2.append(29)
                
            else:
                
                arr.append(365)
                arr2.append(28)

    
    for i2 in range(0,9999-1970):
        if i2 == 0:
            arr1.append(0)
        if i2 > 0:
            arr1.append(int(arr1[-1]) + int(arr[i2]))

    g = 0
    while g <= 9999-1970:

        if int(arr1[g]) <= e1 < int(arr1[g+1]):

            f = g + 1970    #确定是哪一年        
            break
        
        g += 1
    f1 = e1 - int(arr1[g])#当年全部天数
        
    arr3 = [31] + [arr2[g]] +[31,30,31,30,31,31,30,31,30,31,31]#当年各月天数
    arr4 = []#每个月距离当年一月一日的天数和

    
    for i3 in range(0,13):
        if i3 == 0:
            arr4.append(0)
        if i3 > 0:
            arr4.append(int(arr4[-1]) + int(arr3[i3-1]))

    i4 = 0
    while i4 < 13:

        if int(arr4[i4]) <= f1 < int(arr4[i4+1]):

            g1 = i4 + 1 #确定是哪一月
            
            
            break
        
        i4 += 1

    h1 = f1 - int(arr4[i4]) + 1 #确定是哪一天

    #print("GMT+0: %d-%d-%d %d:%d:%d" %(f,g1,h1,c1,b1,a1))
    #GMT+8
    print("GMT+8: %d-%d-%d %d:%d:%d" %(f,g1,h1,c1,b1,a1))


def untime():

    n = input("pls input a num , format like 20120202090101 ,max:20501231235959: ")

    if len(str(n)) == 14 and n >= 19700101000000 and n <= 20501231235959:
        year = int(str(n)[0:4])
        month = int(str(n)[4:6])
        s3 = int(str(n)[6:8])
        s4 = int(str(n)[8:10])
        s5 = int(str(n)[10:12])
        s6 = int(str(n)[12:14])

    if len(str(n)) != 14:
        print("need 14 number!")
        exit()
        
    if n < 19700101000000 and n >= 20501231235959:

        print("out of range")
        exit()

    arr = [0]#1970-当年每年多少天
    arr1 = []#当年一月一日距离1970年一月一日多少天
    arr2 = []#当年二月多少天
    
    for i in range(1970,year+1):        
        if i % 100 == 0:
            
            if i % 400 == 0:
                
                arr.append(366)
                arr2.append(29)
                
            else:
                arr.append(365)
                arr2.append(28)
                
        if i % 100 != 0:
            
            if i % 4 == 0:
                
                arr.append(366)
                arr2.append(29)
                
            else:
                
                arr.append(365)
                arr2.append(28)

    for i2 in range(0,year-1970+1):
        if i2 == 0:
            arr1.append(0)
        if i2 > 0:
            arr1.append(int(arr1[-1]) + int(arr[i2]))

    s1 =  arr1[i2]#当年之前所有天数

    arr3 = [31] + [arr2[year-1970]] +[31,30,31,30,31,31,30,31,30,31]#当年各月天数
    arr4 = []#当月距离当年一月一日的天数和

    for i3 in range(0,12):
        if i3 == 0:
            arr4.append(0)
        if i3 > 0:
            arr4.append(int(arr4[-1]) + int(arr3[i3-1]))
    s2 = arr4[month-1]#当月之前，今年所有天数

    s0 = (s1 + s2 + s3 -1)*24*3600 + s4*3600 + s5*60 + s6 - 28800
    print s0
 

if __name__ == '__main__':

    while(True):
        try:

            mytime()
            break
        
        except Exception,e:

            print e

    while(True):
        try:

            untime()
            break
        
        except Exception,e:

            print e
            
