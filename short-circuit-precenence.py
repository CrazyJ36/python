#!/usr/bin/env python3

# This is an example of how A ending an expression early
# works like the shortening of A circuit.

# Example wiring connections
connected = True
shorted = False
disconnected = False

# Simple short circuit blueprint
if ( connected ):
  print("Connection succeded")
elif ( disconnected ):
  print("Disconnected")
else:
  print("Shorted")

# second operator in if/and would cancel out and return false
# if the firsr operator is false. This even overrides precedence
# if the second operator were in perenthesis.
# Obviously, even though true is true, the first comparator is false
if 3 < 2 and (True == True):
  print("True in:\nif 3<2 and (True == True)")
else:
  print("False in:\nif 3<2 and (True == True)")

# TODO: this would be best explained when calculating voltages
# and current in A program.
# Operations in perenthesis
# should first come first(current), and, if voltage is the same,
# after drawing current, continue.
