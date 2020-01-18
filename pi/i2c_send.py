import smbus2
import time
import json
import struct
from datetime import datetime
bus = smbus2.SMBus(1)

# first bit tells arduino which line to write into

address = 0x05
i2c_cmd_write = 0x01
i2c_cmd_read = 0x02

data_dir = "/home/pi/electronics/data"
time_format = "%Y-%m-%dT%H:%M:%S"

files = ["data_172.json", "data_165.json"]

def parse_time(now, dep):
    timeReal = str(dep['departureTime']['timeReal'])[:-9]
    timeReal = datetime.strptime(timeReal, time_format) 
    return int(round((timeReal - timeNow).seconds / 60.0))

countdown = []

for line, file in enumerate(files):

    timeNow = datetime.now()
   
    with open("{}/{}".format(data_dir, file)) as f:
        data = json.load(f)
        f.close()

    stop = data['data']['monitors'][0]['locationStop']['properties']['title']
    direction = data['data']['monitors'][0]['lines'][0]['towards']
    departures = data['data']['monitors'][0]['lines'][0]['departures']['departure']

    for i, departure in enumerate(departures):
        timeReadable = str(departure['departureTime']['timeReal'])[:-9]
        timeReal = datetime.strptime(timeReadable, time_format) 

        if (timeNow <= timeReal):
            #print(i)
            #print(departures[i]['departureTime'])
            #print(departures[i+1]['departureTime'])
            n1 = parse_time(timeNow, departures[i])
            n2 = parse_time(timeNow, departures[i+1])
            countdown.append(n1)
            countdown.append(n2)

            print("[{}] Station {} towards {} in {} and {} minutes".format(timeNow, stop, direction, n1, n2))
            break

bus.write_i2c_block_data(address, i2c_cmd_write, countdown)
time.sleep(1)
response  = bus.read_i2c_block_data(address, i2c_cmd_read, 5)
