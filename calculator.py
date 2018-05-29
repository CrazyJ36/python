#!/usr/bin/env python3.6

def add(x, y):
    return x + y
def sub(x, y):
    return x - y

num1 = int(input("number1:    "))
sym = input("+, -:       ")
num2 = int(input("number2:    "))
if sym == "+":
    print("answer:    ",add(num1,num2))
elif sym == "-":
    print("answer:    ",sub(num1,num2))
else:
    print("Unknown Equation")
