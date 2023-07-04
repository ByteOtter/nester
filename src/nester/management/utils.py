"""This module provides frequently used code to the wider management module."""

import subprocess


def verify_pip_installed() -> bool:
    """Verify pip is installed on the current system."""

    try:
        subprocess.run("pip", check=True)
    except subprocess.CalledProcessError:
        return False

    return True


def get_package_manager() -> str:
    """Check what package manager is installed"""
    pass
