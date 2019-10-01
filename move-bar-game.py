#!/usr/bin/env python3

def lineL():
    print("-"*5)  # 'dash' 5 times to make A line

def lineR():
    print("\t\t","-"*5)  # two tabs makes 'space', then 'dash' lines

def lineC():
    print("\t","-"*5)

inp = input("choose your side (left, right, center): ")

if inp=='right':
    lineR()
elif inp=='left':
    lineL()
elif inp=='center':
    lineC()
else:
    print("you didn't enter: left, right, or center")
