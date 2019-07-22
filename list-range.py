#!/usr/bin/env python3

# 'list(range(int)' creates A numbered list.

# Makes a int list with 6 items.
nums = list(range(6))

# Print the new list.
print("New list, 6 items:\n>>> nums = list(range(6))\n", nums)

# Print 2nd index position of nums list.
print("\nPrint list item at 2nd index position:")
print(">>> nums[2]\n", nums[2])

# Range can be defined with A specific range of numbers.
# This starts at 2, ends before 6.
nums2 = list(range(2,6))
print("\nNew list whos' indexes range from only 2 to 6:")
print(">>> nums2 = list(range(2,6))\n", nums2)

# A third argument specifies the interval sequence of range.
nums3 = list(range(2,10,2))
print("\nA third range argument defines skipped intervals:")
print("This means 'A range from 2 to 10, in sequences of 2")
print(">>> nums3 = list(range(2,10,2))\n", nums3)

# Test that new range of 10 numbers is same as new range 0-10.
print("\nIs 'range(10)' the same as 'range(0,10)'?:")
print(range(10) == range(0,10))
