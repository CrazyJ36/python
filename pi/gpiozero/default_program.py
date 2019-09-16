# 'default_program' means this my constantly running program
# that starts on boot. As an attempt to use attached hardware
# on Raspberry PI with purpose
# This is set to run on boot at:
# /etc/rc.local

from gpiozero import LED
from time import sleep

led1 = LED(24)
led2 = LED(7)

x = 1
while(x < 5):
  led1.on()
  sleep(0.3)
  led1.off()
  led2.on()
  sleep(0.3)
  led2.off()
  x = x + 1

exit()
