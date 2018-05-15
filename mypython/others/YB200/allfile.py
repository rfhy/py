# -*- encoding: UTF-8 -*-

import os
sn = '4001000C000000EC'


print("====== 1\n")

f = os.popen("adb -s " + sn + " shell ls -lR").read()

print("====== 2\n")

t = f.split("\r\n")

g = f.split("./")

'''
for i in range(0,len(t)):
    
    if '/sdcard/' in t[i]:
        print(t[i] + "\n")
        #e.write(t[i])
    else:
        if len(t[i]) > 30:
            if t[i].split()[3].strip() > 50000000:
                print(t[i] + "\n")




for i in range(0,len(t)-2):
    
    
    if '/sdcard/' in t[i] and '/sdcard/' not in t[i+1]:
	    
        print(t[i] + "\n")
        print i
        #e.write(t[i])
    if '/sdcard/' not in t[i]:
        if len(t[i]) > 35:
            if t[i].split()[3].strip().isdigit():
		    if int(t[i].split()[3].strip()) > 50000000:
			    
				print(t[i] + "\n")
'''

arr = []
for i in range(0,len(g)):

    m = g[i].split("\r\n")

    for k in range(0,len(m)):

        h = m[k].split()

        if len(h) == 7:
            if h[3].isdigit() and int(h[3]) > 1000000:

                print("./" + m[0])
                print m[k]
                arr.append(int(h[3]))

l = sum(arr) /float(1024 *1024)
print("\ntotal big files is: %.2f MB\n"%l)

