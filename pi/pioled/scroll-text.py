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

x = 0
while x < 50:
  # set A canvas for drawing
  # Parameters:
  # mode: mode="1" is 1 bit black and white
  # size: tuple containing pixels.
  # color: canvas color. 0 is black as this would be the background for actual image objects.
  image = Image.new(mode="1", size=(display.width, display.height), color=0)
  draw = ImageDraw.Draw(image)
  #fill=255 means fill white, which is what we need for the monochrome pioled mini.
  draw.text((x, 0), "text", font=ImageFont.load_default(), fill=255)
  # set actual display image to contents of PIL image.
  display.image(image)
  display.show()
  sleep(0.005)
  display.fill(0)
  display.show()
  del image, draw
  x = x + 3
