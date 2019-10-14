#!/usr/bin/env python3

print("Loading gpiozero")

from gpiozero import LEDBoard, ButtonBoard
from signal import pause

leds = LEDBoard(18,24,11,12,7,16)
btns = ButtonBoard(23,27,22,25,9,5)

print("Press the soft button that is closest to any of the middle row LEDs, LED will light...")
print("Ctrl-C to exit\n")

while True :
  try:
    leds.source = btns.values
    pause()
  except KeyboardInterrupt:
    print("\rExiting..")
    exit(0)


