#!/usr/bin/env python3

# import sys.exit, the normal way to exit python program
from sys import exit as prog_end

print("program runnning..")

# exit codes:
# 0 signifies successful program execution complete.
# 1 signifies any or all errors occured.
# 2 in unix systems, 2 signifies there was A command-line error(wrong command-line arguments)

# using sys.exit named as prog_end, with 0 as exit code (program successful, execution done).
#prog_end(0)

# you can specify an error message with sys.exit("message"). this throws A 1 exit code.
prog_end("error, exiting with 1 exit code due to error requiring A message ")
