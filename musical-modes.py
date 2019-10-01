#!/usr/bin/env python3

from collections import deque

I = "1. Ionian"
D = "2. Dorian"
P = "3. Phrygian"
Ly = "4. Lydian"
M = "5. Mixolydian"
A= "6. Aeolian"
Lo = "7. Locrian"
E = "8. Exit"
H = "Only [1-6] as input will do stuff"

print("Musical Modes")
def print_menu():
    print(20 * "-")
    print(I)
    print(D)
    print(P)
    print(Ly)
    print(M)
    print(A)
    print(Lo)
    print(E)
    print("9. Show Menu")
    print(20 * "-" + "\n")
    print("Type an option [1-6]")

print_menu()
loop = True
choice = None

while loop:

    seq=deque('CDEFGAB')

    try:
      choice = int(input())
    except ValueError:
        print(H)
    except KeyboardInterrupt:
      print("\rExit")
      exit()
    if type(choice) is not int:
        print(H)
    elif choice==0:
        print(H)

    elif choice==1:
        print(list(seq), I)
    elif choice==2:
        seq.rotate(-1)
        print(list(seq), D)
    elif choice==3:
        seq.rotate(-2)
        print(list(seq), P)
    elif choice==4:
        seq.rotate(-3)
        print(list(seq), Ly)
    elif choice==5:
        seq.rotate(-4)
        print(list(seq), M)
    elif choice==6:
        seq.rotate(-5)
        print(list(seq), A)
    elif choice==7:
        seq.rotate(-6)
        print(list(seq), Lo)
    elif choice==8:
        print(E)
        loop=False
    elif choice==9:
        print_menu()
