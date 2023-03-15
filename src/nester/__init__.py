#!/usr/bin/env python3

import os
import sys

ALLOWED_OPERATIONS = ["create", "inspect", "clean"]
SUPPORTED_LANGUAGES = ["py", "cpp", "c", "cs", "rb"]

def interactive_mode():
  print(f'''
      Starting Nester.\n
      No arguments given. Launching interactive mode ...
      ''')

  input("What language would you like to generate the structure?\n(py, cpp, c, cs, rb)")

def main():
    if not sys.argv or len(sys.argv) > 3:
      exit("invalid number of arguments!")
    elif len(sys.argv) == 1:
       interactive_mode()
    else:
       for argument in sys.argv:
          if argument not in ALLOWED_OPERATIONS or SUPPORTED_LANGUAGES:
             exit("Invalid argument!\nUSAGE: nester <OPERATION> <LANGUAGE>\nSupported Languages: py, cpp, c, cs, rb")
