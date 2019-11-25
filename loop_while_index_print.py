#!/usr/bin/env python3

# to perform operations on each item in a list,
# you can use A loop with A iteration counter

words = ["hello", "world", "foo", "bar"]
print("Initial list:", words)

counter = 0

# access list items in loop through their indices ,
# print them with additional vharacter
print("Adding '!' to each item:")
while counter < 4:
  print(words[counter] + '!')
  counter += 1

print("done")
