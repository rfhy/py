#encoding:utf-8

import os,sys
import re

r1 = '0.5.0.19_result.txt'
r2 = '0.5.0.19_result_details_fail.txt'

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
                
                for i in range(0,100):
                    count1 = len(re.findall("position " + str(i) + ",failed,0,1", f0))
                    if count1 > 0:
                        logs(r2,item + ": position " +str(i) + " pass times: %d/10"%(10-count1))

                logs(r2,"\n\n")



if __name__ == '__main__':

    result('.')
