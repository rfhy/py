# -*- encoding: UTF-8 -*-

import os,time

SN='0123456789ABCDEF'


lirun = open("setup.txt","r")

#alltext = lirun.read()
#print alltext


for line in lirun.readlines()[0:1]:

    print line

    uipath = line.split('path:')[1].strip('\r\n\t')

    print uipath

    

'''
uipath = alltext.split('\n')[0].split('path:')[1]
classname = alltext.split('\n')[1].split('class:')[1]
packagename = alltext.split('\n')[2].split('package:')[1]
packageclass = packagename + "." + classname
jarname = alltext.split('\n')[3].split('jarname:')[1]
'''

'''
setup.txt
path:H:/Tools/android_Studio/eclipse_work/CheckUFT8BOM
class:Utf8Class
package:utf8package
jarname:testfile
'''
