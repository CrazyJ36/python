#!/usr/bin/env python

# This example doesn't use the slower PIL library which would cause
# flickering in character movement.
print("Loading")
import board
import busio
import adafruit_ssd1306
from time import sleep
import itertools

display = adafruit_ssd1306.SSD1306_I2C(128, 32, busio.I2C(board.SCL, board.SDA), addr=0x3c)

display.fill(0)
display.show()

print("Animating two points...")
x = 0
y = 0

print("x, y start: " + str(x) + ", " + str(y))

while x < 129:
  display.pixel(x, 0, 1)
  if y < 33:
    display.pixel(0, y, 1)
    y = y + 1
  display.show()
  sleep(0.00001)
  display.fill(0)
  x = x + 1

print("x, y end: " + str(x) + ", " + str(y) + "\n" + "Done.")
