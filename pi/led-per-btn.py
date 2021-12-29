#!/usr/bin/env python

print("Loading gpiozero")

from gpiozero import LEDBoard, ButtonBoard
from signal import pause

leds = LEDBoard(4, 18, 6, 13)
btns = ButtonBoard(17, 25, 24, 16)

print("Press A button, closest LED will light...")
print("Ctrl-C to exit\n")

while True :
  try:
    leds.source = btns
    pause()
  except KeyboardInterrupt:
    print("\rExiting..")
    exit(0)


