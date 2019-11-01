#!/usr/bin/env python3

intList = [1,2,3]

def normalList():
  print("initial list: " + str(intList)) # must be str, not list or type
# list items can be reassigned
normalList()

print(intList + [4,5]) # temp print list with more indexes
intList.append(6) # permenently add a 6 to list.
		  # Using .append METHOD from function on python
print(len(intList)) # len() is FUNCTION, not method

intList[1] = 4
print("intList[1] =: " + str(intList[1]))

print("new list: " +  str(intList))

print("list many times" + (str(intList) * 2)) # concatenated so list
# is repeated

print(intList * 3) # this shows the list many times as one

normalList()

# .insert(index, data) method can insert data at any index
intList.insert(1, 7)

normalList()

# new list

newList = ['1','2','3']
print(newList.index('1')) # prints the index position number of item
print(newList.index('3'))

