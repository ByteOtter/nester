import json
from pathlib import Path, PurePath

PATH = Path.cwd()
PROJECT_ROOT = Path(__file__).parent.absolute()

def detect_languages():
    base_path = Path.joinpath(PROJECT_ROOT, "templates")
    return [PurePath(folder).name for folder in base_path.glob('*/')]


LANGUAGES = detect_languages()


def parse_dir(language, projectname):
    template = f"{PROJECT_ROOT}/templates/{language}/{language}_layout.json"
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
