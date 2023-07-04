"""
This module contains the logic for Nester terminal GUI.

If Nester is called without any arguments it enters ```interactive mode```.
The user is prompted to enter all the parameters needed before a project is created, validated or a log is shown.
"""

import sys
from typing import List

import questionary

from .core import commands, nester_log, utils


def interactive_mode() -> None:
    """
    Nester's interactive mode.

    Calling Nester without providing any subcommands will lead it to activate ```interactive mode```.
    This TUI will guide the user through Nester's functionality.
    """
    try:
        operation: questionary.Choice = questionary.select(
            "What operation do you want to perform?",
            choices=["create", "validate", "clean", "log", "---EXIT---"],
        ).unsafe_ask()

        match operation:
            case "create":
                language: str = questionary.select(
                    "What language would you like to create a project for?",
                    choices=utils.LANGUAGES,
                ).unsafe_ask()

                project_name: str = questionary.text(
                    "Name for your project:", multiline=False
                ).unsafe_ask()

                while not project_name:
                    print("This value is required!")
                    project_name = questionary.text(
                        "Name for your project:", multiline=False
                    ).unsafe_ask()

                create_git: bool = questionary.confirm(
                    "Do you also want to create a git repository?", default=True
                ).unsafe_ask()
                create_log: bool = questionary.confirm(
                    "Create a log entry for this project?", default=True
                ).unsafe_ask()

                commands.create_project(
                    language, project_name, create_git, not create_log
                )

            case "validate":
                project_name: str = questionary.text(
                    "Name the project to validate:"
                ).unsafe_ask()

                while not project_name:
                    print("This value is required!")
                    project_name = questionary.text(
                        "Name for your project:", multiline=False
                    ).unsafe_ask()

                language: str = questionary.select(
                    "What language do you want to validate against?",
                    choices=utils.LANGUAGES,
                ).unsafe_ask()

                commands.validate_project(language, project_name)

            case "clean":
                choices: List[str] = ["---Abort---"]
                projects = nester_log.find_all_projects()

                if projects is not None:
                    for project in projects:
                        choices.append(project)
                else:
                    print(
                        "\033[34mNo projects have been logged yet, so none can be removed.\033[0m"
                    )
                    sys.exit(0)

                project_name: str = questionary.select(
                    "What project do you want to remove?",
                    choices=choices,
                ).unsafe_ask()

                if project_name == "---Abort---":
                    print("Aborting...")
                    sys.exit(0)
                confirm: bool = questionary.confirm(
                    f"Project '{project_name}' will be permanently deleted. Are you sure?",
                    default=False,
                ).unsafe_ask()

                if confirm and project_name != "Abort":
                    utils.clean(project_name)
                else:
                    print("Aborting...")

            case "log":
                print("Loading project log...")
                clean: bool = questionary.confirm(
                    "Do you wish to sanitize the log?", default=True
                ).unsafe_ask()

                commands.print_log(clean)

            case "---EXIT---":
                print("Goodbye!")
                sys.exit(0)

            case _:
                print("No valid input or keyboard interrupt detected! Aborting...")
                sys.exit(0)

    except KeyboardInterrupt:
        print("Keyboard Interrupt registered! Aborting...")
        sys.exit(0)
