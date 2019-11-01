#!/usr/bin/env python3
# import regular-expression modules' functions
import re

print()  # space for program text
# Regex Mini Guide:
# ^  -  Match from/at beginning of line
# $  -  Match at end of line
# .  -  Match any character (wildcard)
# \s -  Match white-spase characters (include spaces)
# \S -  Match non white-spase
# *  -  Repeat looking for character zero or more
#       times(so .* is like bash wildcard). + does same.
# *? -  Repeats A character zero or more(non-greedy form)
# [aeiou] - Match A single character in A the set
# [^XYZ]  - Match A single characternot listed in set
# [a-z0-9] - The set of characters can include A range
# ( - Indicates where string exctract should start
# ) - Indicates where string extraction should end
# [^A-Za-z] - invert sets' logic, match other than alphabet
# () - Get subset of matched string in findall()
# \b - Match empty string, only at start or end or word
# \B - Match empty string, not at start or end of word
# \d - Match any decimal digit 0-9, replaces set [0-9]
# \D - Match any non-digit, replaces [^0-9]

# print whole file for conparison later
file = open("text.txt")
print("this is the file content we're working with:\n")
for line in file:
    print(line, end='')

del line
file.close()
print()

# Start
print("\ngetting only 'sender names' from conversation:\n")
file = open("text.txt")
# get lines from file by generic for loop
for line in file:
    # if any line has "from:" text, print it
    if re.search('from:', line):
        print(line, end='')

# exit
del line
file.close()
print("\n\nDone. Exiting...")
exit(0)
