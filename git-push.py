import os
import sys
# Windows only

# Check that git is installed
if os.path.isfile("C:\Program Files\Git\git-cmd.exe") == False:
  print("Git not installed. Install to continue, or simply change\npath in code to point to proper exe.")
  sys.exit(0)

# Check proper message arguments, define commit message.
try:
  msg = "git commit -m " + "\"" + sys.argv[1] + "\""
except IndexError:
  print("Run as: git-push.py \"commit message\"\nFor Windows only.")
  sys.exit(0)

# prewrite git commands
def gitwork():
  os.system("git add .")
  os.system(msg)
  os.system("git push")

# review changes
path = os.getcwd()
print("Push changes in: " + path)
print("with message: " + sys.argv[1])

check = input("[y,n]: ")

# Ask user to continue.
if check == "y":
  gitwork()
elif check == "n":
  print("Cancelled.")
  sys.exit(0)
else:
  print("Unknown response, aborted.")

# Exit
print("Done.")
sys.exit(0)