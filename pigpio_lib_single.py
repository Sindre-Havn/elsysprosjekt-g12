#!/usr/bin/env python

import time
import pigpio

frequency = 20_000 # Hz
wavelength = 1/frequency
halfwave = wavelength / 2

gpio2 = 2
gpio3 = 3

pi = pigpio.pi()

while True:
    pi.write(gpio2, 0)
    pi.write(gpio3, 0)
    time.sleep(halfwave)
    pi.write(gpio2, 1)
    pi.write(gpio3, 1)
    time.sleep(halfwave)
    
