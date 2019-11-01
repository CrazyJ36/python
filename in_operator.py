#!/usr/bin/env python3

# To check if an item is in a list, the in operator can be used. It
# returns true if the item occurs one or more times in the list, and
# false if it doesn't.
#
# The in operator is also used to determine whether
# or not a string is a substring of another string.

charList = ['a','b','c']
print('b' in charList) # prints boolean true, there is 'b' in list.
print('d' in charList) # prints boolean false, no 'd' in list

# 'in' examples
if 'a' in charList:
  print("theres an a")
if not 'd' in charList:
  print("no 'd'")
if 'f' not in charList or not 'f' in charList: #same expression,
					       # different order.
  print("no f in charList array")
