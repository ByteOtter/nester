"""
This module contains unit tests for the utils.py functions
"""

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
    with mock.patch("builtins.open", mock.mock_open(read_data=fake_json)):
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
