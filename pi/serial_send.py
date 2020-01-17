import serial

s = serial.Serial('/dev/ttyUSB0', 9600)


s.write(b'1')
line = s.readline()
print(line)
