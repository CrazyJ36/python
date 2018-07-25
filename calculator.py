<<<<<<< HEAD
#!/usr/bin/env python3
=======
#!/usr/bin/env python3.6
import re
>>>>>>> 6d52c1eb1254f71e0b979d8b6fafe138e645afd2

def add(x, y):
    return x + y
def sub(x, y):
    return x - y

num1 = int(input("number1:    "))
sym = input("+, -:       ")
num2 = int(input("number2:    "))

<<<<<<< HEAD
if sym == "+":
=======
if sym != '+' and sym != '-':
    print("use only '+' or '-' character as equator")
    exit()
elif sym == "+":
>>>>>>> 6d52c1eb1254f71e0b979d8b6fafe138e645afd2
    print("answer:    ",add(num1,num2))
elif sym == "-":
    print("answer:    ",sub(num1,num2))
else:
    print("Unknown Equation")

