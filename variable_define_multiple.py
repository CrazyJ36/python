#!/usr/bin/env python3

# define multiple varables in-line:
# known as packing/unpacking
x, y, z = 2, 'hi', 4.2
print(x,y,z)

# Aother trick
# 1st equals next and next equals two.
# values refer to same instance.
a = b = c = 2
print(a, b, c)
