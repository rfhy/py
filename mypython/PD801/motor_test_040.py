import motor
import time
import random
from datetime import datetime

N = 100000

def logs(str):
    c1=datetime.now().strftime('%Y%m%d-%H:%M:%S')
    lirun=open('PD801_motor_040.log','a+')
    lirun.write(c1 + " " + str + "\n")
    lirun.flush()
    lirun.close()
    print(c1 + " "  + str)

motor.rotto(0, 0)
time.sleep(3)

for i in xrange(N):
    t = random.randint(-150, 150)
    s = random.randint(0, 100)
    logs('angle: %s, speed: %s' %(t, s))
    motor.rotto(t, s)
    time.sleep(5)
    
motor.rotto(0, 0)
time.sleep(5)


