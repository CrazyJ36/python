#!/usr/bin/env python

print("Loading...")

from gpiozero import ButtonBoard, LEDBoard
from time import sleep

btns = ButtonBoard(button1 = 22, button2 = 24, button3 = 25, button4 = 5)
leds = LEDBoard(led1 = 23, led2 = 18, led3 = 12, led4 = 16)

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
