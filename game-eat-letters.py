import time
import sys

sprite = 'O'
food = '-'

i = 10
while i > 0:
  i = i - 1
  print(sprite + food * i, end="")
  print("\0", end="\r") # Removes any line content
  time.sleep(0.5)