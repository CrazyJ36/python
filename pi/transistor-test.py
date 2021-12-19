from gpiozero import LED
from time import sleep

pin = LED(4)

sleep(5)

pin.on()
sleep(5)
pin.off()
sleep(5)
pin.on()
sleep(5)
pin.off()

exit()
