"""
This module handles Nester's logging functionality. Nester logs all projects created with it unless the --no-log flag ist set when calling nester create.
"""

import logging
import re
from pathlib import Path


class ProjectLogFormatter(logging.Formatter):
    """
    Custom formatter class to handle the custom log fields Nester requires.
    """

    def format(self, record):
        """
        Override logging.Formatter.format function
        """
        record = self.process(record)
        return super().format(record)

    def process(self, record):
        """
        Override logging.Formatter.process function
        """
        record.projectname = getattr(record, "projectname", "N/A")
        record.programming_language = getattr(record, "programming_language", "N/A")
        record.location = getattr(record, "location", "N/A")
        return record


_LOG_FILE_PATH = Path.home() / ".nester.log"
LOGGER = logging.getLogger("nester")
LOGGER.setLevel(logging.INFO)


def create_log_file_if_none():
    """
    Create '.nester.log' file if it does not exist already.

    :param: None
    :return: None
    """
    formatter = ProjectLogFormatter(
        "%(asctime)s - %(name)s - %(levelname)s - Project: %(projectname)s - Language: %(programming_language)s - Location: %(location)s"
    )
    file_handler = logging.FileHandler(_LOG_FILE_PATH)
    file_handler.setFormatter(formatter)
    LOGGER.addHandler(file_handler)


def check_log_for_duplicate(projectname):
    """
    Check the nester.log file in the home directory, whether a given projectname has been taken already.
    If no log file exists: Continue with the program.

    :param projectname: Name of the project to be checked
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
        if projectname in line:
            return True

    return False


def remove_log_entry(projectname, verbose=True):
    """
    Check if the given project appears in the log. If it does, remove the entry from the log.

    :param projectname: The name of the project to be removed.
    :type projectname: str
    :param verbose: Flag whether or not to suppress print statements. Needed for clean function.
    :type verbose: bool
    :return: None
    """
    try:
        with _LOG_FILE_PATH.open("r", encoding="utf-8") as log_file:
            log = log_file.readlines()
    except FileNotFoundError:
        print("\033[34mNo log file found! Moving on ...\033[0m")
        return

    entry_found = False
    updated_lines = []

    if projectname[-1] == "/" and projectname[-2] != "\\":
        # If projectname is given as directory or escaped "/" (with ending "/"), trim last "/".
        # This may happen when using autocompletin in the terminal.
        projectname = projectname[:-1]

    for line in log:
        if projectname in line:
            entry_found = True
        else:
            updated_lines.append(line)

    if entry_found:
        try:
            with _LOG_FILE_PATH.open("w", encoding="utf-8") as log_file:
                log_file.writelines(updated_lines)
            if verbose:
                print(
                    f"\033[32mLog entry for '{projectname}' removed successfully.\033[0m"
                )
        except Exception as exception:
            print(f"\033[31mError while removing entry: {exception}\033[0m")
    else:
        print(f"\033[34mNo log entry found for '{projectname}'\033[0m")


def clean_orphaned_entries():
    """
    Check all projects listed in the log and see whether their paths are still valid.
    If not remove the entry.

    :param: None
    :return: None
    """
    items_removed = 0

    try:
        with open(_LOG_FILE_PATH, "r", encoding="utf-8") as log_file:
            for line in log_file:
                project_name = re.search(r"[-\s]+Project:\s+(.*?)\s+-", line).group(1)
                location = re.search(r"[-\s]+Location:\s+(.*)", line).group(1)

                if not Path.exists(Path(location)):
                    remove_log_entry(project_name, False)
                    print(f"Project '{project_name}' cleand up.")
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


def print_log_to_table():
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
        elif _LOG_FILE_PATH.stat().st_size == 0:
            print(
                "\033[33mNo projects logged. Try \033[35mnester create\033[33m to start!\033[0m"
            )

        else:
            with open(_LOG_FILE_PATH, "r", encoding="utf-8") as log_file:
                # Print table header
                print(f"{'Project Name':<20} | {'Language':<10} | {'Location'}")
                print("-" * 80)

                for line in log_file:
                    project_name = re.search(r"[-\s]+Project:\s+(.*?)\s+-", line).group(
                        1
                    )
                    language = re.search(r"[-\s]+Language:\s+(.*?)\s+-", line).group(1)
                    location = re.search(r"[-\s]+Location:\s+(.*)", line).group(1)

                    print(f"{project_name:<20} | {language:<10} | {location}")
                print()
    except Exception as exception:
        print(f"\033[31mAn unexpected error occurred: {exception}\033[30m")
