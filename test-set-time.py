from practicum import findDevices, McuBoard
import time

devices = findDevices()
b= McuBoard(devices[0])

for i in range(10):
    for j in range(10):
        b.usbWrite(5,index=i,value=j)
        time.sleep(1)
    if(i == 0):
        b.usbWrite(3,value=1)
        time.sleep(0.5)
        b.usbWrite(4,value=0)
    if(i == 1):
        b.usbWrite(3,value=0)
    

