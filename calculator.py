#!/usr/bin/env python3

# define what the add funciton is
def add(x, y):
    return x + y

# define what the subtract funtion is
def sub(x, y):
    return x - y

# make sure 1st input is numbers only
try:
    num1 = int(input("number1:    "))  # num1 should only be number
except ValueError:  # if num1 is not int, state to user to try again with number
    print("number 1 must be 0-9")
    exit() # exit the program at that point

# make sure character is '+' or '-' only
sym = input("+, -:       ")
if sym != '+' and sym != '-': # if sym is not the + or - characters, stop
    print("use only '+' or '-' character as equator")
    exit()

# make sure 2nd input is number only
try:
    num2 = int(input("number2:    "))
except ValueError:
    print("number 2 must be 0-9")
    exit()

# get input and use functions to add or subtract based on input
if sym == "+":
    print("answer:    ",add(num1,num2))
elif sym == "-":
    print("answer:    ",sub(num1,num2))
else:
    print("Unknown Equation")

