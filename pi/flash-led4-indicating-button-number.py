#!/usr/bin/env python3

# For '4btn-4led' adafruit perma-proto mini circut.

print("Loading gpiozero")

from gpiozero import LED, ButtonBoard
from time import sleep

led = LED(16)
btns = ButtonBoard(22, 24, 25, 5)

def flashTimes(number):
  x = 0
  print("Button " + str(number) + " pressed.")
  while x < number:
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.2)
    x = x + 1

print("Press any button, LED 4 will light to show button number 1-4...")
print("Ctrl-C to exit\n")

while True :
  try:
    if btns[0].is_pressed:
      flashTimes(1)
    elif btns[1].is_pressed:
      flashTimes(2)
    elif btns[2].is_pressed:
      flashTimes(3)
    elif btns[3].is_pressed:
      flashTimes(4)
  except KeyboardInterrupt:
    print("\rExiting..")
    led.close()
    btns.close()
    exit(0)



