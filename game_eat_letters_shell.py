#!/usr/bin/env python3

import time
import sys
import os

sprite = '(8>{'
food = '-'

os.system('setterm -cursor off')

i = 10
while i > 0:
  i = i - 1
  print(sprite + food * i, end="\r")
  time.sleep(0.5)
  print("\033[K", end="\r")

os.system('setterm -cursor on')
