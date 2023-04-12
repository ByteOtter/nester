"""
This method of running nester is deprecated by using the cli_logic module directly as a setuptool entry point.
"""

#!/usr/bin/env python3

import sys

from nester import nester_commands


def main():
    """
    Main method.
    """
    if not sys.argv or len(sys.argv) > 6:
        sys.exit("VALIDATION ERROR: Invalid number of arguments!")
    elif len(sys.argv) == 1:
        # interactive_mode()
        sys.exit("No arguments detected. Aborting ...")
    else:
        nester_commands.cli()
