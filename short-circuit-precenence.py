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
if 3 < 2 and (True == True):
  print("True in:\nif 3<2 and (True == True)")
else:
  print("False in:\nif 3<2 and (True == True)")
