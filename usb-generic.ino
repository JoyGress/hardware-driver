#include <usbdrv.h>
#include "LiquidCrystal_I2C.h"
//#include <hd44780.h>

#define RQ_SET_LED 0
#define RQ_SET_ALL_LED 1
#define RQ_GET_SWITCH 2
#define RQ_SET_ALARM 3
#define RQ_SET_GAME_POSTION 4
#define RQ_SET_TIME 5

////////////////////////Function Declare

void set_lcd();
void set_buzzer();

///////////////////////Global Variable

LiquidCrystal_I2C lcd(0x27,16,2);
static uint8_t buzz_status = 0;
static uint8_t current_position = 9;
static uint8_t new_position = 0;
static uint8_t current_time_hour = 0;
static uint8_t current_time_minute = 0;
static uint8_t new_time_hour = 12;
static uint8_t new_time_minute = 0;

////////////////////////////

usbMsgLen_t usbFunctionSetup(uint8_t data[8]){

	usbRequest_t *rq = (usbRequest_t*)data;
	static uint8_t switch_state;
	if(rq->bRequest == RQ_SET_LED){
		uint8_t led_index = rq->wIndex.bytes[0];
		uint8_t led_value = rq->wValue.bytes[0];

		if(led_index == 0){
			digitalWrite(PIN_PB0, led_value);
		}else if(led_index == 1){
			digitalWrite(PIN_PB1, led_value);
		}else if(led_index == 2){
			digitalWrite(PIN_PB2, led_value);
		}else if(led_index == 3){
			digitalWrite(PIN_PB3, led_value);
		}else if(led_index == 4){
			digitalWrite(PIN_PB4, led_value);
		}else if(led_index == 5){
			digitalWrite(PIN_PB5, led_value);
		}else if(led_index == 6){
			digitalWrite(PIN_PD0, led_value);
		}else if(led_index == 7){
			digitalWrite(PIN_PD5, led_value);
		}else if(led_index == 8){
			digitalWrite(PIN_PD6, led_value);
		}else{
		}

		return 0;
	}else if(rq->bRequest == RQ_SET_ALL_LED){

		uint8_t led_value_1_8 = rq->wValue.bytes[0];
		uint8_t led_value_9 = rq->wValue.bytes[1];
	}else if(rq->bRequest == RQ_GET_SWITCH){
		switch_state = 0;
		if(digitalRead(PIN_PC2) == HIGH){
			switch_state |= 1;
		}
		if(digitalRead(PIN_PC1) == HIGH){
			switch_state |= 2;
		}

		if(digitalRead(PIN_PC0) == HIGH){
			switch_state |= 4;
		}
		usbMsgPtr = (uint8_t*) &switch_state;
		return sizeof(switch_state);
	}else if(rq->bRequest == RQ_SET_ALARM){
		buzz_status = rq->wValue.bytes[0];
//    buzz_status = alarm_value;
	}else if(rq->bRequest == RQ_SET_GAME_POSTION){
    new_position = rq->wValue.bytes[0];
	}else if(rq->bRequest == RQ_SET_TIME){
    new_time_hour = rq->wIndex.bytes[0];
    new_time_minute = rq->wValue.bytes[0];
    
	}
	return 0;
}


void setup(){
  /////////////////////////PIN Setup
	pinMode(PIN_PB0,OUTPUT); //led1
	pinMode(PIN_PB1,OUTPUT); //led2
	pinMode(PIN_PB2,OUTPUT); //led3
	pinMode(PIN_PB3,OUTPUT); //led4
	pinMode(PIN_PB4,OUTPUT); //led5
	pinMode(PIN_PB5,OUTPUT); //led6
	pinMode(PIN_PD0,OUTPUT); //led7
	//pinMode(PIN_PD1,OUTPUT); //broken
	pinMode(PIN_PD5,OUTPUT); //led8
	pinMode(PIN_PD6,OUTPUT); //led9 
	pinMode(PIN_PC0,INPUT); //switch left
	pinMode(PIN_PC1,INPUT); //switch right
	pinMode(PIN_PC2,INPUT); //switch confirm
	pinMode(PIN_PC3,OUTPUT); //buzzer active

	//LCD setup
	lcd.init();
  lcd.backlight();
  lcd.setCursor(4,0);
  lcd.print("Practicum");
  delay(2000);
  lcd.setCursor(0,1);
  lcd.print("Hello World");
  delay(5000);


  //Usb Setup
	usbInit();
  
	usbDeviceDisconnect();
	delay(300);
	usbDeviceConnect();
  Serial.begin(9600);
}

void loop(){
	usbPoll();
	set_buzzer();
  set_lcd();
}

void set_lcd(){
  if(buzz_status == 1){ /// Playing Game
    if(new_position != current_position){
      lcd.clear();
      lcd.setCursor(8,1);
      lcd.print(new_position);
      current_position = new_position;
    }
  }else{
    if(current_time_hour != new_time_hour || current_time_minute != new_time_minute){
      lcd.clear();
      if(new_time_hour < 10){
        lcd.setCursor(6,0);
        lcd.print(0);
        lcd.setCursor(7,0);
        lcd.print(new_time_hour);
      }else{
        lcd.setCursor(6,0);
        lcd.print(new_time_hour);
      }
      lcd.setCursor(8,0);
      lcd.print(":");
      if(new_time_minute < 10){
        lcd.setCursor(9,0);
        lcd.print(0);
        lcd.setCursor(10,0);
        lcd.print(new_time_minute);
      }else{
        lcd.setCursor(9,0);
        lcd.print(new_time_minute);
      }
      current_time_hour = new_time_hour;
      current_time_minute = new_time_minute;
    }
  
  }
}

void set_buzzer(){
  if(buzz_status == 0){
    digitalWrite(PIN_PC3,LOW);
  }else{
    digitalWrite(PIN_PC3,HIGH);
  }
}
