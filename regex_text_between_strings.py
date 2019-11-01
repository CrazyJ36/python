#!/usr/bin/env python3

import re

orig_text = "This is A sentence of text."

# Here, re is searching for A match of the regular expression,
# assigning the returned match data to string:
# start at 'is' ('is...),
# and any ch/aracters after 'is', onward( (.*)...,
# end at 'of' (...of').
# the returned re.search data is an object,
# so print data at group(1) position the
# returned object data, the actual text match
# (re.search().group1).
# print that.
# TODO: group(1) probably is first occurence. ???

# Basiclly:
# 'is(.*)of'
# means: from 'is' - any char - to 'of'
extracted = re.search('is(.*)of', orig_text).group(1)

print(extracted)
