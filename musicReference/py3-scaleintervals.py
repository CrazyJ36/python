while True:
    option = input("Type scale name.\nmajor,minor,etc. or q(quit):\n\n")
    if option == 'major':
        print("2,2,1,2,2,2,1\n")
    elif option == 'minor':
        print("2,1,2,2,1,2,2\n")
    elif option == 'harmonic minor':
        print("2,1,2,2,1,3,1\n")
    elif option == 'q':
        exit()
    else:
        print("invalid term\n")
