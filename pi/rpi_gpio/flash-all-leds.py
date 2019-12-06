#!/usr/bin/env python3

# Testing my first 4 led setup

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

print("Testing LEDs..")

# set LED PINS
leds = [24, 7, 6]

# Setup all
for all in leds:
  GPIO.setup(all, GPIO.OUT)

# Turn on all
for all in leds:
  GPIO.output(all, GPIO.HIGH)

# sleeping the thread leaves all leds on for one second
sleep(1)

# Turn off all
for all in leds:
  GPIO.output(all, GPIO.LOW)

# cleanup and exit
print("Exiting..")
GPIO.cleanup()
exit()

