def lineL():
 print("-"*5)

def lineR():
 print("\t\t","-"*5)

def lineC():
 print("\t","-"*5)

inp = input("choose your side (left, right, center): ")

if inp=='right':
 lineR()
elif inp=='left':
 lineL()
elif inp=='center':
 lineC()
else:
 print("you didn't enter: left, right, or center")
