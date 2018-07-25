#!/usr/bin/env python3.7

instruct = "Enter x, y, or something else: "
str1 = input(instruct)

def checkStr(str1):
  if (str1 is 'x'):
    print("typed x")
  elif (str1 is 'y'):
    print("typed y")
  else:
    print("typed neither x or y")

checkStr(str1)
