#!/usr/bin/env python3

# The range function creates A sequential list of numbers.

# This example calls list in order to convert the range to A list.

# makes a int list with 6 items
nums = list(range(6))
# print list
print("number list:", nums)
# print index position of nums
print("2nd index of number list", nums[2]) # int index same as int list, because it's int

# A range can be defined with A specific range of numbers
nums2 = list(range(2,6))
print("new specific range of numbers 2-6, excludes 6: ", nums2)
# test algorithm. new range of 10 numbers is same as new range 0-10
print("test similarity: ", range(10) == range(0,10))

# A third argument specifies the interval spaced sequence of range
nums3 = list(range(2,10,2))
print("new intervalic range:", nums3)
