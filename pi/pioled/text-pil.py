#!/usr/bin/env python

# board stuff
from board import SCL, SDA
from busio import I2C
import adafruit_ssd1306

# using python imaging library (Pillow)to create drawing canvas
from PIL import Image, ImageDraw, ImageFont

from time import sleep
i2c = I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
display.fill(0)
display.show()

# set A canvas for drawing
image = Image.new("1", (display.width, display.height))
draw = ImageDraw.Draw(image)

# Load A font. Parameters(str(ttf_font_path), int(font_size))
# font size with A single 'Z' char can go up to 34, 28 for the word 'CrazyJ36'.
font = ImageFont.truetype("/usr/share/fonts/truetype/arial.ttf", 28)

# buffer the text in the PIL way
draw.text((0, 0), "CrazyJ36", font=font, fill=255)

# set actual display image to contents of PIL image.
display.image(image)

# show the now buffered pixels for 3 seconds
display.show()

# wait and exit
sleep(3)
display.fill(0)
display.show()
exit()
