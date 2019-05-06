#!/usr/bin/env python2
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
x = 0
while x < 5:
 GPIO.output(4, GPIO.HIGH)
 sleep(1)
 GPIO.output(4, GPIO.LOW)
 GPIO.output(18, GPIO.HIGH)
 sleep(1)
 GPIO.output(18, GPIO.LOW)
 print x
 x = x + 1
GPIO.cleanup()
