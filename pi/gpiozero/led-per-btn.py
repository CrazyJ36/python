#!/usr/bin/env python3

print("Loading gpiozero")

from gpiozero import LEDBoard, ButtonBoard
from signal import pause

# Image representaion
# leds:  19                4
# leds:  21                15
# btns:  26    20    18    14
leds = LEDBoard(19,21,15,4)
btns = ButtonBoard(26,20,18,14)

print("Press A button for each led..")
print("Ctrl-C to exit")

while True :
  try:
    leds.source = btns.values
    pause()
  except KeyboardInterrupt:
    print("Exiting..")
    exit(0)


