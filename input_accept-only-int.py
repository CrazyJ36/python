#!/usr/bin/env python3

# take input as only integer

print("This will accept only numbers, using:\nint(input())")
try:
  num = int(input("Type a number, or other type to see result: "))
  print("Input was int. No error: ", num)
except ValueError:
  print("ValueError thrown, Input was not int.\nInput handled succesfully.\nExiting..")
  exit()
