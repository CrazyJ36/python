#!/usr/bin/env python3

print("start")
try:
  raise ValueError("wrong value")
  print("tried; exception raised; this won't print")
except ValueError:
  print("excepted ValueError")
finally:
  print("done")
