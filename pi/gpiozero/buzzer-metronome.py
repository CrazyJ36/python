#!/usr/bin/env python3
from gpiozero import Buzzer
from time import sleep
buzzer = Buzzer(19)
beat = 1
while True:
  if beat is 5:
    beat = 1
  buzzer.on()
  print(beat)
  sleep(0.5)
  beat = beat + 1
  buzzer.off()
  print(beat)
  sleep(0.5)
  beat = beat + 1

