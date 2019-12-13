my_list1 = ['a', 'b', 'c', 'd']
my_list2 = ['e', 'f', 'g']

print('\nmy_list1 type is:')
print(type(my_list1))
print('my_list1:')
print(my_list1)

print('\n')
print('my_list2:')
print(my_list2)

my_list1.extend(my_list2)
print('\nAfter: my_list1.extend(my_list2):')
print(my_list1)
