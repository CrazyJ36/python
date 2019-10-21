#!/usr/bin/env python3

filename = input("Enter filename to open: ")
try:
  file = open(filename, 'r')
except FileNotFoundError:
  print("No such file. Exiting...")
  exit(0)
print("File contents:\n" + file.read())
file.close()
