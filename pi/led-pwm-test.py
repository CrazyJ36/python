#!/usr/bin/env python
print("Loading...")
from gpiozero import PWMLED

led = PWMLED(16)
print("LED 4 will pulse 3 times.")
led.pulse(fade_in_time=1, fade_out_time=1, n=3, background=False)

print("Done!")
led.close()
exit()
