#!/usr/bin/env python3

# ways to concatenate strings; produces the same results.
# comma between print arguments infers A space.

print("hello", "world") # normal way
print("hello " + "world") # concatenate way

w, h = 'world', "hello"
print(h, w)
print(h + " " + w)
print(h + " ", w)