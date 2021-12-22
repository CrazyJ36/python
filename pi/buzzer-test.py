#!/usr/bin/env python3

from gpiozero import Buzzer

bz = Buzzer(21)
bz.beep(0.01,0.01,5, False)
