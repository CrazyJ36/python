#!/usr/bin/env python
print("Loading...")\

from gpiozero import DigitalOutputDevice
from time import sleep

pin = DigitalOutputDevice(21)

print("Turning fan on for 20 seconds")
pin.on()
sleep(20)
print("Turning fan off")
pin.off()

print("Exiting")
pin.close()
exit()
