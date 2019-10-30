#!/usr/bin/env python3

print("""
A tuple is A array of immutable Python objects.
The difference between 'tuples' and 'lists'
(list syntax: my_list = ['a','b']), is that tuples
can not be changed unlike list. Tuples use perenthesis,
where lists use square brackets.
Tuple is A comma seperated array of any items types.\n
Even if A tuple has only one value you must include A comma.
Can be empty(initialization)
Tuples start at indice(index position) 0, and can be sliced.
You can not add objects to tuples or update items with new values.
(You could, however, slice one tuples items out and put them into
another tuple.
""")

print("Initialize Empty tuple, no values, syntax:  tuple1 = ()")
tuple1 = ()
print("actual tuple1:", tuple1, "\n")

print("New tuple two, with ints syntax/example: tuple2 = (1, 2, 3)")
tuple2 = (1,2,3)
print("actual tuple2:", tuple2, "\n")

print("Get second item from tuple2, syntax: tuple2[1]")
print("Here:", tuple2[1], "\n")

print("""New tuple3, with different types of values, example: tuple3 = ('hi', 4, 2, 3, 1, 5.6)""")
tuple3 = ('hi', 4, 2, 3, 1,5.6)
print("actual tuple3:", tuple3, '\n')

print("Slicing tuple3 example: print(tuple3[2:5])")
print("Meaning get and print items from index 2 till before 5")
print("Here:", tuple3[2:5], '\n')

print("Concat two tuples into one example: (1,2,3) + (4,5,6)")
print( "Here:", (1,2,3) + (4,5,6) )

print(
"""
You can also use the following function/operation methods on tuples:
len( ('this', 'is', 'tuple') ) - count object of tuple list
(1,2,3) + (4,5,6) - concatenation of tuples to one
('hi',) * 4 - makes tuple with four 'hi's as items
3 in (1,2,3) - Returns true, tests for A  '3' integers' existence in items
for x in (1,2,3): print x, - iterate the tuple
TODO add all of these to examples.
"""
)

print(
"""Just like any variable Object, you can delete
A tuple, syntax:
del tuple1, tuple2, tuple3
I'll do this now to free some RAM memory before we exit,
Bye!"""
)

del tuple1, tuple2, tuple3
exit(0)
