#!/usr/bin/python

# Format string using variables like in C.
# %s - String
# %d - Integers
# %f - floating point(real) numbers

# %.<num of digits>f - floating point number with
#formatted number of digits to right of dot

# requires % before variable, no comma(,)
# between format and variable

text = "hello" #variables
num = 2

print("text: %s num: %d" %(text, num)) # print multiple variables
print("text: %s" %text) # print single variable

nList = [1,3,5]
print("array: %s" %nList) # print array

print("%s %d %s" %(text,num,nList))
