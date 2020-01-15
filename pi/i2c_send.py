import smbus
import time
bus = smbus.SMBus(1)

address = 0x05

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    return number

while True:
    send = input("Number between 1 - 9: ")
    if not send:
        continue

    writeNumber(send)
    print("Raspberry sends: ", send)
    time.sleep(1)

    received = readNumber()
    print("Arduino sends: ", received)


