#!/usr/bin/env python3

from gpiozero import ButtonBoard, LEDBoard
from signal import pause

btns = ButtonBoard(22, 24, 25, 5)
leds = LEDBoard(23, 27, 12, 16)

leds.source = btns

if btns.is_pressed:
  print(btns)
pause()
