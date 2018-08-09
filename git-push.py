import os
import sys

# Check that git is installed
if os.path.isfile("C:\Program Files\Git\git-cmd.exe"):
  print("Git is installed...")
else:
  print("Git not installed. Install to continue.")
  sys.exit(0)

# Check proper message arguments
try:
  msg = "git commit -m " + "\"" + sys.argv[1] + "\""
  print(msg)
except IndexError:
  print("Run as: git-push-win.py \"commit message\"")
  sys.exit(0)

# initialize git commit command. inserting msg to {0} with .format
#cmd = "git commit -m {0}".format(msg)
#print(cmd)

# prewrite git commands
def gitwork():
  os.system("git add .")
  os.system(msg)
  os.system("git push")

# review changes
path = os.getcwd()
print("Push changes in:")
print(path)
print("with message:")
print(msg)
check = input("[y,n]: ")

if check == "y":
  gitwork()
elif check == "n":
  print("Cancelled.")
  sys.exit(0)
else:
  print("Unknown response, aborted.")

print("Done.")
sys.exit(0)