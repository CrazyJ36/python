from collections import deque

def print_menu():
    print 67 * "-"
    print "1. Major"
    print "2. Major 1st Inversion"
    print "3. Menu Option 3"
    print "4. Menu Option 4"
    print "5. Exit"
    print "6. Show Menu Again"
    print 67 * "-" + "\n"

print_menu()
majorseq=deque('02212221')
majornotes=deque('CDEFGAB')
loop = True
while loop:
    choice = int(input("Enter menu choice[1-6]\n\n"))
    if type(choice) is not int:
        print "only digits will do stuff"
        print_menu()
    if choice==1:
        print "Major"
        print list(majornotes)
        print list(majorseq)
    elif choice==2:
        print "Major 1st Inversion\n\n"
        majornotes.rotate(-1)
        majorseq.rotate(-1)
        print list(majornotes)
        print list(majorseq)
    elif choice==3:
        print "Menu 3 has been selected"
    elif choice==4:
        print "Menu 4 has been selected"
    elif choice==5:
        print "Quitting"
        loop=False
    elif choice==6:
         print_menu()
