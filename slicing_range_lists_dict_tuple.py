#!/usr/bin/env python3

# reuse a list, 'sliced' as: [start:end]

mlist = ["bill", "james", "becky", "chris", "thomas", "megan"]

print("my list, defined like ['','','']:")
print(mlist)

print("[0:2] slicing from index 0 to 2, not including 2:")
print(mlist[0:2])

# if start: or :end part is left out, start or end
# of list,tuple is taken.

print("[:2] from start to before second index of mlist:")
print(mlist[:2])
print("[2:] from 2nd to last index:")
print(mlist[2:])

print("[::] all:")
# like above, [::] means slice from start to end
print(mlist[::]) # will print all

# steps between indexes can be indicated
print("[::2] start to end. every steps/intervals of 2:")
print(mlist[::2])

# can use negative index positions to count backwards
print("[-1] backwards 1 index:", mlist[-1])
