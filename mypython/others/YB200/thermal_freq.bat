:a
adb shell cat /sys/class/thermal/thermal_zone*/temp >> temp.log
adb shell cat /sys/class/thermal/thermal_zone*/temp
adb shell cat /sys/devices/system/cpu/cpu*/cpufreq/cpuinfo_cur_freq >> cpu.log
adb shell cat /sys/devices/system/cpu/cpu*/cpufreq/cpuinfo_cur_freq
@ping 127.1.1.0 -n 3 >ping.txt
@del ping.txt
@goto a