"""
This module contains integration tests to asess if all of Nester's function work well together.

This is done by temporarily creating a project, calling all of Nester's features and cleaning up the created project in the end.
"""

from unittest.mock import patch
from pathlib import Path
import src.nester.utils as utils

# Test data
_PROJECT_ROOT = Path(__file__).parent.absolute()
_TEST_LANGUAGE = "py"
_TEST_PROJECTNAME = "TEST_MOCK_PROJECT"
_VALID_STRUCTURE = {"src": {"test_project": {"__init__.py": "test"}}}
_INVALID_STRUCTURE = {
    "invalid_directory": {"test_invalid_project": {"invalid.py": "invalid"}}
}


def test_get_project_dir():
    # Test case: Create a new project directory and check if it is cwd
    with patch.object(Path, "cwd") as mock_cwd:
        mock_cwd.name = _TEST_PROJECTNAME
        assert utils.get_project_dir(_TEST_PROJECTNAME, True) == Path.joinpath(
            Path.cwd(), _TEST_PROJECTNAME
        )


def test_create_structure():
    structure = utils.load_json(_TEST_LANGUAGE, _TEST_PROJECTNAME)
    project_dir = utils.get_project_dir(_TEST_PROJECTNAME, False)
    utils.create_structure(structure, project_dir, _TEST_PROJECTNAME)

    assert utils.validate_structure(structure, _TEST_PROJECTNAME, project_dir)


def test_validate_structure(tmp_path):
    # Create a valid and an invalid directory tree
    utils.create_structure(_VALID_STRUCTURE, tmp_path, "test_project")
    utils.create_structure(_INVALID_STRUCTURE, tmp_path, "test_invalid_project")
    # assert if the given directory tree passes or fails the test when comparing to the correct schema
    assert utils.validate_structure(_VALID_STRUCTURE, "test_project", tmp_path)
    assert not utils.validate_structure(
        _VALID_STRUCTURE, "test_invalid_project", tmp_path / "test_invalid_project"
    )


def test_cleanup():
    project_dir = utils.get_project_dir(_TEST_PROJECTNAME, False)
    utils.clean(_TEST_PROJECTNAME)

    assert not Path.exists(project_dir)
