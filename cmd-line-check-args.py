#!/usr/bin/env python3

import sys

print("""This program is to be run
with some command line arguments.""")

# check for no arguments(try, except)
'''

try:
  my_arg = sys.argv[1]
except IndexError:
  print("No arguments")
  sys.exit(0)

'''
# another way to check for empty args(if len(sys.argv))
if len(sys.argv) > 1:
  my_arg = sys.argv[1]  # or print(sys.argv[1])
else:
  print("No arguments")
  sys.exit()

# print first command line argument
print("The first arg was:", my_arg)
