#!/usr/bin/env python3
print("Loading..\n")

from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

led = LED(24, pin_factory=PiGPIOFactory(host='192.168.1.166'))

print("Be sure to set bash variable PIGPIO_ADDR=ip_address")
print("And set GPIOZERO_PIN_FACTORY=pigpio")
print("Or set LED(pin, pin_factory=PiGPIOFactory (with import) in script.\n")
print("Attempting to flash LED from network")

led.on()
sleep(1)
led.off
led.close()
print("\ndone")
exit(0)

