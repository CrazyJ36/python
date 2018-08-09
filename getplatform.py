#!/usr/bin/env python3

import sys

if sys.platform == 'linux':
  print("Your using Linux.")

elif sys.platform == 'win32':
  print("Your using Windows.")

else:
  print("Your using an OS unknown by this program developer")
