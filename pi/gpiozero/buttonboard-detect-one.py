#!/usr/bin/env python3

# also, use 'function(**kwargs)' like
# function(name1 = value1, name2 = value2)
# should be able to get named buttons from key/value

from time import sleep
from gpiozero import ButtonBoard

btns = ButtonBoard(23, 27, 22, 25, 9, 5, 8)

print("Press any button...")

while True:
  try:
    if btns[0].is_pressed:
      print("button 0 pressed")
    if btns[1].is_pressed:
      print("button 1 pressed")
    if btns[2].is_pressed:
      print("button 2 pressed")
    if btns[3].is_pressed:
      print("button 3 pressed")
    if btns[4].is_pressed:
      print("button 4 pressed")
    if btns[5].is_pressed:
      print("button 5 pressed")
    if btns[6].is_pressed:
      print("button 6 pressed")

    sleep(0.2)

  except KeyboardInterrupt:
    print("Exiting")
    exit(0)
