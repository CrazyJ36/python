# import board, io, and adafruit drivers
from board import SCL, SDA
import busio
import adafruit_ssd1306

from time import sleep

# create i2c interface and set display properties
i2c = busio.I2C(SCL, SDA)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear previous pixels
display.fill(0)
display.show()

# moving pixel
display.pixel(0,0,1)
display.pixel(64, 16, 1)
display.pixel(127, 31, 1)
display.show()
