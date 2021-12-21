#!/usr/bin/env python

import board
import busio
import adafruit_ssd1306
from time import sleep
import operator

# parameters (pixel_width, pixel_height, interface, hardware_address)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, busio.I2C(board.SCL, board.SDA), addr=0x3c)

# Clear previous pixels by fill(0), 0 means fill with 'off' black, fill(1) would fill with 'on'(white screen)
display.fill(0)
display.show()

def drawLine(x_value):
  global x
  global y
  x = x_value
  y = 16

  i = 0
  while i < 10:
    display.pixel(x, y, 1)
    display.show() # no sleep() needed to keep for loop updates, animates as fast as console prints.
    x = x + 1
    y = y + 1
    i = i + 1

  i = 0
  while i < 10:
    display.pixel(x, y, 1)
    display.show()
    x = x + 1
    y = y - 1
    i = i + 1

  print("X axis pixel position: " + str(x))

# run drawLine on loop.
runDrawLine = 0
z = 0
while runDrawLine < 6:
  drawLine(z) # using print(x) each time drawLine() runs to find out where x has iterated to next.
  z = z + 20
  runDrawLine = runDrawLine + 1

print("ZigZag drawn, showing for 3 seconds!")
sleep(3)
display.fill(0)
display.show()
