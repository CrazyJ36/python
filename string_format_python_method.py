#!/usr/bin/env python3

# format items/variables to string with:
#
# "text {to}".format(from)
#
# {to} can be blank curley braces, formatted() in order

# one way:
print("\"string\".format(index[0],index[1])")
# list of words
words = ("sky", "blue")
# format to var
string = "the {0} is {1}!".format(words[0],words[1])
print(string)

# {to} can be blank, though fromat(from) must be in ltr order
xstr = 'test1'
ystr = 'test2'
print("strings are: {} {}".format(xstr, ystr))

# mixed {to} indexes defined in format("from")
print("{0}{1}{0}".format("abra","cad"))

# set {to} define new vars in format
print("{x}{y}".format(y='i',x='h'))
# print(x) # x is not still existenty, was used in above format()
