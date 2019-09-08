#!/usr/bin/env python3

# This program demonstrates how to cleanly exit A program
# with the press of Ctrl-C, useing try/except KeyboardInterrupt.

from time import sleep

number = 0

print("A counter is starting, press Ctrl+C to stop it and exit")

# print-sleep-increment loop works after While and try because the
# try statement IS GOING TO happen while true. Don't let the placement
# of while and try confuse you; Normally A beginner program would have
# print-sleep-increment right after while.
while True :
  try:
    print(number)
    sleep(0.5)
    number = number + 1
  except KeyboardInterrupt:
    print("Ctrl-C pressed, the program will now exit...")
    exit(0)


