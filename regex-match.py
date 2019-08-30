#!/usr/bin/env python3
import re

print("testing string match")
string = 'u'

if not string == 'y':
    print("string is not y")
else:
    print("we have a problem")

# re.match(pattern, text) only checks at the
# beginning of A string,
# while re.search(pattern, text) looks in entire string.
# same algorithm:
if not re.match(string, 'y'):
    print("string is not y")
else:
    print("we have a problem")

print("done\n")
