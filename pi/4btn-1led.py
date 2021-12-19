#!/usr/bin/env python3

print("Loading gpiozero")

from gpiozero import LEDBoard, ButtonBoard
from time import sleep

leds = LEDBoard(23, 27, 12, 16)
btns = ButtonBoard(22, 24, 25, 5)

print("Press any button, LED will light to show button number 1-4...")
print("Ctrl-C to exit\n")

while True :
  try:
    if btns[0].is_pressed:
      print("button 1 pressed")
      leds[0].on()
      sleep(0.2)
      leds[0].off()
      sleep(0.2)
    elif btns[1].is_pressed:
      print("button 2 pressed")
      leds[1].on()
      sleep(0.2)
      leds[1].off()
      sleep(0.2)
    elif btns[2].is_pressed:
      print("button 3 pressed")
      leds[2].on()
      sleep(0.2)
      leds[2].off()
      sleep(0.2)
    elif btns[3].is_pressed:
      print("button 4 pressed")
      leds[3].on()
      sleep(0.2)
      leds[3].off()
      sleep(0.2)

  except KeyboardInterrupt:
    print("\rExiting..")
    exit(0)



