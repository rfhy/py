#-*- coding: UTF-8 -*-
import sys,time
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By

def video():
	device=MonkeyRunner.waitForConnection(6,'ZX1C622884')
	logFile = open("c:\\SNAPSHOT\\monkeyrunner_log_test_videotest.txt","w+")


	if not device:
		print("Please connect a device to start!")
		logFile.write("Please connect a device to start!\n")
	 
	else:
		print("Device Connected successfully!")
		logFile.write("Device Connected successfully!\n")

	count=0
	for i in range(1):
		date = time.strftime('%Y-%m-%d_%H-%M-%S')
		print(date+' start com.roobo.pudding')
		logFile.write(date+" start com.roobo.pudding\n")
		device.startActivity(component='com.roobo.pudding/.activity.SplashActivity')
		print('test started')
		logFile.write("test started\n")
		MonkeyRunner.sleep(7) 
		device.touch(366,1042,"DOWN_AND_UP")
		print("connect video")
		MonkeyRunner.sleep(20)
		logFile.write(date+" Connect shi pin! \n")
		current_screen1=device.takeSnapshot()
		current_screen1.writeToFile('c:\\SNAPSHOT\\current_screen1.png','png')
		MonkeyRunner.sleep(2) 
		pic=current_screen1.getSubImage((269,655,183,176))
		logFile.write(date+" Snapshot screen! \n")
		device.touch(353,722,"DOWN_AND_UP")
		print("Click remote call")
		logFile.write("Click remote call\n")
		MonkeyRunner.sleep(7)
		current_screen2=device.takeSnapshot()
		current_screen2.writeToFile('c:\\SNAPSHOT\\current_screen2.png','png')
		MonkeyRunner.sleep(2) 
		newpic=current_screen2.getSubImage((269,655,183,176))
		logFile.write(date+" Snapshot screen! \n")
		result=str(newpic.sameAs(pic,1.0))
		print result
		if result=='False':
			logFile.write("Video connect successfully\n")
			#return True
		else:
			logFile.write("Video connect failed\n")
			#return False
		count=count+1
		print(str(count))
		device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(2)    
		device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(1)

video()	
	 

		


		

		


		


