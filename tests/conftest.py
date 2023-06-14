"""This module implements all necessary fixtures for running the integration tests."""

from pathlib import Path

import pytest


@pytest.fixture
def project_root():
    return Path(__file__).parent.absolute()


@pytest.fixture
def fake_language():
    return "py"


@pytest.fixture
def fake_project_name():
    return "test_project"


@pytest.fixture
def valid_structure():
    structure = {"src": {"test_project": {"__init__.py": "test"}}}
    return structure


@pytest.fixture
def invalid_structure():
    structure = {
        "invalid_directory": {"test_invalid_project": {"invalid.py": "invalid"}}
    }
    return structure
