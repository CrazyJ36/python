#!/usr/bin/env python3

import os

print("""\nExample: Executing normal linux command line statements in python.
This script uses pythons' 'os.system' to \nlist the current directory(eg. 'ls -a').\n""")
os.system('ls -a')
