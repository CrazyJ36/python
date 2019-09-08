#!/usr/bin/env python3

print("Loading gpiozero")

from gpiozero import LEDBoard, ButtonBoard
from signal import pause

# Image representaion
# leds:  4     18    22    23
# btns:  17    27    25    5
leds = LEDBoard(18, 4, 22, 23)
btns = ButtonBoard(17, 27, 24, 5)

print("Press A button for each led..")
print("Ctrl-C to exit")

while True :
  try:
    leds.source = btns.values
    pause()
  except KeyboardInterrupt:
    print("Exiting..")
    exit(0)


