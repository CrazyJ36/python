#!/usr/bin/env python3

# Make A quick list with to power of amount rule in range

nums = [i*2 for i in range(10)]
print(nums)

# example with if in-line:
# evens=[i**2 for i in range(10) if i**2 % 2 == 0]

# new list up to 5 with values all equalling default + 1.
# This will be 1-5
nums2 = [i+1 for i in range(5)]
print(nums2)
# While this would be 0-4 as default range makes
for i in range(5):
  print(i, end='')

print()  # default new line
