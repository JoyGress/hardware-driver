from practicum import findDevices
from peri import PeriBoard
import time
devices = findDevices()

b = PeriBoard(devices[0])

#test loop led
for i in range(9):
    b.set_led(i,1)
    time.sleep(0.5)

#get switch


"""while(1):
    switch = b.get_switch()
    print(switch)
    time.sleep(1)
"""

#set_alarm

"""for i in range(10):
    if(i == 3):
        b.set_alarm(1)
    elif(i == 7):
        b.set_alarm(0)

    time.sleep(1)"""

#set_position_index

for i in range(10):
    for j in range(10):
        b.set_time(i,j)
        time.sleep(0.5)

    if(i == 1):
        b.set_alarm(1)
        time.sleep(0.5)
        b.set_position_index(0)
        time.sleep(0.5)
    elif(i == 5):
        b.set_alarm(0)
        time.sleep(0.5)

    b.set_position_index(i)
    time.sleep(0.5)


