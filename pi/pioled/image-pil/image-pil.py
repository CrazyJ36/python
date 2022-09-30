#!/usr/bin/env python

# board stuff
from board import SCL, SDA
from busio import I2C
import adafruit_ssd1306

# using python imaging library (Pillow)to create drawing canvas
from PIL import Image

from time import sleep
i2c = I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
display.fill(0)
display.show()

# PIL open image
image = Image.open('img.png').resize((display.width, display.height)).convert('1')
# show the now buffered pixels for 3 seconds
display.image(image)
display.show()

# wait and exit
sleep(3)
display.fill(0)
display.show()
exit()
