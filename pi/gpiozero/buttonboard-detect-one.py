#!/usr/bin/env python3

from time import sleep
from gpiozero import ButtonBoard

btns = ButtonBoard(23, 27)

print("Press button 1 or 2...")

while True:
  try:
    if btns[0].is_pressed:
      print("button one pressed")
    elif btns[1].is_pressed:
      print("button two pressed")
    sleep(0.2)

  except KeyboardInterrupt:
    print("Exiting")
    exit(0)
