#!/usr/bin/env python3
print("Loading...")

# Imports everything defined in mylib.py (which is in this directory)
# which defines pins for btns, leds, etc..

import mylib

from time import sleep

# points to the variable 'btn1' in mylib.py library
# with syntax: library.variable
btn = mylib.btn1

print(
"""Press button1 to show that importing button pin
declaration from another file was successful...
Ctrl-C to exit...
""",
end='')

# Use other files button decleration as 'btn'
while True:
  try:
    if btn.is_pressed:  # btn from mylib.btn1 is used here as btn
      print("Button 1 pressed")
    sleep(0.1)
  except KeyboardInterrupt:
    print("\rRead source to see how this works.\nExiting..")
    exit(0)

# If you wanted to use new Buttons, LEDs, etc. in from gpiozero in
# this file, you would have to 'import gpiozero' in this file.
# Even though those imports were used in mylib.py, gpiozero's
# functions are not made available here. A new 'led = LED(18)'
# would not work here without importing gpoizero here as well.
