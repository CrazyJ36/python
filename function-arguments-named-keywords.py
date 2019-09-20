#!/usr/bin/env python3

print("For function arguments, there can be normal required arguments and optional key:value arguments")

def func(*required_args, **key_args):
  print("Args were: %s %s" %(required_args, key_args))

func('required1', assigned1="key1", assigned2="key2")
