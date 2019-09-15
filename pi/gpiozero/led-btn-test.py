#!/usr/bin/env python3

# This test my "organized" hardware setup on perma-proto

print("Loading gpiozero")

from gpiozero import ButtonBoard, LEDBoard
from time import sleep


leds = LED(24)
# 4 is switch
btn = Button(4, 23)

print("Flashing LED")
led.on()
sleep(1)
led.off()

print("Press Button, ctrl-c to exit")
while True:
  try:
    if btn.is_pressed:
      print("Pressed")
      sleep(0.2)

  except KeyboardInterrupt:
    print("Exiting..")
    exit(0)
