"""This module provides custom exceptions for the opinionated creation of projects."""


class UnsupportedLanguageException(Exception):
    def __str__(self) -> str:
        return "\033[91mError: The chosen language is not supported for opinionated creation!\033[0m"
