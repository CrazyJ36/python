#!/usr/bin/env python3

# This creates/appends personal notes,
# one at A time, run after run, to A
# notes.txt file at home directory(or at up two dirs).

op = open("../../notes.txt", 'a')
text = input("New note:\n")
op.write(text)
op.write("\n")
op.close()

