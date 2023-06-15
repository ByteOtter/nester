"""This module contains tests for the click frontend."""

import pytest
from click.testing import CliRunner

import src.nester.nester_commands as commands
import src.nester.utils as utils


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture(scope="function", autouse=True)
def clean_after_test(fake_project_name):
    utils.clean(fake_project_name)


@pytest.mark.parametrize(
    "fake_project_name, fake_language, git_flag, expected_output",
    [
        (
            "test_project",
            "py",
            False,
            "Done! Happy Hacking!",
        ),
        (
            "test_project",
            "py",
            True,
            "Done! Happy Hacking!",
        ),
    ],
)
def test_nester_create(
    runner,
    fake_project_name,
    fake_language,
    git_flag,
    expected_output,
):
    # Arrange
    args = [fake_language, fake_project_name]
    if git_flag:
        args.append("--git")

    # Act
    result = runner.invoke(commands.create, args)

    # Assert
    assert expected_output in result.output
    assert result.exit_code == 0


def test_nester_validate(runner, fake_project_name, fake_language):
    # Arrange
    # Act
    # Assert
    assert 1


def test_cleanup(fake_project_name):
    runner = CliRunner()
    result = runner.invoke(commands.clean, ["--yes", fake_project_name])
    assert result.exit_code == 0
