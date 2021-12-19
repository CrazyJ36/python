#!/usr/bin/env python

print("Loading")
from gpiozero import PWMLED
from time import sleep


print("LED4 will gradually increase in brightness")

led = PWMLED(pin=16, active_high=True, initial_value=0.1, frequency=100)
sleep(1)
led.close()
led = PWMLED(pin=16, active_high=True, initial_value=0.3, frequency=100)
sleep(1)
led.close()
led = PWMLED(pin=16, active_high=True, initial_value=0.5, frequency=100)
sleep(1)
led.close()
led = PWMLED(pin=16, active_high=True, initial_value=0.7, frequency=100)
sleep(1)
led.close()
led = PWMLED(pin=16, active_high=True, initial_value=1, frequency=100)
sleep(1)
led.close()

print("Exiting")
exit()
