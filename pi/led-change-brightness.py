#!/usr/bin/env python

print("Loading")
from gpiozero import PWMLED
from time import sleep


print("LED4 will gradually increase in brightness")

# Long way:
#led = PWMLED(pin=16, active_high=True, initial_value=0.1, frequency=100)
#sleep(1)
#led.close()
#led = PWMLED(pin=16, active_high=True, initial_value=0.3, frequency=100)
#sleep(1)
#led.close()
#led = PWMLED(pin=16, active_high=True, initial_value=0.5, frequency=100)
#sleep(1)
#led.close()
#led = PWMLED(pin=16, active_high=True, initial_value=0.7, frequency=100)
#sleep(1)
#led.close()
#led = PWMLED(pin=16, active_high=True, initial_value=1, frequency=100)
#sleep(1)
#led.close()

led = PWMLED(16)

led.value = 0
i = 0
while i <= 1.1:
  led.value = led.value + 0.2
  print("LED Value[0-1]: " + str(led.value))
  sleep(1)
  i = led.value + 0.2

print("Exiting")
led.off()
led.close()
exit()
