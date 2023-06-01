"""
This module implements Nester's CLI-behaviour.
"""

import os
import sys

import click

from . import __version__, nester_log, utils

_context_settings = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=_context_settings)
def cli():
    """
    Nester - Copyright (c) 2023 ByteOtter. (github.com/ByteOtter)\n
    Licensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more info.
    """
    pass


@click.command()
@click.argument(
    "language",
    type=click.Choice(utils.LANGUAGES),
    required=1,
    metavar="[LANGUAGE]",
)
@click.argument("projectname", type=click.STRING, required=1)
@click.option(
    "--git", "-g", is_flag=True, default=False, help="Set up git repository aswell."
)
@click.option("--no-log", is_flag=True, default=False, help="Do not log this project.")
def create(language, projectname, git, no_log):
    """
    Create new project structure within current directory.

    LANGUAGE can be either:
    py, c, cpp, cs, java, rb

    PROJECTNAME refers to the name of your project. Your package will be named that way.
    """

    print(
        "Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software."
    )

    print(f"Checking log file for possible duplicate.")
    if nester_log.check_log_for_duplicate(projectname):
        print(
            f"\033[31mUups! A project called '{projectname}' already exists!\033[0m\nPlease choose a different name and try again!"
        )
        sys.exit(1)

    print(f"Creating file structure for your {language} project '{projectname}'...")

    structure = utils.load_json(language, projectname)
    project_dir = utils.get_project_dir(projectname, True)
    utils.create_structure(structure, project_dir, projectname)

    if git:
        print("Also creating git repository...")
        os.system("git init")

    if not no_log:
        nester_log.create_log_file_if_none()
        nester_log.LOGGER.info(
            "",
            extra={
                "projectname": projectname,
                "programming_language": language,
                "location": str(project_dir),
            },
        )

    print("\033[32mDone! Happy Hacking!\033[0m")


@click.command(help="Validate current structure against Nester's JSON schemas.")
@click.argument("language", type=click.Choice(utils.LANGUAGES))
@click.argument("projectname", type=click.STRING, required=1)
def validate(language, projectname):
    """
    Validate given project against the schema for the given language.
    """
    print(
        "Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software.\n"
    )
    print(f"Validating file structure for your {language} project...")

    structure = utils.load_json(language, projectname)
    project_dir = utils.get_project_dir(projectname, False)

    if not utils.validate_structure(structure, projectname, project_dir):
        print(
            "\033[31mYour structure does not seem to line up to our schemas :(\033[0m"
        )
    else:
        print("\033[32mValidation complete!\033[0m Everything looks good. :)")


@click.command()
@click.argument("projectname", type=click.STRING, required=1)
@click.confirmation_option(
    prompt="Are you sure you want to delete this project?\nThis CANNOT be undone!"
)
def clean(projectname):
    """
    Delete ALL contents within the current directory.

    THIS ACTION CANNOT BE UNDONE
    """
    print(
        "Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software.\n"
    )
    utils.clean(projectname)


@click.command()
@click.option(
    "--clean", is_flag=True, default=False, help="Remove orphaned log entries"
)
def log(clean):
    """
    List all previously created projects.

    Note: Only projects that were created without the `--no-log` flag are shown here.
    """
    print(
        "Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software.\n"
    )
    if clean:
        nester_log.clean_orphaned_entries()
    nester_log.print_log_to_table()


@click.command()
def version():
    """
    Print Nester version
    """

    print(
        """Nester - Copyright (c) 2023 ByteOtter. (github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more info.\nNester-version:""",
        __version__,
    )


cli.add_command(create)
cli.add_command(validate)
cli.add_command(clean)
cli.add_command(log)
cli.add_command(version)
