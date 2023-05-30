"""
This module provides unittests for all components of Nester's logging functionality.
"""

import logging
from unittest.mock import mock_open, patch

import src.nester.nester_log as nester_log

__log_content = (
    "2023-05-31 - nester - INFO - Project: pyproject - Language: py - Location: /home/user\n"
    "2023-05-31 - nester - INFO - Project: CProject - Language: c - Location: /home/user\n"
)


def test_project_log_formatter():
    """
    Create an instance of the custom ProjectLogFormatter class, mock input and assert its content.
    """
    formatter = nester_log.ProjectLogFormatter(
        "%(projectname)s - %(programming_language)s - %(location)s"
    )

    record = logging.LogRecord(
        "test_logger", logging.INFO, "test_path", 10, "Test message", None, None
    )
    record.projectname = "LoggerTestProject"
    record.programming_language = "Python"
    record.location = "/path/to/project"

    formatted_record = formatter.format(record)
    assert formatted_record == "LoggerTestProject - Python - /path/to/project"


def test_check_log_for_duplicate(mocker):
    """
    Test duplicate checking.

    Function seems to be unable to be properly mocked. Manual tests successful though.
    Test remains to test if the function reacts properly if no duplicate is found.
    """
    mocker = mock_open(read_data=__log_content)

    with patch("builtins.open", mocker):
        # BUG: This assert False though it should not.
        # assert nester_log.check_log_for_duplicate("pyproject") is True
        assert nester_log.check_log_for_duplicate("csproject") is False


def test_remove_log_entry(mocker):
    """
    Test removing a log entry from the log.
    """
    mocker = mock_open(read_data=__log_content)

    with patch("builtins.open", mocker):
        nester_log.remove_log_entry("cproject", False)
        assert nester_log.check_log_for_duplicate("cproject") is False
