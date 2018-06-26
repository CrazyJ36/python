#!/usr/bin/env python3

# An if statement only runs if the
# condition evaluates to true.
# if statent never runs if false.

# A while statement repeatedly tests
# a condition for trueness until
# it returns false. Then code continues.

i = 0  # to-be iterations counter

while i < 5:
  print(i)
  i += 1  # i equals value of i plus 1

  # the 'break' keyword can be used anytime
  # in A loop to end immediately

  # also, 'continue will jump back to the top
  # this can be used with if to skip an iteration

  # don't use break or continue outside of a loop
print("done")
