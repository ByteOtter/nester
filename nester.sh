#!/bin/bash
# USAGE: nester <OPERATION> <LANGUAGE> <PATH>
# EXAMPLE: nester create python . -s | Create src-layout for python project in
#                                      current directory.

cd src/
python main.py $1 $2 $3 $4