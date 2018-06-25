#!/usr/bin/env python3

intList = [1,2,3]

print("initial list: " + str(intList)) # must be str, not list or type
# list items can be reassigned

print(intList + [4,5]) # temp print list with more indexes
intList.append(6) # permenently add a 6 to list.
		  # Using .method from function on python
intList[1] = 4
print("intList[1] =: " + str(intList[1]))

print("new list: " +  str(intList))

print("list many times" + (str(intList) * 2)) # concatenated so list
# is repeated

print(intList * 3) # this shows the list many times as one
