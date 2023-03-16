#!/usr/bin/env python3

import os
import sys
import click

OPERATION = ""
LANGUAGE = ""
PATH = ""

SUPPORTED_LANGUAGES = ["python", "c", "cpp", "cs", "rb"]


@click.command()
def cli():
    click.echo("hello world!")


@click.command()
@click.option("-g", default=0, help="Set up git repository aswell.")
@click.option("--git", default=0, help="Set up git repository aswell.")
@click.argument("language")
def create(language):
    pass


@click.command()
def validate():
    pass


@click.command()
def clean():
    pass


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
        if userInput not in SUPPORTED_LANGUAGES:
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
        for argument in sys.argv[2:]:
            if argument not in ALLOWED_OPERATIONS or SUPPORTED_LANGUAGES:
                exit(
                    "Invalid argument!\nUSAGE: nester <OPERATION> <LANGUAGE>\nSupported Languages: py, cpp, c, cs, rb"
                )
