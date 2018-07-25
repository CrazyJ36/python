#!/usr/bin/env python3.7
import re

string = 'u'

if not string == 'y':
  print("string is not y")

# same algorithm:

if not re.match(string, 'y'):
  print("string is not y")
