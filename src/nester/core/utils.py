"""
This module provides all functions necessary for Nester's three main utilities:

- create
- validate
- clean
"""

import json
import os
from pathlib import Path, PurePath
from shutil import rmtree

from . import nester_log

PROJECT_ROOT: Path = Path(__file__).parent.absolute()

print(PROJECT_ROOT)


def detect_languages() -> list:
    """
    Look through the templates folder to find which languages we have templates for

    :return: List of languages that have template folders
    :rtype: list
    """
    base_path: Path = Path.joinpath(PROJECT_ROOT, "templates")
    return [PurePath(folder).name for folder in base_path.glob("*/")]


LANGUAGES: list = detect_languages()


def get_project_dir(project_name: str, should_create: bool) -> Path:
    """
    Get the project root directory.
    If the name of the current working directory does not match the project_name,
    a new directory will be created with the given project_name inside which the project
    is created.

    :param project_name: the name of the project
    :type project_name: str
    :param should_create: if directory should be created or not
    :type should_create: bool
    :return: the path of the project root
    """
    try:
        if Path.cwd().name != project_name:
            if should_create:
                Path.mkdir(Path(project_name), 0o755, True)
            return Path.joinpath(Path.cwd(), project_name)
        return Path.cwd()
    except FileNotFoundError:
        print("\033[31mProject directory not found!\033[0m")
        return Path()


def load_json(language: str, project_name: str) -> dict:
    """
    Load the template for the project.

    :param language: the programming language of the project
    :type language: str
    :param project_name: the name of the project
    :type project_name: str
    :return structure: Returns the structure of the given language as a dict
    :rtype: dict
    """
    template: str = f"{PROJECT_ROOT}/templates/{language}/{language}_layout.json"
    structure = {}

    if language not in LANGUAGES:
        print(f"\033[31mFatal Error: Language '{language}' not supported!\033[30m")
        return structure

    try:
        with open(template, "r", encoding="utf-8") as tempfile:
            file_handle = tempfile.read()
            file_handle = file_handle.replace("$projectname", project_name)
            try:
                structure = json.loads(file_handle)
            except json.JSONDecodeError as exc:
                print(f"JSONDecodeError: {exc}")
            except ValueError as exc:
                print(f"ValueError: {exc}")
    except FileNotFoundError as exc:
        print(f"\033[31mFatal Error:'{language}' structure file not found!\033[30m")

    return structure


def create_structure(structure: dict, base_path: Path, project_name: str) -> None:
    """
    Iterate through the items in the structure and create directories and files based on that structure

    :param structure: the directory structure from the template
    :type structure: dict
    :param base_path: The current directory
    :type base_path: Path
    :param project_name: the name of the project
    :type project_name: str
    :return: None
    """
    if structure is not None:
        for key, val in structure.items():
            if isinstance(val, dict):
                base_path = Path.joinpath(base_path, key)
                Path.mkdir(base_path)
                create_structure(val, base_path, project_name)
                base_path = base_path.parent
            else:
                file: Path = Path.joinpath(base_path, key)
                Path.touch(file)
                if isinstance(val, str):
                    file.write_text(val)
    else:
        raise AttributeError("\033[31mFatal Error:\033[30m invalid language structure!")


def validate_structure(structure: dict, project_name: str, base_path: Path) -> bool:
    """
    Iterates through the subdirectories of the current directory and validates if it is a subset of the schema for
    the given language.

    :param structure: The directory structure from the template
    :type structure: dict
    :param base_path: The current directory
    :type base_path: Path
    :param project_name: The name of the project
    :type project_name: str
    :return: True or False depending on if the structure corresponds to the schema or not
    :rtype: bool
    """

    missing_file: bool = False

    for key, val in structure.items():
        if isinstance(val, dict):
            base_path = Path.joinpath(base_path, key)
            validate_structure(val, project_name, base_path)
            base_path = base_path.parent
        key_path: Path = Path.joinpath(base_path, key)
        if not Path.is_file(key_path) and not Path.is_dir(key_path):
            print(f"'{key}' file or directory not found!")
            missing_file = True
            continue
    if missing_file:
        return False
    return True


def clean(project_name: str) -> None:
    """
    Cleanup the given project.

    :param project_name: The name of the project
    """
    project_dir: Path = get_project_dir(project_name, False)
    if not project_dir.exists():
        print(f"\033[31mError: Project '{project_name}' not found!")
    else:
        print("Cleaning up your mess...")
        rmtree(project_dir)
        nester_log.remove_log_entry(project_name)
        print("\033[32mEverything cleaned up!\033[0m")


def initialize_git_repository(project_dir: Path) -> None:
    """
    Initialize ```git``` repository in project dir.

    :param project_dir: Directory of the project to initialize git repository in.
    """
    print("Creating git repository...")
    # Save current working directory
    current_dir = os.getcwd()
    # Change to project directory
    os.chdir(project_dir)
    # Initialize git repository
    os.system("git init")
    # return to previous directory
    os.chdir(current_dir)
