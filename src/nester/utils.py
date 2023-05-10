"""
This module provides all functions necessary for Nester's three main utilities:

- create
- validate
- clean
"""

import json
from pathlib import Path, PurePath
from shutil import rmtree

PROJECT_ROOT = Path(__file__).parent.absolute()


def detect_languages():
    """
    Look through the templates folder to find which languages we have templates for

    :return: List of languages that have template folders
    :rtype: list
    """
    base_path = Path.joinpath(PROJECT_ROOT, "templates")
    return [PurePath(folder).name for folder in base_path.glob("*/")]


LANGUAGES = detect_languages()


def get_project_dir(projectname, should_create):
    """
    Get the project root directory.
    If the name of the current working directory does not match the projectname,
    a new directory will be created with the given projectname inside which the project
    is created.

    :param projectname: the name of the project
    :type projectname: str
    :param should_create: if directory should be created or not
    :type should_create: bool
    :return: the path of the project root
    """
    if Path.cwd().name != projectname:
        if should_create:
            Path.mkdir(Path(projectname), 0o755, True)
        return Path.joinpath(Path.cwd(), projectname)
    return Path.cwd()


def load_json(language, projectname):
    """
    Load the template for the project.

    :param language: the programming language of the project
    :type language: str
    :param projectname: the name of the project
    :type projectname: str
    :return structure: Returns the structure of the given language as a dict
    :rtype: dict
    """
    template = f"{PROJECT_ROOT}/templates/{language}/{language}_layout.json"
    with open(template, "r", encoding="utf-8") as tempfile:
        project_name = tempfile.read()
        project_name = project_name.replace("$projectname", projectname)
        structure = {}
        try:
            structure = json.loads(project_name)
        except json.JSONDecodeError as exc:
            print(f"JSONDecodeError: {exc}")
        except ValueError as exc:
            print(f"ValueError: {exc}")

    return structure


def create_structure(structure, base_path, projectname):
    """
    Iterate through the items in the structure and create directories and files based on that structure

    :param structure: the directory structure from the template
    :type structure: dict
    :param base_path: The current directory
    :type base_path: Path
    :param projectname: the name of the project
    :type projectname: str
    :return: None
    """

    for key, val in structure.items():
        if isinstance(val, dict):
            base_path = Path.joinpath(base_path, key)
            Path.mkdir(base_path)
            create_structure(val, base_path, projectname)
            base_path = base_path.parent
        else:
            file = Path.joinpath(base_path, key)
            Path.touch(file)
            if isinstance(val, str):
                file.write_text(val)


def validate_structure(structure, projectname, base_path):
    """
    Iterates through the subdirectories of the current directory and validates if it is a subset of the schema for
    the given language.

    :param structure: The directory structure from the template
    :type structure: dict
    :param base_path: The current directory
    :type base_path: Path
    :param projectname: The name of the project
    :type projectname: str
    :return: True or False depending on if the structure corresponds to the schema or not
    :rtype: bool
    """

    missing_file = False

    for key, val in structure.items():
        if isinstance(val, dict):
            base_path = Path.joinpath(base_path, key)
            validate_structure(val, projectname, base_path)
            base_path = base_path.parent
        key_path = Path.joinpath(base_path, key)
        if not Path.is_file(key_path) and not Path.is_dir(key_path):
            print(f"'{key}' file or directory not found!")
            missing_file = True
            continue
    if missing_file:
        return False
    return True


def clean(projectname):
    """
    Cleanup the given project.

    :param projectname: The name of the project
    """
    project_dir = get_project_dir(projectname, False)
    print("Cleaning up your mess...")
    rmtree(project_dir)
    print("Everything cleaned up!")
