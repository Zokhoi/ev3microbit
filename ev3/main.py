#!/usr/bin/env python3

from datetime import timedelta
from time import sleep
import json

f = open('config.json')
config = json.load(f)
f.close()

MACADDR = config['MACADDR']

from ev3dev2.sensor import INPUT_1,INPUT_2
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.stopwatch import StopWatch

import pygatt
print("import successful!")

adapter = pygatt.GATTToolBackend()

try:
    adapter.start()
    device = adapter.connect(MACADDR, address_type=pygatt.BLEAddressType.random)
    print("Bluetooth connection successful!")
except:
    print("Bluetooth connection failed!")



numbytearray=[bytearray([0x06,0x09,0x09,0x09,0x06]),bytearray([0x04,0x0C,0x04,0x04,0x1E]),bytearray([0x0C,0x12,0x04,0x08,0x1F]),bytearray([0x0E,0x02,0x0E,0x02,0x0E]),bytearray([0x14,0x14,0x1E,0x04,0x04]),bytearray([0x0E,0x08,0x0E,0x01,0x0E]),bytearray([0x06,0x08,0x1E,0x11,0x0E]),bytearray([0x0F,0x02,0x04,0x04,0x08]),bytearray([0x0E,0x11,0x0E,0x11,0x0E]),bytearray([0x0E,0x11,0x0E,0x02,0x02])]

    
start_touch=TouchSensor(INPUT_1)
end_touch=TouchSensor(INPUT_2)
timer=StopWatch


while True:
    bytearray(b'\xea\x80\x80READY\xde\xb4')
    while True:
        
        if start_touch.is_pressed():
            timer.start()
        
        if end_touch.is_pressed():
            timer.stop()
            time=timer.value_secs()
            break


        sleep(0.1)

    delay=0.6
    time=str(time)
    for p in range(3):
        device.char_write_handle(0x30, bytearray(time.encode('utf-8')))
        #Alternate method
        '''for i in time:
            if i==".":
                device.char_write_handle(0x2e, bytearray([0x00,0x00,0x00,0x0C,0x0C]))
                sleep(delay)
            else:
                device.char_write_handle(0x2e, numbytearray[int(i)])
                sleep(delay)
            device.char_write_handle(0x2e, bytearray([0x0E,0x10,0x0E,0x01,0x0E]))
            sleep(delay*3)'''

    while True:
        buttonA = device.char_read("e95dda90-251d-470a-a062-fa1922dfa9a8")
        buttonB = device.char_read("e95dda91-251d-470a-a062-fa1922dfa9a8")
        if buttonA == bytearray(b'\x01'):
            timer.reset()
            break
        elif buttonB == bytearray(b'\x01'):
            timer.reset()
            break

        sleep(0.1)
    device.char_write_handle(0x30, bytearray(b'\xea\x80\x80RESET\xde\xb4'))
    sleep(4)
    
    