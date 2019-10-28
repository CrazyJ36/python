#!/usr/bin/env python3
from os import environ, name
from sys import platform
if name == 'linux':
    from os import uname


# Get specific item from os.environ dictionary.
print('\nos.environ.get(\'OS\':)', environ.get('OS'))
# Another way to get the dictionary entry:
print('os.environ[\'OS\']:', environ['OS'])

print('os.name:', name)
print('sys.platform:', platform)

# Only works in unix
if name == 'linux':
    print('os.uname() in linux:', uname())
