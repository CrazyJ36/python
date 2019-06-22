#!/usr/bin/env python3
# gets important parts of string to list by regex

import re
string = "names are name-1 and name-2"
print("string is:\n", string)
important_points = re.findall('\S+-\S+', string)
print("Important points of string:\n", important_points)
