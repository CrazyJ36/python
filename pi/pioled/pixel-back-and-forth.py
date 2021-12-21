#!/usr/bin/env python

# This example doesn't use the slower PIL library which would cause
# flickering in character movement.
print("Loading")
import board
import busio
import adafruit_ssd1306
from time import sleep

display = adafruit_ssd1306.SSD1306_I2C(128, 32, busio.I2C(board.SCL, board.SDA), addr=0x3c)

display.fill(0)
display.show()

print("Animating A zigzag...")
x = 0

print("x start: " + str(x))

while x < 128:
  print(x)
  display.pixel(x, 16, 1)
  display.show()
  sleep(0.0000001)
  display.fill(0)
  x = x + 1
while x > 0:
  print(x)
  display.pixel(x, 16, 1)
  display.show()
  sleep(0.0000001)
  display.fill(0)
  x = x - 1

display.show()
print("x end: " + str(x) + "\n" + "Done.")
