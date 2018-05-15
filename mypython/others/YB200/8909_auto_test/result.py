#encoding:utf-8

import os,sys
import re

r1 = '0.5.0.19_result.txt'
r2 = '0.5.0.19_result_details.txt'

def logs(fn,str):
    f = open(fn,'a+')
    f.write(str + "\n")
    f.flush()
    f.close()
    print(str)

def result(p):

    g = os.walk(p)
    for path,d,filelist in g:        
        for filename in filelist:         
            if filename.endswith('result'):             
                item  = os.path.join(path, filename)
                f0 = open(item,'r').read()
                f1 = open(item).readlines()
                a = 0
                b = 0
                c = 0
                
                for i in range(0,100):
                    count =  len(re.findall("position " + str(i) + ",failed", f0))
                    count1 = len(re.findall("position " + str(i) + ",failed,0,1", f0))
                    if count > 0:
                        logs(r2,item + ": position " +str(i) + " fail times: %d , 0: %d , >1: %d"%(count,count1,count - count1))
                        a = a + count
                        b = b + count1
                        c = a - b 

                avg = 1 - float(a)/len(f1)
                avg1 = float(b)/len(f1)
                avg2 = float(c)/len(f1)
                logs(r1,item + " average:   %.2f%% , 0 times percent: %.2f%%"%(avg*100,avg1*100))
                logs(r2,"\n======= " + item + " average: %.2f%%\n\n"%(avg*100))


if __name__ == '__main__':

    result('.')
