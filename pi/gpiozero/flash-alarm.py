#!/usr/bin/env python3

# requires to install python3-gpiozero
# flashes A few leds

print("Loading gpiozero..")

from gpiozero import LED
from time import sleep

led1 = LED(22)
led2 = LED(23)

x = 1
print("Flashing two leds like an alarm..")
while(x < 5):
  print(x, "/4")
  led1.on()
  sleep(0.5)
  led1.off()

  led2.on()
  sleep(0.5)
  led2.off()
  x = x + 1

print("Exiting..")
exit()
