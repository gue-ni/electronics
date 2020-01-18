#!/usr/bin/python3
import serial
import time
import struct
 
s = serial.Serial('/dev/ttyACM0', 9600) # Namen ggf. anpassen
try:
    s.open()
except IOError:
    s.close()
    s.open()


time.sleep(3) # der Arduino resettet nach einer Seriellen Verbindung, daher muss kurz gewartet werden
 
to_send = struct.pack('B', 0x41)

s.write(to_send)

try:
    while True:
        response = s.read(2)
#        response = int.from_bytes(response, byteorder='little', signed=False)
        response = struct.unpack('BB', response)   
        print(response)
except KeyboardInterrupt:
    s.close()