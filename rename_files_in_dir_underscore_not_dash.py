#!/usr/bin/env python3
import os

files = os.listdir('.')
print('current files:\n', files)

choice = input("Rename all these files and directories \
with '-' to use '_' instead(This won't touch files in subdirectories)? (y, n): ")

if choice == 'y':
    x = 0
    while x < len(files):
        try:
            os.rename(str(files[x]), str(files[x].replace('-', '_')))
        except PermissionError:
            pass
        x = x + 1
else:
    print('cancelled.')
    exit(0)
