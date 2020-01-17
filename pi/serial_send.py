

s.write(b'1')
response  = s.read()
print(response)

import serial
import smbus2
import time
import json
from datetime import datetime
s = serial.Serial('/dev/ttyUSB0', 9600)

# first bit tells arduino which line to write into

address = 0x05
data_dir = "/home/pi/electronics/data"
time_format = "%Y-%m-%dT%H:%M:%S"

files = ["data_172.json", "data_165.json"]

def serial_send(number, line):
    if (number > 127): # can not be correctly encoded
        print("number to large")
        return

    s.write(number | (line << 7))
    time.sleep(1)
    received = s.read()

    if (countdown != received):
        print("error sending/receiving")


for line, file in enumerate(files):

    timeNow = datetime.now()
   
    with open("{}/{}".format(data_dir, file)) as f:
        data = json.load(f)
        f.close()

    stop = data['data']['monitors'][0]['locationStop']['properties']['title']
    direction = data['data']['monitors'][0]['lines'][0]['towards']
    departures = data['data']['monitors'][0]['lines'][0]['departures']['departure']

    #print(direction)
    #print(departures)
    
    countdown = -1

    for departure in departures:
        timeReadable = str(departure['departureTime']['timeReal'])[:-9]
        
        timeReal = datetime.strptime(timeReadable, time_format) 
        timePlanned = datetime.strptime(str(departure['departureTime']['timePlanned'])[:-9], time_format)
   
        if (timeNow <= timeReal):
            
            countdown = int(round((timeReal - timeNow).seconds / 60.0))

            print("[{}] Towards {} in {} minutes ({}) planned : {}".format(timeNow, direction, countdown, timeReal, timePlanned))

            serial_send(countdown, line)
            time.sleep(2)
            break




