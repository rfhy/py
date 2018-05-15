# -*- coding: UTF-8 -8-

from sendemail_attach_import import Sendmail
from datetime import datetime
import os

curtime0 = datetime.now().strftime('%Y%m%d_%H%M%S')

def Logfile(str):
    
    global file1

    file1 = curtime0 + "_sendemail.log"
   
    lirun = open(file1,"a+")

    print(str)

    lirun.write(str + "\n")
   
    lirun.flush()

    lirun.close()

def justtest():

    for i in range(1,10):

        Logfile("testtime: " + str(i))

    if i == 9:

        result = 'ok'
    else:

        result = 'nok'

    global nr
    nr = 'just test email test results : ' + result

if __name__ == '__main__':

    justtest()    

    Sendmail(nr,'test subject',os.getcwd() + "\\" + file1)

        
