#-*- coding: utf-8 -*-

import os,sys,time
reload(sys)
sys.setdefaultencoding('utf-8')

name = '    report_time	      success	   reason		     client_id			 form_vcode	   from_vname	   to_vcode	     to_vname	  download_time '
fn = '111.txt'
tag = 'common/result'

m = 0
n = 0

def logs(str):

    f = open('OTA-2017_12_18_13-00.log','a+')
    if str != '\n':
        f.write(str+"    ")
    else:
        f.write(str)
    f.flush()
    f.close()

def hms(s):

    s1 = int(s)/1000
    a = int(s1/60)
    b = int(s1%60)
    c = a/60
    d = a%60
    if a == 0 :
        logs("%ds"%b)
    if 60 > a > 0 :
        logs("%dm %ds"%(a,b))
    if 1440 > a >= 60:
        logs("%dh %dm %ds"%(c,d,b))
    logs("\n")
    

def elk():

    f = open(fn).readlines()
    for i in range(0,len(f)):
        try:
            #if f[i].find(tag) != -1:
            if f[i].find(tag) != -1 and f[i].find('failure') == -1:            
                t = f[i].split(";")                
                a = t[1].split('[')[1].split(']')[0]
                logs(a)                
                b = t[23].split(':')[1]
                logs(b)                
                c = t[22].split(':')[1].split('"')[1]
                logs(c)                
                d = t[15].split(':')[1].split('"')[1]
                logs(d)                
                e = t[18].split(':')[1]
                logs(e)                
                g = t[19].split(':')[1].split('"')[1]
                logs(g)                
                h = t[24].split(':')[1]
                logs(h)
                j = t[25].split(':')[1].split('"')[1]
                logs(j)
                k = t[16].split(':')[1]
                hms(k)
                global m
                global n
                m = m + int(k)
                n = n + 1                
            else:
                pass
            
        except Exception,e:
            print e
 
    ave = m / n
    logs(u"平均下载时间")
    print("average download time: %dms"%ave)
    hms(ave)


if __name__ == '__main__':

    logs(name)
    logs("\n")
    elk()

            
            
