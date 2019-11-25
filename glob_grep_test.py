#!/usr/bin/env python3
import glob

# glob.glob lists/greps files, all(*) in /usr.
print("All /bin executables that start with 'b':\n")
print(glob.glob('/bin/b*'))
