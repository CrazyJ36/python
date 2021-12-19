#!/usr/bin/env python
print("Loading...")\

from gpiozero import DigitalOutputDevice
from time import sleep

# Turn on 5V fan electronically in raspberry pi code, using transistor example:
# 1. Connect negative wire of fan to collector pin of transistor.
# 2. Connect positive wire of fan to 5V output pin of raspberry pi.
# 3. Connect any gpio pin of pi to 1kOHM resistor, and other end of resistor to base of transistor.
# 4. Connect emitter pin of transistor to A ground pin of raspberry pi.
# 5. Set gpio pin HIGH or LOW to turn fan on/off.

pin = DigitalOutputDevice(21)

print("Turning fan on for 5 seconds")
pin.on()
sleep(5)
print("Turning fan off for 5 seconds")
pin.off()
sleep(5)
print("Turning fan on again for 5 seconds")
pin.on()
sleep(5)
print("Turning fan off for the last time")
pin.off()

print("Exiting")
pin.close()
exit()
