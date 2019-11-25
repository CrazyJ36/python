#!/usr/bin/env python3

from subprocess import call

print("Running unix 'ls -a' from python:")
call(["ls", "-a"])
