#!/usr/bin/env python2
# Testing my first 4 led, two button setup
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

print "Testing LEDs.."
# LED PINS
l = [15, 21, 19, 4]
# Setup all
for n in l:
  GPIO.setup(n, GPIO.OUT)

# Turn on all
for n in l:
  GPIO.output(n, GPIO.HIGH)
sleep(5)
# Turn off all
for n in l:
  GPIO.output(n, GPIO.LOW)

# BUTTONS
b = [14, 26]
for x in b:
  GPIO.setup(x, GPIO.IN)

while GPIO.input( b[0] ) == GPIO.LOW:
  sleep(0.1)
  if GPIO.input( b[0] ) == GPIO.HIGH:
    print "pushed button on gpio 14"

GPIO.cleanup()
exit()

