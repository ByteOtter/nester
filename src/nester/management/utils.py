"""This module provides frequently used code to the wider management module."""

import os
import platform
import subprocess

import nester.exceptions as exceptions

PACKAGE_MANAGERS: list[str] = ["zypper", "apt", "apt-get", "dnf", "packman"]


def check_pip_installed() -> bool:
    """Verify pip is installed on the current system."""

    try:
        subprocess.run("pip", check=True)
    except subprocess.CalledProcessError:
        return False

    return True


def get_package_manager() -> str | None:
    """Check what package manager is installed.

    Attempts to identify the system Nester is installed on.
    If it cannot identify the system it will raise an exception.

    :return package_manager: name of the system's package manager
    """
    package_manager: str | None = None
    system: str = platform.system()

    match system:
        case "Linux":
            package_manager = identify_linux_package_manager()
        case "Darwin":
            package_manager = "brew"
        case "Windows":
            package_manager = "winget"

    return package_manager


def identify_linux_package_manager() -> str | None:
    """
    Will attempt to identify the distribution's package manager by brute forcing all known package manager.

    Will raise a UnknownDistroExcpetion if the package manager cannot be identified.

    :return pkgmgr: The Package Manager from the list of known package managers
    """
    for pkgmgr in PACKAGE_MANAGERS:
        try:
            subprocess.run(pkgmgr)
        except subprocess.CalledProcessError:
            raise excpetions.UnknownDistroException(
                "Error: Distribution could not be identified."
            )
        return pkgmgr


def check_for_virtualenv(project_name: str) -> bool:
    """
    Check a project for a virtual environment.

    This function checks whether a given project has a virtualenv directory.

    :param project_name: The name of the project to check.
    :return: Whether the given project has a virtualenv.
    """
    pass


def select_dependency_source(language: str) -> None:
    """
    Select the source of the project's dependencies according to its language.

    Different programming languages have different ways of installing dependencies.\n
    Python uses ```pip```, Ruby uses ```gem``` etc. This function selects the appropriate way of installing dependencies
    using a given programming language.

    :param language: The language the project is written in.
    """
    pass
