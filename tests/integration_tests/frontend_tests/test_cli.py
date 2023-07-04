"""This module contains tests for the click frontend."""

import pytest
from click.testing import CliRunner

import nester.cli as commands
import nester.core.utils as utils


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


def test_nester_validate(runner, fake_language, fake_project_name):
    # Arrange
    args = [fake_language, fake_project_name]
    runner.invoke(commands.create, args)

    # Act
    result = runner.invoke(commands.validate, args)

    # Assert
    assert "Everything looks good. :)" in result.output
    assert result.exit_code == 0


def test_clean(runner, fake_language, fake_project_name):
    # Arrange
    args = [fake_language, fake_project_name]
    runner.invoke(commands.create, args)

    # Act
    result = runner.invoke(commands.clean, ["--yes", fake_project_name])

    # Assert
    assert "Cleaning up your mess..." in result.output
    assert "Everything cleaned up!" in result.output
    assert result.exit_code == 0


def test_empty_log(runner):
    # Act
    result = runner.invoke(commands.log)

    # Assert
    assert "No projects logged." in result.output
    assert result.exit_code == 0


def test_log(runner, fake_language, fake_project_name):
    # Arrange
    args = [fake_language, fake_project_name]
    runner.invoke(commands.create, args)

    # Act
    result = runner.invoke(commands.log)

    # Assert
    assert fake_language and fake_project_name in result.output
    assert result.exit_code == 0


def test_clean_with_unknown_project(runner):
    # Arrange
    project_name = "no_project"

    # Act
    result = runner.invoke(commands.clean, ["--yes", project_name])

    # Assert
    assert f"Error: Project '{project_name}' not found!" in result.output
    assert result.exit_code == 0
