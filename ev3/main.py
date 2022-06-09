#!/usr/bin/env python3

# from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
# from ev3dev2.sensor import INPUT_1
# from ev3dev2.sensor.lego import TouchSensor
# from ev3dev2.led import Leds

import pygatt
from time import sleep
import binascii
import json

adapter = pygatt.GATTToolBackend()

DELAY = 1.0

f = open('config.json')
config = json.load(f)
f.close()

MACADDR = config['MACADDR']

try:
  adapter.start()

  print("Trying to connect to " + MACADDR + " ...")
  device = adapter.connect(MACADDR, address_type=pygatt.BLEAddressType.random)
  print('Connected to ' + MACADDR)
  for uuid in device.discover_characteristics().keys():
    print("Read UUID %s: %s" % (uuid, binascii.hexlify(device.char_read(uuid))))

  # while True:
  #   device.char_write_handle(0x2E, bytearray([0x1F, 0x11, 0x11, 0x11, 0x1F]))
  #   sleep(DELAY)
  #   device.char_write_handle(0x2E, bytearray([0x00, 0x0E, 0x0A, 0x0E, 0x00]))
  #   sleep(DELAY)
  #   device.char_write_handle(0x2E, bytearray([0x00, 0x00, 0x04, 0x00, 0x00]))
  #   sleep(DELAY)
  #   device.char_write_handle(0x2E, bytearray([0x00, 0x00, 0x00, 0x00, 0x00]))
  #   sleep(DELAY)
  #   device.char_write_handle(0x2E, bytearray([0x11, 0x0A, 0x04, 0x0A, 0x11]))
  #   sleep(DELAY)
  #   device.char_write_handle(0x2E, bytearray([0x00, 0x0A, 0x04, 0x0A, 0x00]))
  #   sleep(DELAY)
  #   device.char_write_handle(0x2E, bytearray([0x00, 0x00, 0x04, 0x00, 0x00]))
  #   sleep(DELAY)
  #   device.char_write_handle(0x2E, bytearray([0x00, 0x00, 0x00, 0x00, 0x00]))
  #   sleep(DELAY)
finally:
  adapter.stop()
