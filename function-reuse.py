#!/usr/bin/env python3

# the parameters(x,y) of myAdd can be set directly
# set when calling the function.
def myAdd(x, y):
  return x + y

y = 2
# assigning function to varaible
name = myAdd
print(name(3, y))

# functions can be arguments of other functions
def myPrint():
  print(myAdd(2, 2))

myPrint()
