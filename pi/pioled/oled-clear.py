from board import SCL, SDA
import busio
import adafruit_ssd1306

# create I2C interface
i2c = busio.I2C(SCL, SDA)

# create OLED class
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# clear display
disp.fill(0)
disp.show()

