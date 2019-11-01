#!/usr/bin/env python3

def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

filename = "tst.txt"
with open(filename) as f:
  text = f.read()
print("There are ", end='')
print(count_char(text, "a"), end='')  # uses the text count function from count_char, "a" is chosen character to look for.
print(" 'a's in tst.txt")