import json
from pathlib import Path, PurePath

PROJECT_ROOT = Path(__file__).parent.absolute()


def detect_languages():
    """
    Look through the templates folder to find which languages we have templates for

    :return: List of languages that have template folders
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
    :return: the path of the project root
    """
    if Path.cwd().name != projectname and should_create:
        Path.mkdir(Path(projectname), 0o755, True)
        return Path.joinpath(Path.cwd(), projectname)
    else:
        return Path.cwd()


# TODO: Rename and make modular
def parse_dir(language, projectname):
    """
    Load the template for the project and call iterate_structure to create the directories and files

    :param language: the programming language of the project
    :param projectname: the name of the project
    :return: None
    """
    template = f"{PROJECT_ROOT}/templates/{language}/{language}_layout.json"
    with open(template, "r") as tempfile:
        project_name = tempfile.read()
        project_name = project_name.replace("$projectname", projectname)
        structure = json.loads(project_name)

    return structure


def iterate_structure(structure, base_path, projectname):
    """
    Iterate through the items in the structure and create directories and files based on that structure

    :param structure: the directory structure from the template
    :param base_path: The current directory
    :param projectname: the name of the project
    :return: None
    """

    for key, val in structure.items():
        if isinstance(val, dict):
            base_path = Path.joinpath(base_path, key)
            Path.mkdir(base_path)
            iterate_structure(val, base_path, projectname)
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
    :param base_path: The current directory
    :param projectname: The name of the project
    :return: Boolean
    """

    for key, val in structure.items():
        if isinstance(val, dict):
            base_path = Path.joinpath(base_path, key)
            validate_structure(val, projectname, base_path)
            base_path = base_path.parent
        if not Path.is_file(Path(key)) or Path.is_dir(Path(key)):
            return True
    return False
