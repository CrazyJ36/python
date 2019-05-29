#!/usr/bin/env python3

# Shows that A list of pins can be easyly controlled in python.
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
pin_list = [19, 4] # set multiple ints in list
GPIO.setup(pin_list, GPIO.OUT)
GPIO.output(pin_list, GPIO.HIGH)
sleep(1)
GPIO.output(pin_list, False) # HIGH can be stated as True/False, HIGH/LOW, etc..
GPIO.cleanup()
