#!/usr/bin/env python3

# clear space for program text, prints 1 new line.
# print("\n") would be two lines(print function itself)
print()

# this shows how to use python3's string function
# str.rstrip()

# str.rstrip() only removes ending, or 'trailing'
# whitespace(spaces). if str.rstrip('ing') has A parameter,
# it removes only the given characters that occur at the
# end of the string.

# test using str.rstrip to remove space

str1 = "text1    "
str2 = "text2"

print("I have two strings. Printing both normally: ")
print(str1, str2)

print("Removing space from first word with str.rstrip():")
print(str1.rstrip(), str2, "\n")


# test using str.rstrip to remove end chars
str3 = "list1-"
str4 = "list2-"
print("Two strings:")
print(str3, str4)

print("removing dash from list items:")
print( str3.rstrip('-'), str4.rstrip('-') )

# exit
print("done, exiting...\n")
del str1, str2, str3, str4
exit(0)
