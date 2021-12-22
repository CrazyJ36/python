#! /usr/bin/env python3

from gpiozero import Button
from time import sleep

btn = Button(16)

print("Press btn...")
while True:
  try:
    if btn.is_pressed:
      print("Button pressed")
      sleep(0.2)
  except KeyboardInterrupt:
    print("Exiting")
    btn.close()
    exit(0)
