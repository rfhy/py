adb push D:\config\eng\otaupgrade.xml /mnt/sdcard/pudding/config
adb shell cat /mnt/sdcard/pudding/config/otaupgrade.xml
pause
adb reboot
pause