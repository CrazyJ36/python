#!/usr/bin/env python3

try:
	assert False, "My failed assertion message."
except AssertionError as e:
	print(e.args)
