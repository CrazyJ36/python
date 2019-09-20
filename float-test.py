#!/usr/bin/python3

num1 = 3.5643 # float by default
print(num1) # prints the same
print("%.2f"%num1) #  print formatted. before decimal remains
                   #  default digits. after decimal show only two digits.

num2 = 5
print(num2/2) # divide num2(5) by 2. python converts result to float.

print(num2/num1) # print num2(5) divided by num1(3.5643)
print(num1+num2)
print('\nnum1 x num2 is: %.2f\nrounded to 2 decimal places.' %( num1*num2))

