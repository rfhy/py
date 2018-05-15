# -*- coding: UTF-8 -*-

import os,time,sys
from useriface import device
from useriface import hostpc
from useriface import logger

testtime = 1000
SN = '0123456789ABCDEF'
dev = device.Device(SN)
pc = hostpc.Host(SN)
ui = dev.uidevice
log = logger.Logger(__file__)
log.addLog2file('orientation.log')


def Reset():

   ui.orientation = 'n'



if __name__ == '__main__':

    for i in range(1,testtime):

        log.info("============testtimes: %d ============" %i)

        Reset()

else:

    for i in range(1,testtime):

        log.info("============testtimes: %d ============" %i)

        Reset()
