print("Loading")
import board
import busio
import adafruit_ssd1306
from time import sleep

display = adafruit_ssd1306.SSD1306_I2C(128, 32, busio.I2C(board.SCL, board.SDA), addr=0x3c)

display.fill(0)
display.show()

print("Showing horizontal range")
x = 0
while x < 129:
  print(x)
  display.pixel(x, 0, 1)
  display.show()
  sleep(0.00001)
  display.fill(0)
  x = x + 1

print("Showing vertical range")
y = 0
while y < 33:
  print(y)
  display.pixel(0, y, 1)
  display.show()
  sleep(0.00001)
  display.fill(0)
  y = y + 1

print("Turning off display")
display.fill(0)
display.show()
