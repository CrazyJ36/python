import os

try:
    os.scandir("C:\\Users\\Thomas")
    print("Thomas User(Toshiba Laptop User)")
except FileNotFoundError:
    print("no toshiba thomas")

try:
    os.scandir("C:\\Users\\CrazyJ36")
    print("CrazyJ36 User(Win Azure PC)")
except FileNotFoundError:
    print("no azurewin CrazyJ36")

try:
    os.scandir("/home/thomas/")
    print("Linux user thomas")
except FileNotFoundError:
    print("no linux thomas")
