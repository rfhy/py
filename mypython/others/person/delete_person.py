# -*- coding: UTF-8 -*-

import os,sys,time
from datetime import datetime
import random

os.popen("copy person_backup.txt person.txt")
os.popen("del name.txt")
time.sleep(1)

def addper(name):

        f = open("person.txt","a+")
        f.write("\n" + name)
        f.flush()
        f.close()

def delper(name):

        f1 = open("person.txt")
        f2 = f1.readlines()
        #print f2
        f1.close()
        f3 = open("person.txt","w+")
        for i in range(len(f2)):
            if name == f2[i] or name == f2[i].strip('\n'):
                f2[i]=''
                #print f2
        f3.writelines(f2)
        f3.flush()
        f3.close()

def select():
        reload(sys)
        sys.setdefaultencoding('gbk')
        w = [u'****** 三等奖名单 ******',u'****** 二等奖名单 ******',u'****** 一等奖名单 ******',u'****** 特别奖名单 ******']
        
        i2 = 4
        
        while(i2):

                print w[4-i2]
                f4 = open("name.txt","a+")
                f4.write(w[4-i2] + "\n")
                f4.flush()
                
                try:
                        n = input("quantity:")
                        
                        f8 = open("person.txt").readlines()
                            
                        if n > len(f8):
                                print("input number is to big, only %d person" %len(f8))
                                
                        if n < len(f8):
                                i2 -= 1
                                for i in range(n):

                                        f2 = open("person.txt").readlines()
                                        name1 = f2[random.randrange(len(f2))]
                                        print name1
                    
                                        f4.write(name1 + "\n")                        
                                        f4.flush()
                    
                                        delper(name1)
                                
                except Exception,e:

                        print e
                        
                
                f4.close()
                #raw_input(u"按回车键继续")
                    
            
if __name__ == '__main__':


        while 1:
                
                name = raw_input("pls input delete person name,input q to exit: ")
                if name == 'q':
                        exit()
                else:
                        delper(name)




            
