#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
pin_list = [17, 27] # set multiple ints in list
GPIO.setup(pin_list, GPIO.OUT)
GPIO.output(pin_list, GPIO.HIGH)
sleep(1)
GPIO.output(pin_list, False)
GPIO.cleanup()
