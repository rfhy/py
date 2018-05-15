# -*- coding: UTF-8 -*-


import wx
import os,sys,time

global deadline
n = 20180224180000


def apps():
    
    app = wx.App()
        
    frame = wx.Frame(parent=None,title='Go home time cut down')
    frame.Show()

    Button1 = wx.Button(frame,label=dates(),pos=(5,5),size=(192,25))

    Button2 = wx.Button(frame,label='Left time:  ' + showtime() + '    ',pos=(5,35),size=(192,25))

    Button3 = wx.Button(frame,-1,label='reset',pos=(200,5),size=(70,25))

    Button4 = wx.Button(frame,label='refresh',pos=(200,35),size=(70,25))

    app.MainLoop()

    #Button3.Bind(wx.EVT_BUTTON,ref(),Button3)


def dates():
    
    year = str(n)[0:4]
    month = str(n)[4:6]
    day = str(n)[6:8]
    hour = str(n)[8:10]
    mins = str(n)[10:12]
    secs = str(n)[12:14]

    dates = year + '-' + month + '-' + day + ' ' + hour + ':' + mins + ':' + secs
    return 'Deadline:  ' + dates


def showtime():

    #t1 = time.time()
    
    while(True):
        n1 = int(untime(n)) - ref()
        a1 = n1 % 60 #秒
        b1 = n1 / 60 % 60 #分钟
        c1 = (n1 / 3600) % 24 #小时
        e1 = (n1 / 3600) / 24 #总天数

        return "%dd %dh %dm %ds" %(e1,c1,b1,a1)

def ref():

    global t1 

    t1 = time.time()

    return t1


def untime(n):

    #n = input("pls input a num , format like 20120202090101 ,max:20501231235959: ")

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

    global deadline

    deadline = (s1 + s2 + s3 -1)*24*3600 + s4*3600 + s5*60 + s6 - 28800
    #print deadline
    return str(deadline)
 
    

if __name__ == '__main__':


    apps()
