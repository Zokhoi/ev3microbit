#!/usr/bin/env python3
# This script does not work as it segfaults.
# See https://github.com/pybricks/support/issues/514#issuecomment-905909129

import time

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

from gattlib import GATTRequester

import json

DELAY = 0.1

f = open('config.json')
config = json.load(f)
f.close()

MACADDR = config['MACADDR']

print("Trying to connect to " + MACADDR + " ...")
req = GATTRequester(MACADDR, False)
req.connect(True, channel_type="random")
# req.connect(True, channel_type="random", security_level="medium")
if req.is_connected():
  print('Connected to ' + MACADDR)

# print('Trying to read by handle...')
# data = req.read_by_handle(0x27)
# print('Successfully read by handle: '+str(data))

# print('Trying to read by uuid...')
# data = req.read_by_uuid("e95dda90-251d-470a-a062-fa1922dfa9a8")[0]
# print('Successfully read by uuid: '+str(data))


while True:
  req.write_by_handle(0x2e, str([0x00, 0x00, 0x00, 0x00, 0x00]))
  time.sleep(DELAY)
  req.write_by_handle(0x2e, str([0x11, 0x0A, 0x04, 0x0A, 0x11]))
  time.sleep(DELAY)
  req.write_by_handle(0x2e, str([0x00, 0x0A, 0x04, 0x0A, 0x00]))
  time.sleep(DELAY)
  req.write_by_handle(0x2e, str([0x00, 0x00, 0x04, 0x00, 0x00]))
  time.sleep(DELAY)
  req.write_by_handle(0x2e, str([0x00, 0x00, 0x00, 0x00, 0x00]))
