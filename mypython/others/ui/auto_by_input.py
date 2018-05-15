# -*- encoding: UTF-8 -*-

import os,time

SN='0123456789ABCDEF'

jarname = raw_input("Please input file name of jar: ")
uipath = raw_input("Please input path of src: ")
packclass = raw_input("Please input the packagename.className: ")

def UiTest():
    
    oldpath = os.getcwd()
    print("old path is: " + oldpath)
    os.chdir(uipath)
    newpath = os.getcwd()
    print("new path is: " + newpath)


    buildxml = os.popen("android create uitest-project -n " + jarname +  " -t 1 -p " + uipath).read()
    print("android create uitest-project -n " + jarname +  " -t 1 -p " + uipath)
    print buildxml
    time.sleep(2)


    antbuild = os.popen("ant build").read()
    print antbuild
    time.sleep(2)

    pushjar = os.popen("adb -s " + SN + " push " + uipath + "/bin/" + jarname + ".jar /data/local/tmp/").read()
    print("adb -s " + SN + " push " + uipath + "/bin/" + jarname + ".jar /data/loacal/tmp/")
    print pushjar
    time.sleep(2)

    print("adb -s " + SN + " shell uiautomator runtest " + jarname + ".jar -c " + packclass + " --nohup")
    runjar = os.popen("adb -s " + SN + " shell uiautomator runtest " + jarname + ".jar -c " + packclass + " --nohup").read()
    print runjar
    time.sleep(2)

def StopUi():

    uikill = raw_input("Input entry key to run kill uiautomator: ")

    print("adb -s " + SN + " shell ps | findstr uiautomator")
    findpid = os.popen("adb -s " + SN + " shell ps | findstr uiautomator").read()
    print findpid

    pidnum = findpid.split()[1]
    time.sleep(2)

    uistop = os.popen("adb -s " + SN + " shell kill " + pidnum).read()

if __name__ == '__main__':

    UiTest()

    

