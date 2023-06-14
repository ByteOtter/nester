"""Thi module contains fixtures specifically needed for running unittests."""

import pytest


@pytest.fixture
def fake_log_content():
    log_content = (
        "2023-05-31 - nester - INFO - Project: pyproject - Language: py - Location: /home/user\n"
        "2023-05-31 - nester - INFO - Project: CProject - Language: c - Location: /home/user\n"
    )
    return log_content
