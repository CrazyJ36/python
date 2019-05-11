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
sleep(1)
# Turn off all
for n in l:
  GPIO.output(n, GPIO.LOW)

print "push buttons to test.."
# BUTTONS
b = [14, 26]
for x in b:
  GPIO.setup(x, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while GPIO.input( b[1] ) == GPIO.LOW:
  sleep(0.1)
  if GPIO.input( b[1] ) == GPIO.HIGH:
    print "Button 14 pushed.."

print "Exiting.."
GPIO.cleanup()
exit()

