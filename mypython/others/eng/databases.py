# -*- coding: UTF-8 -*-

import os,sys,time
import multiprocessing
import subprocess
import threading
from datetime import datetime
SN='1011010000200E1B'
ip='192.168.10.214:6666'
#SN='10110000002037C8'
allsize = 289382033
defalut_md5 = 'FDFF8E3F25ACDFC47F55E22627F969D0'

devices = os.popen("adb devices").read()

print devices

print os.popen("adb -s " + ip + " shell sqlite3 /data/data/com.android.providers.settings/databases/settings.db").read()


time.sleep(3)

os.popen("select * from system;")
