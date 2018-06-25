#!/usr/bin/env python3

# Lists in python are the same as arrays in other languages.
# define A list usinf square brackets and commas for any type
#   of values.
# Values of A list can be accessed by using indsx values starting
#   from 0.

nums = [1,2,3]
print(nums[1]) # print second index, 2.

strings = ["one", "two", "three",] # comma after last
				   # item is optional, but valid.
print(strings[1])

characters = ['a','b','c']
print(characters[1])

place_holder = [] # empty list
print(place_holder)

# list of lists, can be used for 2d grids
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])  # second index: 0
print(things[2])  # 3rd index, a list in the things[] list: [1,2,3]
print(things[2][2]) # second index(embeded list), second index of that: 3

# strings can be treated like a list
str = "string"
print(str[2]) # third character in string

# you can't call an index position that does not exist,
#   this causes an out-of-bounds error.
