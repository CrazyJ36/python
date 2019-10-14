#!/usr/bin/env python3

# This test my "organized" hardware setup on perma-proto

print("Loading.. Press Ctrl-c to exit A test.\n")
import sys
from time import sleep
from signal import pause
from gpiozero import Button, ButtonBoard, LEDBoard, Buzzer


usage = "Command error..\nUsage: ./perma-proto-org... [leds, buttons, buzzer, all]"
try:
  cmd = sys.argv[1]
except IndexError:
  print(usage)
  exit(0)


try:
  leds = LEDBoard(4, 18, 24, 11, 12, 7, 16, 6)
  btns = ButtonBoard(23, 27, 22, 25, 9, 5, 8)
  buzz = Buzzer(2)
except Exception:
  print("gpiozero or pin didn't load correctly, Exiting..")
  exit(0)


def test_leds():
  try:
    print("\nTotal desired LEDs: ", end='' )
    print(len(leds))
    print("Flashing All LEDs in order 3 times, watch PI..")
    sleep(1)
    i0 = 0
    while i0 < 3:
      i1 = 0
      while i1 < len(leds):
        leds[i1].on()
        sleep(0.3)
        leds[i1].off()
        i1 = i1 + 1
      i0 = i0 + 1
  except KeyboardInterrupt:
    print("Exiting..\n")
    return


def test_btns():
  print("\nTesting Buttons...")
  print("Total desired button devices: ", end='')
  print(len(btns))
  print("Press any push button on the board, you'll see it active in A list of all.")
  while True:
    try:
      if btns.is_pressed:
        print(btns.value)
        sleep(0.2)
    except KeyboardInterrupt:
      print("Exiting\n\n")
      return

def test_buzz():
  print("Testing Buzzer.. Beep(repeated on/off) for A short time...")
  buzz.beep(0.005, 0.005, 50, False)
  return

# Switch Method Reference
'''
def test_switch():
  print("Toggle the switch(the one on the right of the two)")
  try:
    while True:
      if switch.is_pressed:
        print("Switch is on")
        switch.wait_for_release()
      else:
        print("Switch is off")
        switch.wait_for_press()

  except KeyboardInterrupt:
    print("\nExiting..\n")
    return
'''

if cmd == "leds":
  test_leds()
elif cmd == "buttons":
  test_btns()
elif cmd == "buzzer":
  test_buzz()
elif cmd == "all":
  test_leds()
  test_btns()
  test_buzz()
else:
  print(usage)
  exit(0)


exit(0)
