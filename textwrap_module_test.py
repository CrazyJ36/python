#!/usr/bin/env python3
from textwrap import wrap

text_string = 'This is A long paragraph of text in A character string.\
 The content was be wrapped in A pretty form, meaning I use the module:\
 textwrap.wrap to take A string of any length and split it into A list\
 of new strings which have A specific character length, specified with\
 the textwrap.wrap(width=int) option.\
 textwrap.wrap returns A list of specified lines,\
 I printed each line in A loop through the list of strings.'

text_wrapped_lines = wrap(text_string, width=30)

for i in text_wrapped_lines:
  print(i)

exit(0)
