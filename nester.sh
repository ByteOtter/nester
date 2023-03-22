#!/bin/bash
# USAGE: nester <OPERATION> <LANGUAGE> <PATH>
# EXAMPLE: nester create py . -s | Create src-layout for py project in
#                                      current directory.

cd src/
python nester.py $1 $2 $3 $4