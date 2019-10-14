#!/usr/bin/env python3
print("Loading...")

from time import sleep

# Imports everything defined in permaMyLib.py (which is in this directory)
# which defines pins for btns, leds, etc.. also already imports Button, LED
import permaMyLib

# points to the variable 'btn1' in permaMyLib library with: library.variable
btn = permaMyLib.btn1

print(
"""Press button1 to show that importing button pin
declaration from another file was successful...
Ctrl-C to exit...
""",
end='')

# Use other files button decleration as 'btn'
while True:
  try:
    if btn.is_pressed:  # btn from permaMyLib.btn1 is used here as btn
      print("Button 1 pressed")
    sleep(0.1)
  except KeyboardInterrupt:
    print("\rRead source to see how this works.\nExiting..")
    exit(0)
