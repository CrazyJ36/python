#!/usr/bin/env python3

# Include upper 'python' directory in systems
# search path for modules, then import A variable from
# another program.
import sys
sys.path.append('../')
import get_dir


import zipfile

file1_name = current_cmd_path + '\file1.txt'

file2_name = current_cmd_path + '\file2.txt'

print(file1_name)
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