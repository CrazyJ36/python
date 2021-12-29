#!/usr/bin/env python3

# - This is not accurate do to the 1 beat being
# Accented with A beep instead of A pulse,
# which takes more time.
# - 60 seconds in A minute.

print("Loading...")
from gpiozero import Buzzer, LEDBoard
from time import sleep
from sys import argv, stdout

buzzer = Buzzer(21)
leds = LEDBoard(4, 18, 6, 13)
usage = "You forgot to specify the tempo. Use as:\n$ ./buzzer-metronome.py [0.1-1]"
try:
  bpm = float(argv[1])
except IndexError:
  print(usage)
  exit()

print("Starting, press Ctrl-C to exit.")
beat = 1
measure_count = 1
print("measure: 1")

def flashBeep(led_num):
  stdout.write("\33[2K\r" + str(beat))
  stdout.flush()
  leds[led_num].on()
  buzzer.on()
  sleep(bpm)
  leds[led_num].off()
  buzzer.off()
  stdout.write("\33[2K\r")

while True:
  try:
    if beat == 1:
      stdout.write("\33[2K\r" + str(beat))
      leds[0].on()
      buzzer.beep(0.009, 0.009, 1)
      sleep(bpm)
      leds[0].off()
      beat = beat + 1
      stdout.write("\33[2k\r")
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
      measure_count = measure_count + 1
      print(measure_count)
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
