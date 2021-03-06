#!/usr/bin/env python3

# Python's order of operations is the same as that of normal
# mathematics: parentheses first, then exponentiation, then
# multiplication/division, and then addition/subtraction.

# List of operators from highest
# precenece to lowest:
#
# **    -Exponentiation (raise to the power)
# ~+-   -Complement, unary plus minus (method names +@ -@)
# * / % //   -Multiply, division, modulo, floor division
# +-    -Addition, subtraction
# >> <<  -right and left bitwise shift
# &      -Bitwise 'AND'
# ^|    -Bitwise exclusive `OR' and regulat `OR'
# <= < > >=   -Comparison operators
# <> == !=   -Equality operators
# = %= /= //= -= +- *= **=   -Assignment operators
# is, is not   -identity operators
# in, not in   -Membership operators
# not, and, or   -Logical operators
# Research these more

x = 1 + (2 * 2)
print(x)

if False == (False or True): # == has higer precenence than or
			     # so or does'nt even apply.
  print("Same")
else:
  print("false")
