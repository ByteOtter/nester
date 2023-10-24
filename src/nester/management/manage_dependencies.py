"""This module provides logic to allow Nester to manage dependencies."""

import subprocess

from . import utils


def add_dependency(language: str, dependency: str) -> None:
    """
    Add dependency to current project.

    Adds a dependency to a project and adds it to the list of dependencies for the project's language.\n
    E.g the pyproject.toml etc.

    :param language: The language of the project.
    :param dependency: The name of the dependency to add.
    """
    match language:
        case "py":
            if utils.check_pip_installed():
                subprocess.run("pip").args("install").args(dependency)
                # TODO Add dependency logging!
            else:
                print("Error: Dependency cannot be added. Pip is not installed!")


def remove_dependency(dependency: str) -> None:
    """
    Remove a given dependency.

    Remove a given dependency from a project.

    :param dependency: The dependency to remove.
    """
    pass
