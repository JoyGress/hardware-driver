from practicum import findDevices , McuBoard
import time
devices = findDevices()
b = McuBoard(devices[0])
b.usbWrite(3,value=1)
b.usbWrite(4,value=2)
time.sleep(2)
b.usbWrite(4,value=3)
time.sleep(3)
b.usbWrite(4,value=5)
time.sleep(2)
b.usbWrite(3,value=0)
