#!/usr/bin/env python3

if 1 < 2:
  print("1 is less than 2")
elif 1 < 3: # this does'nt get tested in else if as the first one was true
  print("1 is less than 3")
else:
  print("nothing is possible")
