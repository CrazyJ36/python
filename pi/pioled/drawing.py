#!/usr/bin/env python

print("Loading...")
import board
import busio
import adafruit_ssd1306
from time import sleep

# parameters (pixel_width, pixel_height, interface, hardware_address)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, busio.I2C(board.SCL, board.SDA), addr=0x3c)

# Clear previous pixels by fill(0), 0 means fill with 'off' black, fill(1) would fill with 'on'(white screen)
display.fill(0)
display.show()

# Available methods, from the FrameBuffer class in /usr/local/lib/python[version]/dist-packages/adafruit_framebuf.py:

# rotation(int), avaible params: 0, 1, 2, 3. Flips display for viewing at 4 different angles.

# fill(int), available params: 0, 1. 0 is black, 1 is white. Fills entire display with color.

# fill_rect(x_position, y_position, width, height, color), A filled rectangle.

# pixel(x, y, color). Draws 1 pixel on screen.

# hline(x , y, width, color). Draws horizontal line.

# vline(x, y, height, color). Draws vertical line.

# circle(center_x, center_y, radius, color). Draws circle at the given midpoint location.

# rect(left_top_corner__position, lef_top_corner_postition, width, height, color).
# Draws an open rectangle with A 1 pixel outline.

# blit(). Not yet implemented.

def scrollTest():
  # create character
  display.rect(20, 16, 30, 10, 1)
  display.show()
  # scroll(x_change, y_change).
  # moves framebuffer by A positive or negative numer of pixels along the x or y axis. don't move it too much
  # or framebuffer seems to overlap previous drawings. Plus this slow even when not using time.sleep() at all.
  move_count = 0
  while move_count < 5:
    display.scroll(5, 0)
    display.show()
    move_count = move_count + 1

  display.fill(0)
  display.show()

def textTest():
  # text(string, x_position, y_position, color, font_name="font.ttf", size=1). Must download the default font file
  # from https://github.com/adafruit/Adafruit_CircuitPython_framebuf/raw/main/examples/font5x8.bin
  # IF size of this font file from running 'ls -l' doesn't equal 1282bytes, try downloading again by using the
  # link address attached to the 'Download' button on the Github page.
  display.text("Text", 64, 16, 1, size=1)
  display.show()

  sleep(1)
  display.fill(0)
  display.show()

def lineTest():
  # line(x_0, y_0, x_1, y_1, color). Draws line using specified starting(x_0, y_0)
  # and ending(x_1, y_1) grid points.
  display.line(64, 16, 80, 20, 1)
  display.show()

  sleep(1)
  display.fill(0)
  display.show()

def fillTest():
  display.fill(1)
  display.show()
  sleep(1)
  display.invert(True)


print("scrolling object...")
scrollTest()
print("showing text")
textTest()
print("showing line")
lineTest()
print("filling screen")
fillTest()

print("Exiting")
exit()
