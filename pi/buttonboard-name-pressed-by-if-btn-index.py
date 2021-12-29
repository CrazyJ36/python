#!/usr/bin/env python3

# also, use 'function(**kwargs)' like
# function(name1 = value1, name2 = value2)
# should be able to get named buttons from key/value
print("Loading GpioZero..")
from time import sleep
from gpiozero import ButtonBoard, LED

btns = ButtonBoard(17, 25, 24, 16)
led = LED(4)

print("Press any button, Led will flash times of buttons number.")
print("And Ctrl-C to exit...")
def flashTimes(times):
  x = 0
  while x is not times:
    sleep(0.1)
    print(x + 1)
    led.on()
    sleep(0.2)
    led.off()
    x = x + 1
  print("Press another...")

while True:
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

  except KeyboardInterrupt:
    print("\rExiting")
    exit(0)
