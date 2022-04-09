import requests
from math import floor
from time import time, sleep
import json
from practicum import findDevices
from peri import PeriBoard


devices = findDevices()
b = PeriBoard(devices[0])

def get_request(): # use to check if it's alarm time or not
    r = requests.get("http://127.0.0.1:8000/isalarm/")
    x = r.text
    json_acceptable_string = x.replace("'", "\"")
    d = json.loads(json_acceptable_string)
    res = d.get("result")
    if(res == "True"):
        return True
    else:
        return False

while(1):
    if(get_request()): # if it's alarm time , starts game
        exec(open('ingame.py').read())
     # else show time
    curtime = (time() + 7 * 3600) % 86400
    hour = floor(curtime / 3600)
    minute = floor(curtime % 3600 / 60)
    b.set_time(hour,minute)
    sleep(60)
