#!/usr/bin/env python

import board
import busio
import adafruit_ssd1306
from time import sleep

# parameters (pixel_width, pixel_height, interface, hardware_address)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, busio.I2C(board.SCL, board.SDA), addr=0x3c)
# Clear previous pixels by fill(0), 0 means fill with 'off' black, fill(1) would fill with 'on'(white screen)
display.fill(0)
display.show()

print("Turning pixel 0, 0 on")
display.pixel(0,0,1)
display.show()

# instead of using display.fill(0) within the app, control only the active pixels to save processing power.
sleep(1)
print("Turning pixel 0, 0 off")
display.pixel(0,0,0)
display.show()

print("Done")


