"""
This module provides an abstraction of the functionality previously found in the cli module.

Implemented here are commonly used functions for Nester used in its frontend both cli as well as TUI.
"""

import sys
from pathlib import Path

from . import nester_log, utils


def create_project(language: str, project_name: str, git: bool, no_log: bool) -> None:
    """
    Create a new project.

    :param language: The language the project needs the structure of.
    :param project_name: The name of the project.
    :param git: Whether or not to create a git repository.
    :param no_log: Whether or not to disable logging for this project.
    """

    print(f"\nChecking log file for possible duplicate.")
    if nester_log.check_log_for_duplicate(project_name):
        print(
            f"\033[31mUups! A project called '{project_name}' already exists!\033[0m\nPlease choose a different name and try again!"
        )
        sys.exit(1)

    structure: dict = utils.load_json(language, project_name)
    project_dir: Path = utils.get_project_dir(project_name, True)

    utils.create_structure(structure, project_dir, project_name)

    print(f"Creating file structure for your {language} project '{project_name}'...")

    if git:
        utils.initialize_git_repository(project_dir)

    if not no_log:
        nester_log.create_log_file_if_none()
        nester_log.LOGGER.info(
            "",
            extra={
                "project_name": project_name,
                "programming_language": language,
                "location": str(project_dir),
            },
        )

    print("\033[32mDone! Happy Hacking!\033[0m")


def validate_project(language: str, project_name: str) -> None:
    """
    Validate the project against a given languages's structure.

    :param language: The language to validate against
    :param project_name: The name of the project to validate.
    """

    structure: dict = utils.load_json(language, project_name)
    project_dir: Path = utils.get_project_dir(project_name, False)

    print(f"Validating file structure for your {language} project...")

    if not utils.validate_structure(structure, project_name, project_dir):
        print(
            "\033[31mYour structure does not seem to line up to our schemas :(\033[0m"
        )
    else:
        print("\033[32mValidation complete!\033[0m Everything looks good. :)")


def print_log(clean_log: bool) -> None:
    """
    Print nester log to console.

    :param clean_log: Whether or not to sanitize the log and remove orphaned entries.
    """
    if clean_log:
        nester_log.clean_orphaned_entries()
    nester_log.print_log_to_table()


def clean_project(project_name: str) -> None:
    """
    Delete project when it is found in the log.

    :param project_name: Name of the project to be removed.
    """
    print("Checking log if project exists...")
    if not nester_log.check_log_for_duplicate(project_name):
        print(
            f"""\033[31mError: Project '{project_name}' not found! Either the project was created with logging disabled.
Or it does not exist."""
        )
    else:
        utils.clean(project_name)
