from gpiozero import Button, LED
from time import sleep

led = LED(24)
btn = Button(23)

while True:
  if btn.is_pressed:
    led.on()
    sleep(1)
    led.off()

  s = input("press any key to quit")
  if s:
    exit(0)


