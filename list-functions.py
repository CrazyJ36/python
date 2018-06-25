#!/usr/bin/env python3

nList = ['c','b','a']

def printnList():
  print(nList)

print("Initial list:")
printnList()

# to concatenate as string use plus
print("\n2nd item index: " + str(nList.index('b')))

# this print statement doesn't require concatenation
# so comma is used.
print("3rd item index: ", nList.index('a'))

# max() list function returns the item
# in the list with the highest integral value.
print("Item with max() value(ascii):", max(nList))

# min(list) list function returns the list item
# with the minimum value
print("List item with minimum value:",  min(nList))

print("Appending 'b' to list\nNew List:")
nList.append('b')
printnList()

# list.count(obj) returns number of times am item occurs in A list.
print("Item 'b' occurs", nList.count('b'), "times.")
