#!/usr/bin/env python3
from gpiozero import Button
from gpiozero import LED
from time import sleep

# Buttons are 14 and 26
btn = Button(27)
btn2 = Button(24)
led = LED(22)

print("press right button for led, left button to exit")

while True:
  if btn.is_pressed:
    led.on()
    sleep(0.1)
    led.off()
  elif btn2.is_pressed:
    btn.close()
    led.close()
    print("done")
    exit(0)
