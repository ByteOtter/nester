"""This module provides custom exceptions for the opinionated creation of projects."""


class UnsupportedLanguageException(Exception):
    """
    This exception is raised, whenever the user tries to use opinionated creation for a language that does not
    support this feature.
    """

    def __str__(self) -> str:
        return "\033[91mError: The chosen language is not supported for opinionated creation!\033[0m"
