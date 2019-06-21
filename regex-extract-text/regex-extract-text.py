#!/usr/bin/env python3

# Guide:
# ^  -  Match from/at beginning of line
# $  -  Match at end of line
# .  -  Match any character (wildcard)
# \s -  Match white-spase characters (include spaces)
# \S -  Match non white-spase
# *  -  Repeat looking for character zero or more
#       times(so .* is like bash wildcard)
# *? -  Repeats A character zero or more(non-greedy form)
# [aeiou] - Match A single character in A the set
# [^XYZ]  - Match A single characternot listed in set
# [a-z0-9] - The set of characters can include A range
# ( - Indicates where string exctract should start
# ) - Indicates where string extraction should end


# import pythons' regular expression library
import re

# print whole file for conparison later
file = open("text.txt")
print("this is the file content we're working with:\n")
for line in file:
  print(line, end='')

del line
file.close()
print("\n")

# Start extracting text
print("getting only 'sender names' from conversation:\n")
file = open("text.txt")
# get lines from file
for line in file:
# strip lines into strings
  line = line.rstrip()
# if any line has "from:" text, print it
  if re.search('from:', line):
    print(line)

# exit
del line
file.close()
print("\nDone. Exiting...")
exit(0)
