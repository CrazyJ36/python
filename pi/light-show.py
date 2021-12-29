#!/usr/bin/env python

print("Loading...")
from gpiozero import PWMLED
from time import sleep

print("Atttempting to pulse 4 leds left-right...")

leds = [PWMLED(4), PWMLED(18), PWMLED(6), PWMLED(13)]
len = 0.4

def rightLightShift():
  x = 1
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
    x = x - 1

runInBothDirections = 0
while runInBothDirections < 3:
  rightLightShift()
  leftLightShift()
  runInBothDirections = runInBothDirections + 1

print("Exiting...")
for i in leds:
  i.close()
exit()

