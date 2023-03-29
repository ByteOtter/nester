#!/bin/bash
# USAGE: nester <OPERATION> <LANGUAGE> <PATH>
# EXAMPLE: nester create -g py | Create src-layout for py project in
#                                current directory and initialize a git repo.

python $( dirname -- "$0"; )/src/nester.py $1 $2 $3 $4