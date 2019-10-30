#!/usr/bin/env python3
import os

files = os.listdir('files')
print('the files:', files)
do_rename = input("will rename all files in \'files\' \
directory. continue? y, n")

if do_rename == 'y':
    os.renames(files, str.replace('-', '_'))
else:
    print('cancelled')

del files
del do_rename
exit(0)


