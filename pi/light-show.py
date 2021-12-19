#!/usr/bin/env python

print("Loading...")
from gpiozero import PWMLED
from time import sleep

print("Atttempting to pulse 4 leds left-right...")

leds = [PWMLED(23), PWMLED(18), PWMLED(12), PWMLED(16)]
len = 0.5

def rightLightShift():
  x = 0
  while x < 4:
    if x == 0:
      leds[0].pulse(len, len, 1, True)
      sleep(len)
    elif x == 1:
      leds[1].pulse(len, len, 1, True)
      sleep(len)
    elif x == 2:
      leds[2].pulse(len, len, 1, True)
      sleep(len)
    elif x == 3:
      leds[3].pulse(len, len, 1, True)
      sleep(len)
    x = x + 1

def leftLightShift():
  x = 2
  while x != -1:
    if x == 2:
      leds[2].pulse(len, len, 1, True)
      sleep(len)
    elif x == 1:
      leds[1].pulse(len, len, 1, True)
      sleep(len)
    elif x == 0:
      leds[0].pulse(len, len, 1, True)
      sleep(len)
    x = x - 1

rightLightShift()
leftLightShift()

print("Exiting...")
leds[0].close()
leds[1].close()
leds[2].close()
leds[3].close()
exit()

