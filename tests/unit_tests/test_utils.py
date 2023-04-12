"""
This module contains unit tests for the utils.py functions
"""

from unittest.mock import patch
from unittest import mock
from pathlib import Path


import src.nester.utils as utils

# Test data
_TEST_PROJECTNAME = "test_project"
_VALID_STRUCTURE = {"src": {"test_project": {"__init__.py": "test"}}}
_INVALID_STRUCTURE = {
    "invalid_directory": {"test_invalid_project": {"invalid.py": "invalid"}}
}


def test_detect_languages():
    languages = utils.detect_languages()

    assert "py" in languages
    assert "cpp" in languages
    assert "c" in languages
    assert "cs" in languages
    assert "java" in languages
    assert "rb" in languages


def test_load_json():
    # Arrange
    fake_json = '{"src": {"test_project": {"__init__.py": "test"}}}'

    # Act
    with patch("builtins.open", mock.mock_open(read_data=fake_json)):
        result = utils.load_json("py", "test")

    # Assert
    assert result == _VALID_STRUCTURE


def test_create_structure(tmp_path):
    # Arrange
    source_path = Path.joinpath(tmp_path, "src")
    project_path = Path.joinpath(source_path, _TEST_PROJECTNAME)
    file = Path.joinpath(project_path, "__init__.py")

    # Act
    utils.create_structure(_VALID_STRUCTURE, tmp_path, _TEST_PROJECTNAME)

    # Assert
    assert Path.exists(tmp_path / "src/test_project/__init__.py")
    assert file.read_text() == "test"


def test_validate_structure(tmp_path):
    # Create a valid and an invalid directory tree
    utils.create_structure(_VALID_STRUCTURE, tmp_path, "test_project")
    utils.create_structure(_INVALID_STRUCTURE, tmp_path, "test_invalid_project")
    # assert if the given directory tree passes or fails the test when comparing to the correct schema
    assert utils.validate_structure(_VALID_STRUCTURE, "test_project", tmp_path)
    assert not utils.validate_structure(
        _VALID_STRUCTURE, "test_invalid_project", tmp_path / "test_invalid_project"
    )
