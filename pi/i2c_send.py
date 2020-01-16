#import smbus2
import time
import json
from datetime import datetime
#bus = smbus2.SMBus(1)

# first bit tells arduino which line to write into

address = 0x05
data_dir = "."

time_format = "%Y-%m-%dT%H:%M:%S"

files = ["data_172.json", "data_165.json"]

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    return number

def i2c_send(number, line):
    if (number > 127): # can not be correctly encoded
        print("number to large")
        return -1

    writeNumber(number | (line << 7))
    print("Raspberry sends: {} to line {}".format(countdown, line))
    time.sleep(1)
    received = readNumber()
    print("Arduino sends: {}".format(received))


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

        if (timeNow <= timeReal):
            
            countdown = int(round((timeReal - timeNow).seconds / 60.0))

            print("Towards {} in {} minutes".format(direction, countdown))

            #i2c_send(countdown, line)
            #time.sleep(2)
            break




