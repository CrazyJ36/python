#!/usr/bin/env python3
from sys import argv

print("Args length: " + str(len(argv)) + '\n')

help_str = """
Usage: python my-help.py module function

This program can quickly show python documentation for modules of functions.
If you type something weird, you get the shown the most relevant information.

Show this help message with [-h]
"""

if len(argv) == 1 or (argv[1] == '-h'):  # No args, check for --help
    print(help_str)
    exit(0)
elif len(argv) == 2:  # module
    help(str(argv[1]))
    exit(0)
elif len(argv) == 3:  # module function
    help(str(argv[1]) + '.' + str(argv[2]))
    exit(0)
