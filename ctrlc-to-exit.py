#!/usr/bin/env python3

# This program demonstrates how to cleanly exit A program
# with the press of Ctrl-C, useing try/except KeyboardInterrupt.

# for sys.exit(), the normal way to exit A python program/module or
#  the interpreter.
from sys import exit as end_prog
from time import sleep

number = 0

print("A counter is starting, press Ctrl+C to stop it and exit")

# print-sleep-increment loop works after While and try because the
# try statement IS GOING TO happen while true. Don't let the placement
# of while and try confuse you; Normally A beginner program would have
# print-sleep-increment right after while.
while True:
    try:
        print(number)
        sleep(0.5)
        number = number + 1
    except KeyboardInterrupt:
        # Notice the '\r' (return) escape character at the beginning of
        # this print string. This removes the '^' carat character
        # from your terminal output upon key press and exit.
        print("\rCtrl-C pressed, the program will now exit...")
        end_prog(0)  # end_prog as sys.exit()
