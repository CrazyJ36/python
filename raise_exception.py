#!/usr/bin/env python3
print('Intentional fake error:')
raise ValueError("Optional message: There was A value error.")
# Or simply use 'raise ValueError'

# you can re-raise after exception if needed.
try:
  print(invalidVar)
except:
  print("there was an error")
  raise # will show the exact error that occured.
        # Doesn't change output
