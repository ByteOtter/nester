#!/usr/bin/env python3

import os
import sys
import click

PATH = ""

LANGUAGES = {"py": "python", "c": "C", "cpp": "C++", "rb": "Ruby", "java": "Java"}


@click.command()
def cli():
    click.echo("hello world!")


@click.command()
@click.argument("language", type=click.Choice(LANGUAGES.keys))
@click.option("--git", default=0, help="Set up git repository aswell.")
def create(language):
    print(
        "Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software.\n"
    )
    print(f"Creating file structure for {language}...")


@click.command()
@click.argument("language", type=click.Choice(LANGUAGES.keys))
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


# TODO:add commands to cli group


def interactive_mode():
    print(
        "Starting Nester.\nCopyright (c) 2023 ByteOtter.(github.com/ByteOtter)\nLicensed under the terms of GPL-3.0. Check github.com/ByteOtter/nester/LICENSE for more information.\nNo warranty or liability are included with the use of this software.\n"
    )
    print("No arguments given. Launching interactive mode ...")

    userInput = ""

    while True:
        userInput = input(
            "Which operation shall be performed?(create, validate, clean)\n"
        )
        if userInput not in ALLOWED_OPERATIONS:
            print("ERROR: Please enter a valid operation!(create, validate, clean)\n")
            continue
        else:
            OPERATION = userInput
            print("Selected operation: " + OPERATION)
            break

    while True:
        userInput = input(
            "What language would you like to generate the structure for?\n(py, cpp, c, cs, rb)\n"
        )
        if userInput not in LANGUAGES:
            print("ERROR: Please enter a supported language!\n(py, cpp, c, cs, rb)\n")
            continue
        else:
            LANGUAGE = userInput
            print("Selected language: " + LANGUAGE)
            break


def main():
    if not sys.argv or len(sys.argv) > 4:
        exit("VALIDATION ERROR: Invalid number of arguments!")
    elif len(sys.argv) == 1:
        interactive_mode()
    else:
        cli()
