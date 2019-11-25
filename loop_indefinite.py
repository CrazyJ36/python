#!/usr/bin/env python3

# i definite loop run until SIGSTOP (ctrl-c)
# this is so a program can do
# things whenever the user make a
# condition true.

# this loops ask for a character until the character is q
str = ""

while str != 'q':
  print("looping, type q to stop")
  str = input("")

print("done")
