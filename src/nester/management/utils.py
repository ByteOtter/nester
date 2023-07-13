"""This module provides frequently used code to the wider management module."""

import subprocess


def check_pip_installed() -> bool:
    """Verify pip is installed on the current system."""

    try:
        subprocess.run("pip", check=True)
    except subprocess.CalledProcessError:
        return False

    return True


def get_package_manager() -> str:
    """Check what package manager is installed."""
    pass


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
