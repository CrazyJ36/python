#!/usr/bin/env python3
print("Loading..")
from gpiozero import LED
from time import sleep
led = LED(4)
print("Flashing 'dancy' led for 10 seconds to show animation")
led.on()
sleep(10)
led.off()
led.close()
del led
print("Done")
exit(0)
