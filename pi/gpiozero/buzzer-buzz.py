#!/usr/bin/env python3

from gpiozero import Buzzer
from time import sleep

bz = Buzzer(2)
bz.beep(0.005,0.005,50, False)
