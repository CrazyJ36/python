#!/usr/bin/env python3
from gpiozero import Button
from gpiozero import LED
from time import sleep

btn = Button(23)
btn2 = Button(27)
led = LED(24)

print("""
From left-to-right,
press button 1 for led 1,
button 2 to exit.
""")

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
