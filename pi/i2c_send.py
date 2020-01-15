import smbus2
import time
import json
import datetime
bus = smbus2.SMBus(1)

# first bit tells arduino which line to write into

address = 0x05

files = ["data_sfp.json", "data_pha.json"]

def parseDeparture(json_response):
	return json_response['data']['monitors'][0]['lines'][0]['departures']['departure']	

def parseDate(string):
    return int(datetime.datetime.strptime(string, '%Y-%m-%dT%H:%M:%S').strftime("%s"))

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    return number

current_timestamp = parseDate(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')) 

for file in files:

    with open(file) as f:
        data = json.load(f)
        f.close()

    countdown = -1

    for count, departure in enumerate(parseDeparture(data)):
        timeRealReadable = str(departure['departureTime']['timeReal'])[:-9]
        timeReal = parseDate(timeRealReadable)

        if (current_timestamp <= timeReal):
            countdown = (timeReal - current_timestamp) / 60
            print("{} in {} minutes".format(file, countdown))

            if (countdown > 127): # can not be correctly encoded
                break
        
            writeNumber(countdown | (count << 7))
            print("Raspberry sends: {} to line {}".format(countdown, count))
            time.sleep(1)
            received = readNumber()
            print("Arduino sends: ", received)

            break



