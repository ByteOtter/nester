"""
This module provides support functionality for the opinionated creation module.
"""

import subprocess

from . import supported_tools


def identify_package_manager() -> str:
    """
    Identify which distribution's package manager is installed via trial and error.

    :return: The name of the package manager to be used to install dependencies.
    :rtype: str
    """
    for pm in supported_tools.package_managers:
        try:
            subprocess.run(pm)
        except subprocess.CalledProcessError:
            continue
        return pm
    return ""
