#!/usr/bin/env py

a, b, c = 1, 2, 3
print('a = 1; type of A is:', type(a))  # a is int.

x = a, b, c  # puts these values into A tuple.
print('x = 1, 2, 3; type is: ', type(x))

# leaves A as from values in x tuple,
# (*y) assigns y to anything from 
# the x tuple that is not directly
# assigned here(assigns y to the
# rest of x). y is list.
a, *y = x
print('a, *y = x; assigns y as the rest of x tuple, \
    besides a which defined as itself; \
    type of y is:', type(y))

print('a, y values are:', y)
