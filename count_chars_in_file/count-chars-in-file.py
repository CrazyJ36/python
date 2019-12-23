#!/usr/bin/env python3

def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

with open("tst.txt") as f:
  text = f.read()

result = count_char(text, 'a')
print(result)