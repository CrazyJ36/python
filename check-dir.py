# there is probably a built-in way to check username

import os

if os.scandir("C:\\Users\\Thomas"):
    print("Thomas User(Tohsiba Laptop User)")
elif os.scandir("C:\\Users\\CrazyJ36"):
    print("CrazyJ36 User(Win Azure PC)")
elif os.scandir("/home/thomas/"):
    print("Linux user")
