#!/usr/bin/python3

print("Loading..")

from gpiozero import Button

btn = Button(17)

print("Now detecting hard vibrations from sensor on pin 17...")

while True:
  try:
    if btn.is_pressed:
      print("Sensed Vibration with sensor on pin 17")
  except KeyboardInterrupt:
    print("Exiting")
    exit(0)



