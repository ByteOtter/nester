"""Custom Exceptions for Nester's project management utility."""


class UnknownDistroException(Exception):
    """Exception to handle in the event that a linux distribution cannot be identified or does not have a known package manager."""

    def __init__(self, message: str):
        super().__init__(message)
