# -*- coding: UTF-8 -*-

import os,sys,time
from datetime import datetime
import random

os.popen("copy person_backup.txt person.txt")
os.popen("del name.txt")
time.sleep(1)

def addper(name):

        f = open("person.txt","a+")
        f.write(name + "\n")
        f.flush()
        f.close()

def delper(name):

        f1 = open("person.txt")
        f2 = f1.readlines()
        #print f2
        f1.close()
        f3 = open("person.txt","w+")
        for i in range(len(f2)):
            if name == f2[i]:
                f2[i]=''
                #print f2
        f3.writelines(f2)
        f3.flush()
        f3.close()

def select():
        reload(sys)
        sys.setdefaultencoding('gbk')
        w = [u'三等奖名单：',u'二等奖名单：',u'一等奖名单：',u'特别奖名单：']
        
        for i2 in range(len(w)):
                print w[i2]
                f4 = open("name.txt","a+")
                f4.write(w[i2] + "\n")
                f4.flush()

                n = input("quantity:")
                
                for i in range(0,n):
                    f1 = open("person.txt","a+")
                    f2 = f1.readlines()
                    f1.close()
                    name1 = f2[random.randrange(len(f2))]
                    print name1
                    
                    f4.write(name1)                        
                    f4.flush()
                    
                    delper(name1)
                
                f4.close()
                #raw_input(u"按回车键继续")
        
                    
            
if __name__ == '__main__':

        select()


            
