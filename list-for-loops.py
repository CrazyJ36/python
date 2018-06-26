#!/usr/bin/env python3

# to perform operations on each item in a list,
# you can use A loop with A iteration counter

words = ["hello", "world", "foo", "bar"]
print("initial list:", words)

counter = 0

print("adding '!' to each item:")
while counter < 4:
  print(words[counter] + "!")
  counter += 1

print("done")
