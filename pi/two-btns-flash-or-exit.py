#!/usr/bin/env python3
from gpiozero import Button
from gpiozero import LED
from time import sleep

btn = Button(22)
btn2 = Button(24)
led = LED(16)

print("""
From left-to-right,
press button 1 for led 4,
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
