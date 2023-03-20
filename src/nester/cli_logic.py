import click

import os
import sys
import click

PATH = ""

LANGUAGES = {"py": "Python", "c": "C", "cpp": "C++", "rb": "Ruby", "java": "Java"}


@click.group()
def cli():
    pass


@click.command()
@click.argument("language", type=click.Choice(LANGUAGES.keys()), required=1)
@click.argument("projectname", type=click.STRING, required=1)
@click.option(
    "--git", "-g", is_flag=True, default=False, help="Set up git repository aswell."
)
def create(language, projectname, git):
    print(
        f"Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software.\n"
    )
    print(
        f"Creating file structure for your {LANGUAGES[language]} project '{projectname}'..."
    )

    if git:
        print(f"Also creating git repository...")


@click.command()
@click.argument("language", type=click.Choice(LANGUAGES.keys()))
def validate(language):
    print(
        "Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software.\n"
    )
    print(f"Validating file structure for your {language} project...")


@click.command()
def clean():
    print(
        "Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software.\n"
    )
    print(f"Cleaning up your mess...")
    # os.remove()


cli.add_command(create)
cli.add_command(validate)
cli.add_command(clean)
