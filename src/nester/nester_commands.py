"""
This module implements Nester's CLI-behaviour.
"""

import os
import click
from . import utils, __version__

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
def create(language, projectname, git):
    """
    Create new project structure within current directory.

    LANGUAGE can be either:
    py, c, cpp, cs, java, rb

    PROJECTNAME refers to the name of your project. Your package will be named that way.
    """

    print(
        "Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software."
    )

    print(f"Creating file structure for your {language} project '{projectname}'...")

    structure = utils.load_json(language, projectname)
    project_dir = utils.get_project_dir(projectname, True)
    utils.create_structure(structure, project_dir, projectname)

    if git:
        print("Also creating git repository...")
        os.system("git init")

    print("Done! Happy Hacking!")


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
        print("Your structure does not seem to line up to our schemas :(")
    else:
        print("Validation complete! Everything looks good. :)")


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
cli.add_command(version)
