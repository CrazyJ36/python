#!/usr/bin/env python3

from gpiozero import ButtonBoard, LEDBoard
from signal import pause

print("""The 4 buttons are the 'trigger' switch to the leds on.
An led (1-4) will light when that same positional button (1-4) is pressed.
Press Ctrl-C to exit.
""")

btns = ButtonBoard(22, 24, 25, 5)
leds = LEDBoard(23, 18, 12, 16)

leds.source = btns

try:
  pause()
except KeyboardInterrupt:
  print("\rExiting..")
  leds.close()
  btns.close()
  exit(0)
