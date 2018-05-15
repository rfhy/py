import sys
import subprocess

class adb(object):
    def getCmdLines(cmd):
        ret = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False).stdout.readlines();
        results = [ result.decode('utf-8').strip() for result in ret ]
        return results

    def devices():
        lines = adb.getCmdLines("adb devices") 
        print(len(lines))
        results = []
        if (lines[0].find("List of devices attached") != -1):
            for index in range(1, len(lines)):
                fields = (lines[index]).split()
                if (len(fields) > 1):
                    results.append(str(fields[0]))
        return results

    def execute_cmd_on_device(device, cmd):
        print(device, len(device))
        cmdStr = "adb -s %s %s" % (device, cmd);
        print(cmdStr)
        return adb.getCmdLines(cmdStr)


def start_test():
    for device in adb.devices():
        results = adb.execute_cmd_on_device(device, "shell ls /sdcard/")
        if "start_test.sh" not in results:
            print("do copy, device %s has no start_test.sh in sdcard" % device)
            subprocess.call("adb -s %s push start_test.sh /sdcard/" % device)

        results = adb.execute_cmd_on_device(device, "shell ls /sdcard/")
        if "start_test.sh" not in results:
            print("device %s has no start_test.sh in sdcard" % device)
            return

        print("start test on device", device)
        adb.execute_cmd_on_device(device, 'shell "sh /sdcard/start_test.sh"')

def collect_results():
    for device in adb.devices():
        results = adb.execute_cmd_on_device(device, "shell ls /sdcard/")
        if "collect_results.sh" not in results:
            print("do copy, device %s has no collect_results.sh in sdcard" % device)
            subprocess.call("adb -s %s push collect_results.sh /sdcard/" % device)

        results = adb.execute_cmd_on_device(device, "shell ls /sdcard/")
        if "collect_results.sh" not in results:
            print("device %s has no collect_results.sh in sdcard" % device)
        else:
            print("start collect results from devices", device)
            adb.execute_cmd_on_device(device, 'shell "sh /sdcard/collect_results.sh"')
            adb.execute_cmd_on_device(device, "pull -a /sdcard/results %s" % device)


def install(apk, replace):
    for device in adb.devices():
        if replace:
            adb.execute_cmd_on_device(device, "install -r %s" % apk)
        else:
            adb.execute_cmd_on_device(device, "install %s" % apk)


def printUsage():
    print("%s start_test|collect_results|install" % sys.argv[0])
    return


def main():
    if len(sys.argv) == 1:
        printUsage()
        return
    if sys.argv[1] == "start_test":
        start_test()
    elif sys.argv[1] == "collect_results":
        collect_results()
    elif sys.argv[1] == 'install':
        if len(sys.argv) == 3:
            install(sys.argv[2], False)
        elif len(sys.argv) == 4 and sys.argv[2] == '-r':
            install(sys.argv[3], True)
        else:
            printUsage()
    else:
        printUsage()

if __name__ == '__main__':
    main()