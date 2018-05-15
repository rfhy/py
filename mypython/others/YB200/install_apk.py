# -*- coding: UTF-8 -*-

import os

def Install(filespath):    

    for items in os.listdir(filespath):

        curitems = filespath + "/" + items

        if os.path.isfile(curitems):

            if os.path.splitext(curitems)[1] == '.apk':
            
                print("start install " + curitems + " :\n")

                os.system("adb install " + curitems)
                
            else:

                print(curitems + " is not apk\n")

        elif os.path.isdir(curitems):

            print(curitems + " is a folder\n")

            Install(curitems)

 

if __name__ == '__main__':

    Install('.')
        
