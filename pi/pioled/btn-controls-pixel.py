#!/usr/bin/env python

import board
from busio import I2C
import adafruit_ssd1306
from gpiozero import ButtonBoard
from time import sleep

btns = ButtonBoard(17,16)

display = adafruit_ssd1306.SSD1306_I2C(128, 32, I2C(board.SCL, board.SDA), addr=0x3c)

display.fill(0)
display.show()

x = 64
y = 16
display.pixel(x, y, 1)
display.show()

print("Pixel showing, press button 1 or button 2 to move it.\nCtrl-C to exit...")
try:
  while btns.wait_for_press:
    if btns[0].is_pressed:
      display.fill(0)
      x = x - 1
      display.pixel(x, y, 1)
      display.show()
    elif btns[1].is_pressed:
      display.fill(0)
      x = x + 1
      display.pixel(x, y, 1)
      display.show()
except KeyboardInterrupt:
  print("Exiting")
  display.fill(0)
  display.show()
  for i in btns:
    i.close()
