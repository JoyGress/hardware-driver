from practicum import McuBoard

RQ_SET_LED = 0
RQ_SET_ALL_LED = 1
RQ_GET_SWITCH = 2
RQ_SET_ALARM = 3
RQ_SET_GAME_POSITION = 4
RQ_SET_TIME = 5

class PeriBoard(McuBoard):
    def set_led(self,light_id,led_value):
        self.usbWrite(RQ_SET_LED,index=light_id,value=led_value);

    def get_switch(self):
        #switch_state = [0,0,0]
        getSwitch2 = self.usbRead(RQ_GET_SWITCH,length=1)
        getSwitch = bin(getSwitch2[0])
        print(f'getSwitch = {getSwitch}  len = {len(getSwitch)} last_index = {getSwitch[-1]} {(len(getSwitch) == 3 and getSwitch[-1] == 0)}')
        if(len(getSwitch) == 3 and int(getSwitch[-1]) == 0):
            return [0,0,0]
        elif(len(getSwitch) == 3 and int(getSwitch[-1]) == 1):
            return [0,0,1]
        elif(len(getSwitch) == 4):
            return [0,1,0]
        elif(len(getSwitch) == 5):
            return [1,0,0]
    def set_alarm(self,status_alarm):
        self.usbWrite(RQ_SET_ALARM,value=status_alarm)

    def set_position_index(self,index):
        self.usbWrite(RQ_SET_GAME_POSITION,value=index)

    def set_time(self,hour,minute):
        self.usbWrite(RQ_SET_TIME,index=hour,value=minute)



