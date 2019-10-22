#!/usr/bin/env python3

# Sets can be used for testing lists' items for things like duplicates.
# Sets are like dictionaries, they both can be checked for items with 'in'.
# This shows the difference between set and dictionary and lists.
# Dictionary:
a_dict = {1,2,3}
print("Check for '2' item in: a_dict = {1,2,3}:")
print(2 in a_dict)
print()

# straight list can also use bool 'in':
print("try to use boolean 'in' in A list object(a_list = [1,2,3]:")
a_list = [1,2,3]
print(1 in a_list)
print()

# set converted from list.
a_set = set([1,2,3])
print("Check for '1' item in: a_set = set([1,2,3]) which is list converted to set:")
print(1 in a_set)
print()
print("Check for something that is not in a_set")
print(4 in a_set)
print()

print("To instantiate sets, you can use curly braces of the set([list]) function.")
print("Also to create empty set specifically use the set() function, A '{}' creates empty dictionary")
print()

print("""Sets are unordered, can't be indexed, cannot contain duplicate items(they will be removed).
Checking for items is faster in sets than list, due to how they're stored.
use add() instead of append() for sets. remove() works for sets items.
pop() removes arbitrary element.
""")

nums_set = set([1,1,4,5,3,4])
print("Items will be removed and reordered in set([1,1,4,5,3,4]), same as dict:")
print(nums_set)
print()

print("Regular list, anything goes. nums_list = [1,2,4,5,3,4]")
nums_list = [1,2,4,5,3,4]
print(nums_list)
