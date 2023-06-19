"""
This module implements Nester's CLI-behavior.
"""

import os
import sys
from pathlib import Path

import click

from . import __version__, nester_log, utils

_context_settings: dict = dict(help_option_names=["-h", "--help"])


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
@click.argument("project_name", type=click.STRING, required=1)
@click.option(
    "--git", "-g", is_flag=True, default=False, help="Set up git repository as well."
)
@click.option("--no-log", is_flag=True, default=False, help="Do not log this project.")
def create(language: str, project_name: str, git: bool, no_log: bool) -> None:
    """
    Create new project structure within current directory.

    LANGUAGE can be either:
    py, c, cpp, cs, java, rb

    PROJECT_NAME refers to the name of your project. Your package will be named that way.
    """

    click.echo(
        "Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software."
    )

    click.echo(f"Checking log file for possible duplicate.")
    if nester_log.check_log_for_duplicate(project_name):
        print(
            f"\033[31mUups! A project called '{project_name}' already exists!\033[0m\nPlease choose a different name and try again!"
        )
        sys.exit(1)

    click.echo(
        f"Creating file structure for your {language} project '{project_name}'..."
    )

    structure: dict = utils.load_json(language, project_name)
    project_dir: Path = utils.get_project_dir(project_name, True)
    utils.create_structure(structure, project_dir, project_name)

    if git:
        click.echo("Also creating git repository...")
        os.system("git init")

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

    click.echo("\033[32mDone! Happy Hacking!\033[0m")


@click.command(help="Validate current structure against Nester's JSON schemas.")
@click.argument("language", type=click.Choice(utils.LANGUAGES))
@click.argument("project_name", type=click.STRING, required=1)
def validate(language: str, project_name: str) -> None:
    """
    Validate given project against the schema for the given language.
    """
    print(
        "Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software.\n"
    )
    print(f"Validating file structure for your {language} project...")

    structure: dict = utils.load_json(language, project_name)
    project_dir: Path = utils.get_project_dir(project_name, False)

    if not utils.validate_structure(structure, project_name, project_dir):
        print(
            "\033[31mYour structure does not seem to line up to our schemas :(\033[0m"
        )
    else:
        print("\033[32mValidation complete!\033[0m Everything looks good. :)")


@click.command()
@click.argument("project_name", type=click.STRING, required=1)
@click.confirmation_option(
    prompt="Are you sure you want to delete this project?\nThis CANNOT be undone!"
)
def clean(project_name: str) -> None:
    """
    Delete ALL contents within the current directory.

    THIS ACTION CANNOT BE UNDONE
    """
    click.echo(
        "Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software.\n"
    )
    utils.clean(project_name)


@click.command()
@click.option(
    "--clean", is_flag=True, default=False, help="Remove orphaned log entries"
)
def log(clean: bool) -> None:
    """
    List all previously created projects.

    Note: Only projects that were created without the `--no-log` flag are shown here.
    """
    click.echo(
        "Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software.\n"
    )
    if clean:
        nester_log.clean_orphaned_entries()
    nester_log.print_log_to_table()


@click.command()
def version() -> None:
    """
    Print Nester version
    """

    click.echo(
        """Nester - Copyright (c) 2023 ByteOtter. (github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more info.\nNester-version:""",
        __version__,  # type: ignore
    )


cli.add_command(create)
cli.add_command(validate)
cli.add_command(clean)
cli.add_command(log)
cli.add_command(version)
