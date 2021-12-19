#!/usr/bin/env python

from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

buzzer = TonalBuzzer(pin=19, initial_value=None, mid_tone=Tone('A4'), octaves=1)

print("Playing: A4...")
buzzer.play(Tone("A4"))
sleep(1)

print("...B4")
buzzer.play("B4")
sleep(0.5)

print("...C4")
buzzer.play(Tone(frequency=523))
sleep(0.5)

print("...E4")
buzzer.play("E4")
sleep(1)

print("Done, exiting...")
buzzer.stop()
buzzer.close()
exit()
