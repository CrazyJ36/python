#!/usr/bin/env python3

# decorators allow to reuse A function in A new way to extend it's function.

# or @decor to call this below
def decor(func):
  def wrap():
    print("-----")
    func()
    print("-----")

  return wrap

def print_text1():
  print("Hello")

def print_text2():
  print("World")

decor1 = decor(print_text1)
decor2 = decor(print_text2)

decor1()
decor2()
print()  # skip line

# The same, simpler
def title(text):
  print("-----")
  print(text)
  print("-----")

title("Hello")
title("World")
