import json
from pathlib import Path

PATH = Path.cwd()
PROJECT_ROOT = Path(__file__).parent.absolute()
LANGUAGES = {"py": "python", "c": "c", "cpp": "c++", "rb": "ruby", "java": "java"}


def parse_dir(language, short_lang, projectname):
    template = f"{PROJECT_ROOT}/templates/{language}/{short_lang}_layout.json"
    with open(template, "r") as tempfile:
        structure = json.loads(tempfile.read())

    iterate_structure(structure, PATH)

    return "Success!"


def iterate_structure(structure, base_path):
    for key, val in structure.items():
        if isinstance(val, dict):
            base_path = Path.joinpath(base_path, key)
            iterate_structure(val, base_path)
            continue
        else:
            base_path = Path.joinpath(base_path, key)
            Path.touch(base_path)
