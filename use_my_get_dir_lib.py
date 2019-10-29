#!/usr/bin/env python3

# In case your lib file is in A different directory
# then your new file that is using your library,
# temporarily append directories to the systems
# search path for modules, then import my variables
# or functions from another program.
# import sys
# sys.path.append('crazyj36_libs')

# Or use blank file called __ init __.py in the
# directory which holds your modules, this
# tells python it can import from here.
# This is the method used here.
# Then you can import modules from the folder
# which contains __init__.py
from crazyj36_libs import get_dir

print(get_dir.get_os_dir_append_name('no-file.txt'))

# Calling:
# function_name.__doc__
# returns the docstring or
# programmer defined instructions,
# from function declerations.
print(get_dir.get_os_dir_append_name.__doc__)