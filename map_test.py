#!/usr/bin/env python3

# The library module function 'map' takes A function and
# an iterable as arguments, returns A new iterable with
# the function applied to each argument.


nums = [2, 5, 1]

# the function adds one to any arg.
def add_one(x):
  return x + 1

# map function taking add_one as it's function to act on,
# with the parameter nums for add_one.

# This is converted to list with list(items) to be printable.
result = list(map(add_one, nums))

print(result)
