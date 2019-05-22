#!/usr/bin/env python3
# Requires Python2
# Usage: $ chmod +x flash4PWM.py; ./flash4PWM.py
import RPi.GPIO as GPIO
from time import sleep

# Choose pin # to light
pin = 15
# Must always setup your used gpio pin..
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

# Pulse width modulation is an sequence on, then off pulses.
# The pi zero has probably 4 pins that can output as PWM.
# In this example I'm using an LED to visualize the pulses.

# Here, the GPIO.PWM() function takes two parameters:
# the pin number(A pin with PWM), and the frequency(rate of pulse).

# I chose 10 as the frequency here as 10hz can easyily be recognized
# visually(like A subwoofer moving in/out at 10hz.).
pwm = GPIO.PWM(pin, 10)

# The parameter in .start() is the percentage of time that the 'on'
# pulse lasts against the total length of the frequency pulse.
# Called Duty Cycle.
# It can do A short 'on' pulse, then A long off pulse, repeatedly.
# Or vice versa. This can also simulate LED brightness control by
# using A fast frequency, which would appear on most of the time,
# then by giving only short bursts of power during this fast movement
# the LED would appear dimmer.

# This the following loop will simulate A 10hz pulse, on and off evenly
# 50 means 'on for 50 percent of the pulse'.
# sleeping for 0.1th of A second gives this some time to run.
print("Pulsing LED 18 on-off evenly at 10hz..")
x = 0
while x < 30:
  pwm.start(50)
  print(x, "/30")
  sleep(0.1)
  x = x + 1

pwm.stop()

print("Giving LED A 1sec break...")
sleep(1)

# pwm.start(2)'s param  makes the led on for only 2 percent of the
# time of each pulse, making it appear dimmer.
# looping through 'x' A higher number of times as A 100hz pulse
# would go by faster, and this still should last viewable while.
print("100hz, with less time on during each pulse, makes led dimmer..")
pwm.ChangeFrequency(100)

x = 0
while x < 40:
  pwm.start(2)
  print(x, "/40")
  sleep(0.1)
  x = x + 1

pwm.stop()
print("done..")

GPIO.cleanup()
print("GPIO cleaned-up. Bye!")

exit(0)
