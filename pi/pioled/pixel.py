import board
import busio
import adafruit_ssd1306

# parameters (pixel_width, pixel_height, interface, hardware_address)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, busio.I2C(board.SCL, board.SDA), addr=0x3c)

# Clear previous pixels by fill(0), 0 means fill with 'off' black, fill(1) would fill with 'on'(white screen)
display.fill(0)
display.show()

# create and show pixel.
# parameters are (x_position, y_position, pixel_color(0=black, 1=white)
display.pixel(0,0,1)
display.show()
