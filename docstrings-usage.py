#!/usr/bin/env python3

def myDocPrintFunc():
  """
   -----
   A Docstring;
   Should document what
   the function or module does.
   This text, by default,
   doesn't show during program execution,
   and can be read by developers.
   Though you can use:\n
   print(mfunc.__doc__)
   Anytime in the code
   to print this as A help function.\n
   To show an interactive help
   (like manpage) use:
   help(mfunc) or
   print(help(mfunc))
   -----
  """

task = input("""Use:
i - for interactive help
h - for inline help
""")
if task == "i":
  help(myDocPrintFunc)
elif task == "h":
  print(myDocPrintFunc.__doc__)

myDocPrintFunc()

# As opposed to docstring,
# A source code comment (# comment)
# Should document how
# a statement works.
