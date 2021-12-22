#!/usr/bin/env python

print("Loading...")

from gpiozero import ButtonBoard, LEDBoard
from time import sleep

btns = ButtonBoard(button1 = 17, button2 = 25, button3 = 24, button4 = 16)
leds = LEDBoard(led1 = 4, led2 = 18, led3 = 6, led4 = 13)

# Turns LEDBoard and ButtonBoard into A corresponding grid.
leds.source = btns

print("""
Push any of 4 buttons, corresponding led number will light once.
Ctrl-C to exit.
""")

while True:
  try:
    if btns.is_pressed:
      print(btns.value)
      sleep(0.2)
  except KeyboardInterrupt:
    print("Exiting")
    btns.close()
    leds.close()
    exit()
