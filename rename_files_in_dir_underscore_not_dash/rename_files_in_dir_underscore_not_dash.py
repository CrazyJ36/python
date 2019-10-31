#!/usr/bin/env python3
import os

files = os.listdir('.')
print('the files:', type(files), files)

x = 0
while x < len(files):
    print(type(files[x]), files[x])
    os.rename(str(files[x]), str(files[x].replace('-', '_')))
