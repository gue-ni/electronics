import smbus2
import time
import json
import datetime
bus = smbus2.SMBus(1)

address = 0x05

files = ["data_sfp.json", "data_pha.json"]

def parse_departure(json_response):
	return json_response['data']['monitors'][0]['lines'][0]['departures']['departure']	


def parse_date(string):
    return int(datetime.datetime.strptime(string, '%Y-%m-%dT%H:%M:%S').strftime("%s"))

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    return number

current_timestamp = parse_date(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')) 

for file in files:

    with open(file) as f:
        data = json.load(f)
        f.close()

    countdown = -1

    for departure in parse_departure(data):
        timeRealReadable = str(departure['departureTime']['timeReal'])[:-9]
        timeReal = parse_date(timeRealReadable)

        if (current_timestamp <= timeReal):
            countdown = (timeReal - current_timestamp) / 60
            print(countdown)
        
            writeNumber(countdown)
            print("Raspberry sends: ", countdown)
            time.sleep(1)

            received = readNumber()
            print("Arduino sends: ", received)

            break



