#!/usr/bin/env python

import argparse
from sys import argv

# Initialize argument parser function with A program with
# default only -h arg and program description.
parser = argparse.ArgumentParser(
    description='This simply test argparse. \
    Try running with the argument -h.')

# len argv < 2 catches whether running as 'python prog' or
# './prog'  on windows(git-bash)
if len(argv) < 2:
    print('run with -h or --help to show simplicity of argparse.')
else:
    parser.parse_args()

# By default argparse has generated A help option and we've
# added A program description to this should the user type
#  -h or --help as command line argument.
