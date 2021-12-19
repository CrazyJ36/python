#!/usr/bin/env python3
# This is not accurate do to the 1 beat being
# Accented with A beep instead of A pulse,
# which takes more time.

from gpiozero import Buzzer
from time import sleep
buzzer = Buzzer(19)
beat = 1
while True:
  try:
    print(beat)
    if beat == 1:
      buzzer.beep(0.004, 0.004, 5, False)
      sleep(0.5)
      beat = beat + 1
    else:
      buzzer.on()
      sleep(0.5)
      buzzer.off()
      beat = beat + 1
      if beat == 5:
        beat = 1
  except KeyboardInterrupt:
    print("\rExiting..")
    del beat
    exit(0)
