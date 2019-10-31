#!/usr/bin/env python3
import os

path = "/data/data/com.termux/files/home/development"

print("Current directory:")
print(os.getcwd())
print("Changing to development work directory", path)
os.chdir(path)
print("Showing current directory (within script):")
os.system('ls')
