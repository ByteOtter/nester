import os
import shutil

import click

import nester.utils as utils

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
        f"Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software.\n"
    )

    print(f"Creating file structure for your {language} project '{projectname}'...")

    utils.parse_dir(language, projectname)

    if git:
        print(f"Also creating git repository...")
        os.system("git init")


@click.command(help=f"Validate current structure against Nester's JSON schemas.")
@click.argument("language", type=click.Choice(utils.LANGUAGES))
def validate(language):
    print(
        "Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software.\n"
    )
    print(f"Validating file structure for your {language} project...")


@click.command()
@click.option("--yes", "-y", is_flag=True, default=False, help="auto-confirm")
def clean(y):
    """
    Delete ALL contents within the current directory.

    THIS ACTION CANNOT BE UNDONE
    """
    print(
        "Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software.\n"
    )
    if y:
        print(f"Cleaning up your mess...")
        shutil.rmtree(utils.PROJECT_ROOT)
    else:
        print(f"No confirmation flag (--yes/-y) given. Aborting...")


cli.add_command(create)
cli.add_command(validate)
cli.add_command(clean)
