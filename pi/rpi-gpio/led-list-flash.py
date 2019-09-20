#!/usr/bin/env python3

# Shows that A list of pins can be easyly controlled in python.
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
pin_list = [24, 7, 6] # set multiple pins as ints in list
GPIO.setup(pin_list, GPIO.OUT) #  You can act on pins in the list in one function.
GPIO.output(pin_list, 1) # here, 1 is on, 0 is off
sleep(1)
GPIO.output(pin_list, 0) # HIGH can be stated as True/False, HIGH/LOW, 0/1 etc..
GPIO.cleanup()
