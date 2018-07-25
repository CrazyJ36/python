#!/usr/bin/env python3

# int(function()) states that the str will return as int
var = int(str("2"))
print("Value of: int(str(\"2\")):\n", type(var))

# take input as only integer
try:
  num1 = int(input("type a number: "))
  num2 = int(input("another number: "))
  print(num1, num2)
except ValueError:
  print("Input was not int")
  exit()

exit()
