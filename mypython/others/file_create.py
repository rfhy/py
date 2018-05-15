# -*- coding: UTF-8 -*-

import os,time,sys

def CreateFile():

    print("\n1 : 1M.txt")
    print("2 : 10M.txt")
    print("3 : 100M.txt")
    print("4 : 500M.txt")
    print("5 : 1G.txt")
    print("6 : 3G.txt")
    print("7 : 5G.txt\n")
    
    while(1):

        try:
        
            n = raw_input("please select 1,2,3,4,5,6,7 : ")
    
            fn = {'1':'1M.txt','2':'10M.txt','3':'100M.txt','4':'500M.txt','5':'1G.txt','6':'3G.txt','7':'5G.txt'}
            fs = {'1M.txt':'1048576','10M.txt':'10485760','100M.txt':'104857600','500M.txt':'524288000','1G.txt':'1073741824','3G.txt':'3221225472','5G.txt':'5368709120'}

            mid = fn[n]

            print("\n" + mid + " is creating, please wait ...")

            os.popen("fsutil file createnew " + mid + " " + fs[mid])

            print("\ncreate "+ mid + " in " + os.getcwd() + " OK.")

            break
        
        except:
            
            print("\ninput type is wrong!\nselect again!\n")


if __name__ =='__main__':

    CreateFile()

