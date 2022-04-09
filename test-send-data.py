from practicum import findDevices, McuBoard
import time
devices = findDevices()
b = McuBoard(devices[0])
"""b.usbWrite(0,index=0,value=0)
time.sleep(0.5)
b.usbWrite(0,index=1,value=1)
time.sleep(0.5)
b.usbWrite(0,index=2,value=0)
time.sleep(0.5)
b.usbWrite(0,index=3,value=1)
time.sleep(0.5)"""
for i in range(9):
    b.usbWrite(0,index=i,value=1)
    time.sleep(0.01)
"""while(1):
    b.usbWrite(0,index=0,value=1)
    time.sleep(2)
    b.usbWrite(0,index=0,value=0)
    time.sleep(2)
"""
