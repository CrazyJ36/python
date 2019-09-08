#!/usr/bin/env python3

# Testing my first 4 led setup

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

print("Testing LEDs..")
# LED PINS
l = [4, 18, 22, 23]
# Setup all
for n in l:
  GPIO.setup(n, GPIO.OUT)

# Turn on all
for n in l:
  GPIO.output(n, GPIO.HIGH)

sleep(1)
# Turn off all
for n in l:
  GPIO.output(n, GPIO.LOW)

print("Exiting..")
GPIO.cleanup()
exit()

