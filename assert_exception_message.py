#!/usr/bin/env python3

# This shows how to show A custom
# error message when you 'assert' A
# statement to return true, but turns out false.

print("""Trying A 'statement'. If error occurs
in the statememt, A known-error message will
be shown instead of an AssertionError.\n""")
try:
    assert False, "Can not assert False statement."
    print("Asserted True.")
except AssertionError as assertError1Var:
    print(assertError1Var.args)

print("\nDone. Exiting...")
