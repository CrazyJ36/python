#!/usr/bin/env python

import board
import busio
import adafruit_ssd1306
from time import sleep

display = adafruit_ssd1306.SSD1306_I2C(128, 32, busio.I2C(board.SCL, board.SDA), addr=0x3c)
print("clearing screen")
display.fill(0)
display.show()

print("showing pixel")
display.pixel(64, 16, 1)
display.show()
sleep(1)

print("inverting")
display.invert(True)
#display.show()
sleep(1)

print("clearing screen")
display.pixel(64, 16, 0)
display.show()
display.invert(False)
print("Done")


