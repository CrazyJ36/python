#!/usr/bin/env python3

from gpiozero import ButtonBoard
import inspect
from time import sleep

print("""
The syntax for calling A pre-made function with
name-able assignable **keyword_arguments is:
TheFunction(custom_name1=actual_arg, custom_name2=actual_arg)
""")

btns=ButtonBoard(button1=23,button2=27, button3=22)

print("Press button 1, 2 or 3. The 'values' output will show custom names")

while True:
  try:
    if btns.is_pressed:
      print(btns.value)
    sleep(0.1)
  except KeyboardInterrupt:
    print("\rExiting... TODO: get, print only left keyword name not value.")
    btns.close() #  close each board button
    exit(0)
