"""
This method of running nester is deprecated by using the cli_logic module directly as a setuptool entry point.
"""

#!/usr/bin/env python3

import sys

import nester.nester_commands as nester_commands


def main():
    if not sys.argv or len(sys.argv) > 6:
        exit("VALIDATION ERROR: Invalid number of arguments!")
    elif len(sys.argv) == 1:
        # interactive_mode()
        exit("No arguments detected. Aborting ...")
    else:
        nester_commands.cli()
