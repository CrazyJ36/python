#!/usr/bin/env python2

import RPi.GPIO as GPIO
from time import sleep

# In the case A (GPIO)pin you wnat to use is on A (BOARD)pin that
# does not initially show board AND gpio(On Sparkfuns' reference sheet)
# as in Board pin 5, GPIO 3, PIs' processor must be using the pin for something
# else (SCL in this pins' case), so the led is already normally on.
# Though it can be temporarily overrided and used. This program still works.

pin = 5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, GPIO.LOW)
sleep(1)
GPIO.output(pin, GPIO.HIGH)
sleep(1)
GPIO.output(pin, GPIO.LOW)
sleep(1)

GPIO.cleanup()
exit()

