from practicum import findDevices, McuBoard
devices = findDevices()
b = McuBoard(devices[0])

switch = b.usbRead(2,length=1)
print(switch)
