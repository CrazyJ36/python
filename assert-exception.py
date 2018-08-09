#!/usr/bin/env python3

# Asstertion: assert A statement, maing sure it's true.
# test functionality. An expression is tested,
# and if the result is false, AssertionError is raised.
# 'assert' is often used to check for valid input at the
# start of functions, or at the end of functions to check
# valid output. If AssertionError(statement is false),
# program terminates immediatly, stopping execution.

print("asserting A true expression")
assert 1 + 2 == 3, "log message if false" # True, no assert problem
print("Done, code successful.")

print("Trying to assert A false expression")
assert 1 == 2, "Optional false Assert message"
# Wrap false assert in try/except to handle exception.
