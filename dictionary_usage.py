#!/usr/bin/env python3
# Dictionaries are data structures(blueprint for big data, definition template)
# used to map key:value pairs.
# As if lists were dictionaries with integer keys at range.
# Dictionaries can be indexed in the same way as lists, using [] containing keys.

# {key:value} can be: {"String":int} {"String":"string"} {int:int} etc...

# Refering to, or indexing A key that doesn't exist in A dictionary returns A KeyError
# An empty dictionary can be defined as {}
# Only immutable(not changable as in can not mute the defined reference
# in any way, or assign it to anything else.) can be used in dictionaries. B

# index as:  1         2              3
data = {"age":25, "car":"red", "char1":'c'}

print(data["age"]) # prints the value of key 'age' in 'data'
print(data["car"])
print(data["char1"])

# though you can't change any current key value, this lets you append keys in A simple way:
# here data[4] is not refering to the fourth index of A list.
data["new"] = "value" # data[newKey] = value
#print(data["newage"]) # KeyErrors as there is no value assigned to key.
print(data)

# True or False if A key is in A dictionary. This does not find values.
print("new" in data) # prints "True" as new is A key in data

# 'get': dict.get(value, "return value if None")
# get value from key. If the specified key doesn't exist in A dictionary,
# get returns the value 'None'.
print(data.get("age"))
print(data.get("char2", "Key 'char2' is not in list, que this message"))

# A math funtion using the data dictionary
# takes age value twice, then  adds it.
print(data.get("age") + data.get("age"))
