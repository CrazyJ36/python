#!/usr/bin/env python3

# purposeful false assertio.
try:
	assert False, "My failed assertion message."
except AssertionError as e:
	print(e.args)
