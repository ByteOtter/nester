#!/usr/bin/env python3

import sys

import nester.cli_logic as cli_logic


def main():
    if not sys.argv or len(sys.argv) > 6:
        exit("VALIDATION ERROR: Invalid number of arguments!")
    elif len(sys.argv) == 1:
        # interactive_mode()
        exit("No arguments detected. Aborting ...")
    else:
        cli_logic.cli()
