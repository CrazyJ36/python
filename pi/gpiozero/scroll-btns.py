#!/usr/bin/env python3
from gpiozero import Button, LEDBoard
from time import sleep

leds = LEDBoard(15, 21, 19, 4)

print("""Press right button to alternate through LEDs'.
Press left button to exit""")

def led_flash(x):
  leds[x].on()
  sleep(0.5)
  leds[x].off()

while True:

  btn1 = Button(14)
  btn2 = Button(26)

  if btn1.is_pressed:

    led_flash(0)
    led_flash(1)
    led_flash(2)
    led_flash(3)

  if btn2.is_pressed:
    print("Exiting..")
    exit(0)

  btn1.close()
  btn2.close()

