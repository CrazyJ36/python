#!/usr/bin/env python3

from os import listdir, path
from sys import argv

num_args = len(argv)

if num_args is not 2:
  print("Enter one directory as program argument. Exiting...")
  exit(0)


try:

  for f in listdir(argv[1]):
      print(f)

except FileNotFoundError:
  print("Not A directory. Exiting...")
  exit(0)


exit(0)
