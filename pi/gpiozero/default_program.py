# 'default_program' means this my constantly running program
# that starts on boot. As an attempt to use attached hardware
# on Raspberry PI with purpose
# This is set to run on boot at:
# /etc/rc.local

from gpiozero import LED, Button
from time import sleep
from subprocess import call

led = LED(6)
btn1 = Button(23)
btn2 = Button(27)
btn3 = Button(22)
btn4 = Button(25)
btn5 = Button(
def flash():
  led.on()
  sleep(0.1)
  led.off()
  sleep(0.1)


while True:
  if btn.is_pressed:
    print
