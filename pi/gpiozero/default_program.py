# 'default_program' means this my constantly running program
# that starts on boot. As an attempt to use attached hardware
# on Raspberry PI with purpose
# This is set to run on boot at:
# /etc/rc.local

from gpiozero import LED, Button
from time import sleep

led = LED(6)
btn = Button(8)

while True:
  led.on()
  sleep(1)
  led.off()
  sleep(1)
  if btn.is_pressed: exit()
