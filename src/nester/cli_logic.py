import os
import shutil

import click

import nester.utils as utils


@click.group()
def cli():
    pass


@click.command()
@click.argument("language", type=click.Choice(utils.LANGUAGES.keys()), required=1)
@click.argument("projectname", type=click.STRING, required=1)
@click.option(
    "--git", "-g", is_flag=True, default=False, help="Set up git repository aswell."
)
def create(language, projectname, git):
    print(
        f"Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software.\n"
    )
    print(
        f"Creating file structure for your {utils.LANGUAGES[language]} project '{projectname}'..."
    )
    utils.parse_dir(utils.LANGUAGES[language], language, projectname)

    if git:
        print(f"Also creating git repository...")
        os.system("git init")


@click.command()
@click.argument("language", type=click.Choice(utils.LANGUAGES.keys()))
def validate(language):
    print(
        "Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software.\n"
    )
    print(f"Validating file structure for your {language} project...")


@click.command()
@click.option("--yes", "-y", is_flag=True, default=False)
def clean(y):
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
