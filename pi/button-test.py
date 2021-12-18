#! /usr/bin/env python3

from gpiozero import Button
from time import sleep

btn = Button(22)

print("Press button 1 on pin 22...")
while True:
  try:
    if btn.is_pressed:
      print("Pressed buttons' data: " + str(btn) + ",\nwith value(1 for closed, 0 for open): " + str(btn.value))
      sleep(0.2)
  except KeyboardInterrupt:
    print("Exiting")
    btn.close()
    exit(0)
