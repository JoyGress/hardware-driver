from practicum import findDevices, McuBoard
import time
devices = findDevices()
b = McuBoard(devices[0])
#b.usbWrite(3,value=0)
while(1):
    b.usbWrite(3,value=1)
    time.sleep(1)
    b.usbWrite(3,value=0)
    time.sleep(1)

    

