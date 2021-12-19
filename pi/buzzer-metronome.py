#!/usr/bin/env python3

# - This is not accurate do to the 1 beat being
# Accented with A beep instead of A pulse,
# which takes more time.
# - 60 seconds in A minute.

print("Loading...")
from gpiozero import Buzzer, LEDBoard
from time import sleep
from sys import argv

buzzer = Buzzer(19)
leds = LEDBoard(23, 18, 12, 16)

print("Usage: $ ./buzzer-metronome.py float(0.1-1)")
bpm = float(argv[1])
beat = 1

def flashBeep(led_num):
  print(beat)
  leds[led_num].on()
  buzzer.on()
  sleep(bpm)
  leds[led_num].off()
  buzzer.off()

while True:
  try:
    if beat == 1:
      flashBeep(0)
      beat = beat + 1
    elif beat == 2:
      flashBeep(1)
      beat = beat + 1
    elif beat == 3:
      flashBeep(2)
      beat = beat + 1
    elif beat == 4:
      flashBeep(3)
      beat = beat + 1
    elif beat == 5:
        beat = 1

  except KeyboardInterrupt:
    print("\rExiting..")
    buzzer.close()
    leds[0].close()
    leds[1].close()
    leds[2].close()
    leds[3].close()
    del beat
    exit(0)
