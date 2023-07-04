"""This module provides logic to allow Nester to manage dependencies."""


def add_dependency(language: str, dependency: str) -> None:
    """
    Add dependency to current project.

    Adds a dependency to a project and adds it to the list of dependencies for the project's language.\n
    E.g the pyproject.toml etc.

    :param language: The language of the project.
    :param dependency: The name of the dependency to add.
    """
    pass


def remove_dependency(dependency: str) -> None:
    """
    Remove a given dependency.

    Remove a given dependency from a project.

    :param dependency: The dependency to remove.
    """
    pass
