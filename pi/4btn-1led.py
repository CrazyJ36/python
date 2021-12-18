#!/usr/bin/env python3

print("Loading gpiozero")

from gpiozero import LED, ButtonBoard
from time import sleep

led = LED(16)
btns = ButtonBoard(22, 24, 25, 5)

print("Press any button, LED will light to show button number 1-4...")
print("Ctrl-C to exit\n")

def flashTimes(number):
  x = 0
  while x < number:
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)
    x = x + 1
while True :
  try:
    if btns[0].is_pressed:
      print("button 1 pressed")
      flashTimes(1)
    elif btns[1].is_pressed:
      print("button 2 pressed")
      flashTimes(2)
    elif btns[2].is_pressed:
      print("button 3 pressed")
      flashTimes(3)
    elif btns[3].is_pressed:
      print("button 4 pressed")
      flashTimes(4)

    sleep(0.2)
  except KeyboardInterrupt:
    print("\rExiting..")
    exit(0)



