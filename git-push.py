import os
import sys

# Check that git is installed
if os.path.isfile("C:\Program Files\Git\git-cmd.exe") == False:
  print("Git not installed. Install to continue.")
  sys.exit(0)

# Check proper message arguments, define commit message.
try:
  msg = "git commit -m " + "\"" + sys.argv[1] + "\""
except IndexError:
  print("Run as: git-push-win.py \"commit message\"")
  sys.exit(0)

# prewrite git commands
def gitwork():
  os.system("git add .")
  os.system(msg)
  os.system("git push")

# review changes
path = os.getcwd()
print("Push changes in: " + path)
#print(path)
print("with message: " + sys.argv[1])
#print(msg)
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