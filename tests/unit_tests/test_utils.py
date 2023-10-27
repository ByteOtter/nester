"""
This module contains unit tests for the utils.py functions
"""

import tempfile
from pathlib import Path
from unittest import mock

import nester.core.utils as utils


def test_detect_languages():
    languages = utils.detect_languages()

    assert "py" in languages
    assert "cpp" in languages
    assert "c" in languages
    assert "cs" in languages
    assert "java" in languages
    assert "rb" in languages


def test_load_json(valid_structure):
    # Arrange
    fake_json = '{"src": {"test_project": {"__init__.py": "test"}}}'

    # Act
    with mock.patch("builtins.open", mock.mock_open(read_data=fake_json)):
        result = utils.load_json("py", "test")

    print(valid_structure, result)
    # Assert
    assert result == valid_structure


def test_create_structure(tmp_path, fake_project_name, valid_structure):
    # Arrange
    source_path = Path.joinpath(tmp_path, "src")
    project_path = Path.joinpath(source_path, fake_project_name)
    file = Path.joinpath(project_path, "__init__.py")

    # Act
    utils.create_structure(valid_structure, tmp_path, fake_project_name)

    # Assert
    assert Path.exists(tmp_path / "src/test_project/__init__.py")
    assert file.read_text() == "test"


def test_rename_structure(tmp_path, fake_project_name, fake_new_project_name):
    # Arrange
    # Create a temporary directory and files for testing
    with tempfile.TemporaryDirectory() as tmp_dir:
        old_project_dir = Path(tmp_dir) / fake_project_name
        old_project_dir.mkdir()
        file_path = old_project_dir / "test_file.txt"
        file_path.touch()

        with mock.patch(
            "nester.core.utils.get_project_dir", return_value=old_project_dir
        ):
            # Act
            utils.rename_project_directory(fake_project_name, fake_new_project_name)

            # Assert
            new_project_dir = Path(tmp_dir) / fake_new_project_name
            assert new_project_dir.exists()
            assert not old_project_dir.exists()
            new_file_path = new_project_dir / "test_file.txt"
            assert new_file_path.exists()
