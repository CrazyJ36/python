#!/usr/bin/env python3

# Include upper 'python' directory in systems
# search path for modules, then import my variables
# or functions from another program.
import sys
sys.path.append('../crazyj36_libs/get_dir')
import get_dir


import zipfile

print('initiating 2 test files.')
'''
file1 = open(current_cmd_path + 'file1.txt', 'x')
file2 = open(current_cmd_path + 'file2.txt', 'x')

print('writing 2 test files to disk')
file1.write()
file2.write()

zipfile.ZipFile((file1, file2), 'x', 0, True)

print('done with 2 test files')
file1.close()
file2.close()
'''