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

'''
def i2c_send(number, line):
    if (number > 127): # can not be correctly encoded
        print("number to large")
        return

    
    data = struct.pack('BBBB', 0xf, 0xff, 0x41, 0x54)
    #bus.write_byte(address, number | (line << 7))
    bus.write_i2c_block_data(address, i2c_cmd_write, data)
    time.sleep(1)
    received = bus.read_byte(address) 

    if (countdown != received):
        print("error sending/receiving")

'''

def parse_time(now, dep):
    timeReal = str(dep['departureTime']['timeReal'])[:-9]
    timeReal = datetime.strptime(timeReal, time_format) 
    c =  int(round((timeReal - timeNow).seconds / 60.0))
    print(c)
    return c

times = []

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
            times.append(n1)
            times.append(n2)

            print("[{}] Towards {} in {} and {} minutes".format(timeNow, direction, n1, n2))
            break

print(times)
bus.write_i2c_block_data(address, i2c_cmd_write, times)
time.sleep(1)
response  = bus.read_i2c_block_data(address, i2c_cmd_read, 5)
print(response)
