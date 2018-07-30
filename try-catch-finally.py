#!/usr/bin/env python3

# errors to except:
# ImportError: an import fails;
# IndexError: a list is indexed with an out-of-range number;
# NameError: an unknown variable is used;
# SyntaxError: the code can't be parsed properly;
# TypeError: a function is called on a value of an
# inappropriate type;
# ValueError: a function is called on a value of the correct
# type, but with an inappropriate value.
try:
  print(1)
except NameError:    # catch errors
  print('Name error')
finally:    # finally runs no matter if error occured or not
  print('Done')
