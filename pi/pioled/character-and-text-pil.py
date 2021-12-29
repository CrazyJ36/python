#!/usr/bin/env python

# board stuff
from board import SCL, SDA
from busio import I2C
import adafruit_ssd1306
from time import sleep
from PIL import Image, ImageDraw, ImageFont

i2c = I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
display.fill(0)
display.show()

image = Image.new("1", (display.width, display.height))
draw = ImageDraw.Draw(image)

# Not possible due to PIL.Image taking whole screen
#display.pixel(0, 0, 1)

# Text
draw.text((64, 14), "text", font=ImageFont.load_default(), fill=255)
# Character
draw.rectangle([(0, 0), (10, 10)], fill=255, width=2)

display.image(image)
display.show()

sleep(3)
display.fill(0)
display.show()
exit()
