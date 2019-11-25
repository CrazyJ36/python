#!/usr/bin/env python3
import os

if os.name == 'nt':
    files = os.system('dir /b')  # dir /b switch, shows names only
elif os.name == 'posix':
    files = os.system('ls -a')
else:
    print('unknown os, exiting')
    exit(0)

print(files)
print('done')