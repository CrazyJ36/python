#!/usr/bin/env python3

from gpiozero import Buzzer
from time import sleep

bz = Buzzer(19, active_high=False)
while True:
  bz.on()
  print("on")
  sleep(0.5)
  bz.off()
  print("off")
  sleep(0.5)
