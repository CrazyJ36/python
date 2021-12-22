#!/usr/bin/env python

print("Loading gpiozero")

from gpiozero import LED
from time import sleep

led = LED(4)

print("Lighting led for 1 second")
led.on()
sleep(1)
led.off()

led.close()
exit()


