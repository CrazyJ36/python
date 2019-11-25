#!/usr/bin/env python3

def add(x, y):
  return x + y

y = 2
name = add
print(name(3, y))

# functions can be arguments of other functions
def myPrint():
  print(add(2, 2))

myPrint()
