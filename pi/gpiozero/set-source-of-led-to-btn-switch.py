#!/usr/bin/env python3

from gpiozero import Button, LED
from signal import pause

print("button 1 is 'trigger' switch to led 1")
btn = Button(23)
led = LED(24)

led.source = btn

try:
  pause()
except KeyboardInterrupt:
  print("\rExiting..")
  led.close
  btn.close
  exit(0)
