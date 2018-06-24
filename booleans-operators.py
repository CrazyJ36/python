#!/usr/bin/env python3

# and, or, not

if 1 < 2 and 1 < 3:
  print("true")
else:
  print("false")

if 1 < 0 or 1 > 2:
  print("true")
else:
  print("false")

if 1 is not 2:
  print("true")

if 1 != 2:
  print("true")

if not 1 < 0:  # "not <expr>" means false
  print("1 is not less than 0")
