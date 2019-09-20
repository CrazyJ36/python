#!/usr/bin/env python3
from time import sleep

print(
"""
\nNormally(on linux) when you press ctrl-c to exit A program,
your left with an ugly '^' in your terminal to
signify that you pressed ctrl-c.
That symbol can be removed when you signify that
you're exiting the program with A return escape
character \\r.
Try/Catch(except) Keyboard Interrupt and use:

>>  print("\\rExiting")
>>  exit(0)

The '\\r' in print("Exiting") will return line, and be pretty.\n
""")
while True:
  try:
    print("Press ctrl-c")
    sleep(1)
  except KeyboardInterrupt:
    print("\rExiting..")
    exit(0)


