#!/usr/bin/env python3

# Assertion: assert(assume true) A statement,
# testing it's functionality.
# An expression is tested, and if the result
# is false, AssertionError is raised by Interpreter.
# 'assert' is often used to check for valid input at the
# start of functions, or at the end of functions to check
# valid output. If AssertionError(statement is false),
# program terminates immediatly, stopping execution.

# A True statement, no assertion problem
print("Asserting A true expression.")
assert 1 + 2 == 3, "This is the log message if false."
print("Done, code successful.\n")

print("Trying to assert A false expression.")
assert 1 == 2, "My reason for error: 1 is not 2."
# Wrap false assert in try/except to handle exception.
