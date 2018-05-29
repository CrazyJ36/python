#!/usr/bin/env python3

# if a variable has not been defined or no longer exists,
# you will get a NameError

a = 'text1'  # a variable(can change) piece of data, stored in ram. 
b = 'text2'

print(a)
del a  # delete variable from memory
print(b)

c = input("enter a number: ") # inputcan be stored in a variable
print(c)
del c, b #  error does occur if i try to use these again
