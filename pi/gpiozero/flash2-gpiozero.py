# requires to install python3-gpiozero

from gpiozero import LED
from time import sleep

led1 = LED(17)
led2 = LED(27)

x = 0
while(x < 5):
  led1.on()
  sleep(1)
  led1.off()

  led2.on()
  sleep(1)
  led2.off()
  x = x + 1

exit()
