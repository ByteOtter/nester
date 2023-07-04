"""
This module contains integration tests to asses if all of Nester's function work well together.

This is done by temporarily creating a project, calling all of Nester's features and cleaning up the created project in the end.
"""

from pathlib import Path
from unittest.mock import patch

import nester.core.utils as utils


def test_get_project_dir(fake_project_name):
    # Test case: Create a new project directory and check if it is cwd
    with patch.object(Path, "cwd") as mock_cwd:
        mock_cwd.name = fake_project_name
        assert utils.get_project_dir(fake_project_name, True) == Path.joinpath(
            Path.cwd(), fake_project_name
        )


def test_create_structure(fake_language, fake_project_name):
    structure = utils.load_json(fake_language, fake_project_name)
    project_dir = utils.get_project_dir(fake_project_name, False)
    utils.create_structure(structure, project_dir, fake_project_name)

    assert utils.validate_structure(structure, fake_project_name, project_dir)


def test_validate_structure(tmp_path, valid_structure, invalid_structure):
    # Create a valid and an invalid directory tree
    utils.create_structure(valid_structure, tmp_path, "test_project")
    utils.create_structure(invalid_structure, tmp_path, "test_invalid_project")
    # assert if the given directory tree passes or fails the test when comparing to the correct schema
    assert utils.validate_structure(valid_structure, "test_project", tmp_path)
    assert not utils.validate_structure(
        valid_structure, "test_invalid_project", tmp_path / "test_invalid_project"
    )


def test_cleanup(fake_project_name):
    project_dir = utils.get_project_dir(fake_project_name, False)
    utils.clean(fake_project_name)

    assert not Path.exists(project_dir)
