"""
This module implements Nester's CLI-behavior.
"""

import click

from . import __version__, tui
from .core import commands, utils

_context_settings: dict = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=_context_settings, invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """
    Nester - Copyright (c) 2023 ByteOtter. (github.com/ByteOtter)\n
    Licensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more info.
    """
    if ctx.invoked_subcommand is None:
        click.echo(
            """Nester - Copyright (c) 2023 ByteOtter. (github.com/ByteOtter)\nLicensed under the terms of GPL-3.0.
Check github.com/ByteOtter/nester/LICENSE for more info.
        """
        )
        click.echo("No commands registered. Starting interactive mode...")
        tui.interactive_mode()


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

    commands.create_project(language, project_name, git, no_log)


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

    commands.validate_project(language, project_name)


@click.command()
@click.argument("project_name", type=click.STRING, required=1)
@click.confirmation_option(
    prompt="Are you sure you want to delete this project?\nThis CANNOT be undone!"
)
def clean(project_name: str) -> None:
    """
    Delete the given project, if it is found in the log.

    THIS ACTION CANNOT BE UNDONE
    """
    click.echo(
        "Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software.\n"
    )
    commands.clean_project(project_name)


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
    commands.print_log(clean)


@click.command()
def version() -> None:
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
