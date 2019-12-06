#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
buzzer = 19
GPIO.setup(buzzer, GPIO.OUT)
while True:
  GPIO.output(buzzer, GPIO.HIGH)
  print("Beep")
  sleep(0.5)
  GPIO.output(buzzer, GPIO.LOW)
  print("No beep")
  sleep(0.5)


