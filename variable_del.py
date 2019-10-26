#!/usr/bin/env python3

# if a variable has not been defined or no longer exists,
# a NameError is raised.

a = 'variable a'  # a variable(can change) piece of data, stored in ram.
print(a)
del a  # delete variable from memory
try:
  print("Trying to print(a)")
  print(a)
except NameError:
  print("Failed(on purpose): The varable 'a' has previously been deleted using pythons 'del' module.")
exit()
