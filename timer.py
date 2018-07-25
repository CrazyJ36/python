#!/usr/bin/env python3

import time

num = 0

while (num < 10):

  if num == 5:
    print(str(num) + " half")

  if num > 0 and num is not 5:
    print(num)

  time.sleep(1)
  num = num + 1
print("10 Seconds Reached")
