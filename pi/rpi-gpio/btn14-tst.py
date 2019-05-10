#!/usr/bin/env python2
import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
pin = 14
GPIO.setup(pin, GPIO.IN)

GPIO.add_event_detect(pin, GPIO.RISING)
x = 0
y = 0
while x < 300:
  x = x + 1
  if GPIO.event_detected(pin):
    sleep(0.1)
  else:
    print "btn pressed"
    y = y + 1
    sleep(0.1)

print y

GPIO.cleanup()
exit(0)
