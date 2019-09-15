#!/usr/bin/env python3

print("Loading gpiozero")

from gpiozero import LEDBoard, ButtonBoard
from signal import pause

# Image representaion
# leds:  24     7      6
# btns:  27    10    5
leds = LEDBoard(24, 7, 6)
btns = ButtonBoard(27, 9, 5)

print("Press the soft button that is closest to any of the 3 LEDs, LED will light...")
print("Ctrl-C to exit\n")

while True :
  try:
    leds.source = btns.values
    pause()
  except KeyboardInterrupt:
    print("Exiting..")
    exit(0)


