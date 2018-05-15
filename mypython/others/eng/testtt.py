#! /usr/bin/env python
#coding=utf-8

import os

sn = '101300000020114B'
s = datetime.now().strftime('%Y%m%d_%H%M%S')

def test():   

    os.popen("adb -s " + sn + " shell \"logcat -v time -s NetSender | grep question\" > " + s +"_shiyin.log")

def test1():

    f = open(s + "_shiyin.log")

    d = f.readlines()

    

 
if __name__ == '__main__':

    test1()
