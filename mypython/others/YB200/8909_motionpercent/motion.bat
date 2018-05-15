chcp 936
@adb wait-for-device
@adb shell logcat -v time | motion.py
pause