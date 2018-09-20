#!/usr/bin/env python3

try:
  file = open("/home/thomas/junk/tst.txt")
  file.close()
except FileNotFoundError:
  print("tst.txt not found in ~/junk")
  exit(0)

file = open("/home/thomas/junk/tst.txt")
text = file.read()
file.close()
print(text, end='')

