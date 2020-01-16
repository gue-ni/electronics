import smbus2
import time
import json
from datetime import datetime
bus = smbus2.SMBus(1)

# first bit tells arduino which line to write into

address = 0x05

files = ["data_sfp.json", "data_pha.json"]

def parseDeparture(json_response):
    return json_response['data']['monitors'][0]['lines'][0]['departures']['departure']	

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

timeNow = datetime.now()

for line, file in enumerate(files):

    with open(file) as f:
        data = json.load(f)
        f.close()

    countdown = -1

    for departure in parseDeparture(data):
        timeReadable = str(departure['departureTime']['timeReal'])[:-9]
        timeReal = datetime.strptime(timeReadable, "%Y-%m-%dT%H:%M:%S") 

        if (timeNow <= timeReal):
            print(timeReadable)
            
            countdown = (timeReal - timeNow).seconds / 60

            print("{} in {} minutes".format(file, countdown))

            i2c_send(countdown, line)
            time.sleep(2)
            break




