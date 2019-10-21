#!/usr/bin/env python3

# using 'with open(file) as file_ojb'
# enables 'context manager' capabilities and getting handle.


try:
  file = open("/home/thomas/junk/tst.txt")
  file.close()
except FileNotFoundError:
  print("tst.txt not found in ~/junk")
  exit(0)

file = open("/home/thomas/junk/tst.txt")
text = file.read()
file.close()
print("Whole file:")
print(text, end='')

