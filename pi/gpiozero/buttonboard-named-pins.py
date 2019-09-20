#!/usr/bin/env python3

from gpiozero import ButtonBoard

btns=ButtonBoard(button1=23,button2=27)

print("Press button 1 or 2, the 'values' output will show custom names")

while True:
  try:

    if btns.is_pressed:
      print(btns.value)

  except KeyboardInterrupt:
    print("\rExiting..")
    btns.close() #  close each board button
    exit(0)
