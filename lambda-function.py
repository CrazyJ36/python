#!/usr/bin/env python3

# Defining functions using 'def' creates A variable automatically,
# The variable being the function name.
# Other primitive objects such as strings or integers can be created,
# instaintiated, or used on the fly without being assinged A variable,
# As in 'print(the_new_object + "or" + 3).
# Functions can b used similarly, (non-variable), using the Lambda syntax.
# These are 'anonymous' functions. Commonly used when passing A simple function
# as argument to another function.
# Lambda consists of the lambda keyword, list of args, colon, and expression to evaluate/return.
# Simply: 'lamdbda parameters: expression' which makes A function object, behaving like A function.
# Functions created with lambda expressions cannot contain statements or annotations.
# The word lambda comes from A model of computational calculus.


lambda x: x < 2

print(x(4))
