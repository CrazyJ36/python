#!/usr/bin/env python2
from gpiozero import Button
from gpiozero import LED
from time import sleep
from signal import pause

# Buttons are 14 and 26
btn = Button(14)
btn2 = Button(26)
led = LED(15)

print "press right button for led, left button to exit"

while True:
  if btn.is_pressed:
    led.on()
    sleep(0.1)
    led.off()
  elif btn2.is_pressed:
    btn.close()
    led.close()
    print "done"
    exit(0)
