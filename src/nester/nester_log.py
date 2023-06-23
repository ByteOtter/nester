"""
This module handles Nester's logging functionality. Nester logs all projects created with it unless the --no-log flag ist set when calling nester create.
"""

import logging
import re
from pathlib import Path
from typing import List


class ProjectLogFormatter(logging.Formatter):
    """
    Custom formatter class to handle the custom log fields Nester requires.
    """

    def format(self, record: logging.LogRecord) -> str:
        """
        Override logging.Formatter.format function
        """
        record = self.process(record)
        return super().format(record)

    def process(self, record: logging.LogRecord) -> logging.LogRecord:
        """
        Override logging.Formatter.process function
        """
        record.project_name = getattr(record, "project_name", "N/A")
        record.programming_language = getattr(record, "programming_language", "N/A")
        record.location = getattr(record, "location", "N/A")
        return record


_LOG_FILE_PATH: Path = Path.home() / ".nester.log"
LOGGER: logging.Logger = logging.getLogger("nester")
LOGGER.setLevel(logging.INFO)


def create_log_file_if_none() -> None:
    """
    Create ```.nester.log``` file if it does not exist already.

    :param: None
    :return: None
    """
    formatter: logging.Formatter = ProjectLogFormatter(
        "%(asctime)s - %(name)s - %(levelname)s - Project: %(project_name)s - Language: %(programming_language)s - Location: %(location)s"
    )
    file_handler: logging.FileHandler = logging.FileHandler(_LOG_FILE_PATH)
    file_handler.setFormatter(formatter)
    LOGGER.addHandler(file_handler)


def check_log_for_duplicate(project_name: str) -> bool:
    """
    Check for duplicate log entries.

    Check the nester.log file in the home directory, whether a given project_name has been taken already.
    If no log file exists: Continue with the program.

    :param project_name: Name of the project to be checked
    :return: True/False depending on whether an entry has been found.
    :rtype: bool
    """
    try:
        with _LOG_FILE_PATH.open("r", encoding="utf-8") as log_file:
            log = log_file.readlines()
    except FileNotFoundError:
        print(f"\033[34mLog file not found. Moving on ...\033[0m")
        return False

    for line in log:
        if project_name in line:
            return True

    return False


def remove_log_entry(project_name: str, verbose: bool = True) -> None:
    """
    Check if the given project appears in the log. If it does, remove the entry from the log.

    :param project_name: The name of the project to be removed.
    :type project_name: str
    :param verbose: Flag whether or not to suppress print statements. Needed for clean function.
    :type verbose: bool
    :return: None
    """
    try:
        with _LOG_FILE_PATH.open("r", encoding="utf-8") as log_file:
            log: List[str] = log_file.readlines()
    except FileNotFoundError:
        print("\033[34mNo log file found! Moving on ...\033[0m")
        return

    entry_found: bool = False
    updated_lines: List[str] = []

    if project_name[-1] == "/" and project_name[-2] != "\\":
        # If project_name is given as directory or escaped "/" (with ending "/"), trim last "/".
        # This may happen when using autocompletion in the terminal.
        project_name = project_name[:-1]

    for line in log:
        if project_name in line:
            entry_found = True
        else:
            updated_lines.append(line)

    if entry_found:
        try:
            with _LOG_FILE_PATH.open("w", encoding="utf-8") as log_file:
                log_file.writelines(updated_lines)
            if verbose:
                print(
                    f"\033[32mLog entry for '{project_name}' removed successfully.\033[0m"
                )
        except Exception as exception:
            print(f"\033[31mError while removing entry: {exception}\033[0m")
    else:
        print(f"\033[34mNo log entry found for '{project_name}'\033[0m")


def clean_orphaned_entries() -> None:
    """
    Check log entries for orphaned projects.

    Orphaned projects are projects created and logged by Nester, but the source tree has been removed.
    Check all projects listed in the log and see whether their paths are still valid.
    If not remove the entry.

    :param: None
    :return: None
    """
    items_removed: int = 0

    try:
        with open(_LOG_FILE_PATH, "r", encoding="utf-8") as log_file:
            for line in log_file:
                project_name: str = re.search(
                    r"[-\s]+Project:\s+(.*?)\s+-", line
                ).group(1)
                location: str = re.search(r"[-\s]+Location:\s+(.*)", line).group(1)

                if not Path.exists(Path(location)):
                    remove_log_entry(project_name, False)
                    print(f"Project '{project_name}' cleaned up.")
                    items_removed = items_removed + 1

            if items_removed == 0:
                print("\033[32mLog Check completed! No orphaned entries. :)\033[0m")
            else:
                print(
                    f"\033[32mLog Check completed! {items_removed} entries removed.\033[0m"
                )
    except FileNotFoundError:
        print(
            "\033[31mError: No log file found. Run 'nester create' to get started!\033[0m"
        )


def find_all_projects() -> List[str]:
    """
    Read the log file and save all project names into a list.
    """
    projects: List[str] = []
    try:
        # Check if log fille exists
        if not _LOG_FILE_PATH.exists():
            print(
                "\033[031mError: Log file could not be found.\033[0m\nThis could happen because you have not created a single project yet. Try `nester create` to get started!"
            )
        # Check if log file is empty
        elif _LOG_FILE_PATH.stat().st_size == 0:
            print(
                "\033[33mNo projects logged. Try \033[35mnester create\033[33m to start!\033[0m"
            )
        else:
            with open(_LOG_FILE_PATH, "r", encoding="utf-8") as log_file:
                for line in log_file:
                    project_name = re.search(r"[-\s]+Project:\s+(.*?)\s+-", line).group(
                        1
                    )
                    projects.append(project_name)

    except Exception as exception:
        print(f"\033[31mAn unexpected error occurred: {exception}\033[30m")

    return projects


def print_log_to_table() -> None:
    """
    Read the log file and print its contents into a table.

    :param: None
    :return: None
    """
    try:
        # Check if logfile exists
        if not _LOG_FILE_PATH.exists():
            print(
                "\033[031mError: Log file could not be found.\033[0m\nThis could happen because you have not created a single project yet. Try `nester create` to get started!"
            )

        # Check if logfile is empty
        if _LOG_FILE_PATH.stat().st_size == 0:
            print(
                "\033[33mNo projects logged. Try \033[35mnester create\033[33m to start!\033[0m"
            )
        else:
            with open(_LOG_FILE_PATH, "r", encoding="utf-8") as log_file:
                # Print table header
                print(f"{'Project Name':<20} | {'Language':<10} | {'Location'}")
                print("-" * 80)

                for line in log_file:
                    project_name: str = re.search(
                        r"[-\s]+Project:\s+(.*?)\s+-", line
                    ).group(1)
                    language: str = re.search(
                        r"[-\s]+Language:\s+(.*?)\s+-", line
                    ).group(1)
                    location: str = re.search(r"[-\s]+Location:\s+(.*)", line).group(1)

                    print(f"{project_name:<20} | {language:<10} | {location}")
                print()
    except Exception as exception:
        print(f"\033[31mAn unexpected error occurred: {exception}\033[30m")
