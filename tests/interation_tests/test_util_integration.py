"""
This module contains integration tests to asess if all of Nester's function work well together.

This is done by temporarily creating a project, calling all of Nester's features and cleaning up the created project in the end.
"""

import shutil
from unittest.mock import patch
from pathlib import Path
import src.nester.utils as utils

# Test data
PROJECT_ROOT = Path(__file__).parent.absolute()
TEST_LANGUAGE = "py"
TEST_PROJECTNAME = "TEST_MOCK_PROJECT"


def test_get_project_dir():
    # Test case: Create a new project directory and check if it is cwd
    with patch.object(Path, "cwd") as mock_cwd:
        mock_cwd.name = TEST_PROJECTNAME
        assert utils.get_project_dir(TEST_PROJECTNAME, True) == Path.joinpath(
            Path.cwd(), TEST_PROJECTNAME
        )


def test_create_structure():
    structure = utils.load_json(TEST_LANGUAGE, TEST_PROJECTNAME)
    project_dir = utils.get_project_dir(TEST_PROJECTNAME, False)
    utils.create_structure(structure, project_dir, TEST_PROJECTNAME)

    assert utils.validate_structure(structure, TEST_PROJECTNAME, project_dir)


def test_validate_structure():
    structure = utils.load_json(TEST_LANGUAGE, TEST_PROJECTNAME)
    project_dir = utils.get_project_dir(TEST_PROJECTNAME, False)

    assert utils.validate_structure(structure, TEST_PROJECTNAME, project_dir)


def test_cleanup():
    project_dir = utils.get_project_dir(TEST_PROJECTNAME, False)
    shutil.rmtree(project_dir)

    assert 1
