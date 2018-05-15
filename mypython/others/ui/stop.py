# -*- encoding: UTF-8 -*-

import os,time

SN='0123456789ABCDEF'

uikill = raw_input("Input entry key to run kill uiautomator: ")
print("adb -s " + SN + " shell ps | findstr uiautomator")
findpid = os.popen("adb -s " + SN + " shell ps | findstr uiautomator").read()
print findpid

pidnum = findpid.split()[1]
time.sleep(2)

uistop = os.popen("adb -s " + SN + " shell kill " + pidnum).read()

