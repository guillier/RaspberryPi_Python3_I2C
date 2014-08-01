#!/usr/bin/env python3

import smbus

found = False

try:
    smbus.SMBus(0)
    print('I2C bus #0 is accessible')
    found = True
except:
    pass

try:
    smbus.SMBus(1)
    print('I2C bus #1 is accessible')
except:
    if not found:
        print('Error accessing a I2C bus')
