#!/usr/bin/env python3

import re

def add(x, y):
    return x + y
def sub(x, y):
    return x - y

try:
    num1 = int(input("number1:    "))
except ValueError:
	print("numbers must use 0-9's")
	exit()
	
sym = input("+, -:       ")

try:
    num2 = int(input("number2:    "))
except ValueError:
	print("numbers must use 0-9's")
	exit()

if sym != '+' and sym != '-':
    print("use only '+' or '-' character as equator")
    exit()
elif sym == "+":
    print("answer:    ",add(num1,num2))
elif sym == "-":
    print("answer:    ",sub(num1,num2))
else:
    print("Unknown Equation")

