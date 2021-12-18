#!/usr/bin/env python3

from gpiozero import Button, LED
from signal import pause

print("button 1 is 'trigger' switch to led 1")
print("led will light as long as button is pressed.")

btn = Button(23)
led = LED(4)

led.source = btn

try:
  pause()
except KeyboardInterrupt:
  print("\rExiting..")
  led.close
  btn.close
  exit(0)
