#!/usr/bin/env python3
for i in range(1,6):
  file = open("note" + str(i) + ".txt", 'w')
  file.write("content " + str(i) + "\n")
  file.close()
