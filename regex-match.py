#!/usr/bin/env python3
import re

print("testing string match")
string = 'u'

if not string == 'y':
  print("string is not y")
else:
  print("we have a problem")

# same algorithm:
if not re.match(string, 'y'):
  print("string is not y")
else:
  print("we have a problem")

print("done\n")
