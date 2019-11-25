#!/usr/bin/env python3

print("A true test:\n")
assert 1 == 1, "My failed msg if 1 is not 1"

print("A false test:")
try:
	assert 1 == 2, "My reason of expression failure."
except AssertionError as ae:
	ae.args += ('more', 'reasons') # this can only concatenate tuple, not str
	print(ae.args) # Or 'raise' here. Print looks cleaner and still gives reason detail.

