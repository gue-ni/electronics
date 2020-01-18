#!/usr/bin/python3
import serial
import time
import struct
 
s = serial.Serial('/dev/ttyACM1', 9600) 

try:
    s.open()
except IOError:
    s.close()
    s.open()

time.sleep(3) 
 
data = struct.pack('BBBB', 0xf, 0xff, 0x41, 0x54)

print("Writing...")
s.write(data)

print("Reading...")
try:
    response = s.read(4)
    response = struct.unpack('BBBB', response)   
    print(response)


except KeyboardInterrupt:
    s.close()
