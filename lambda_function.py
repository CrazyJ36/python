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

# lambda function to calculate x minus 2:
# lambda x: x - 2

# in python lambdas, your lambda and argument must be in their own perenthesis.
# The following states that function 'x' will take arg 'y' and subtract two, then return.
# or: 'for x, x - 2, with 8 as x'
# (lambda x: x - 2)(8)
print( (lambda x: x - 2)(8) )

# You can't call x from 'lambda x' portion. Though you can assign the expression as varibable.
# this expression can then be called like A function.
# This is equivilent of:
#
# def sub_two(x):
#   return x - 2
#
sub_two = lambda x: x - 2
print( sub_two(10) )

# multiple arg lambda. function printing two words. lambdas can use functions( like print() ) in the expression.
# simple: lambda function with two args, pring the args:
words = lambda first, last: print( first + last )

words('thomas', 'kennedy')

# create function in funtion using lambda.
def multi_func(x):
  # x from multi_func() will be used as y in lambda expression.
  return (lambda y: y + 5)(x)

print(multi_func(3))



