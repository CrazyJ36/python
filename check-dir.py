import os

if os.scandir("C:\\Users"):
    print("windows users exists")
else:
    print("windows users nonexistent")

try:
    os.scandir("C:\\Fake")
except FileNotFoundError:
    print("no fake directories on your system")
