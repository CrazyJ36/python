#!/usr/bin/env python3

from gpiozero import ButtonBoard
from time import sleep

print("""
The syntax for calling A pre-made function with
name-able assignable **keyword_arguments is:
theFunction(custom_name1=actual_value, custom_name2=actual_value)
""")
btns = ButtonBoard(button1=22, button2=24, button3=25)

while True:
  try:
    if btns.is_pressed:
      print(btns.value)
      sleep(0.3)
  except KeyboardInterrupt:
    print("\rExiting... TODO: print only value keyword name not value.")
    btns.close() #  close each board button
    exit(0)

