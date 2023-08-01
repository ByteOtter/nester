"""
This module takes care of reading the stock configuration files located in the ```configs``` directory and dumps
their content into the already created empty config files.
"""

import subprocess
from typing import Any

import yaml

try:
    import tomllib as toml
except ImportError:
    import toml

from . import exceptions, supported_linters


def set_config_files_for_project(
    language: str, project_name: str, add_linters: bool
) -> None:
    """
    Will set config files for project.

    This function takes the project's language and name at creation time and will look for a folder containing the
    templates for various config files such as build files.

    If ```add_linters``` is true, the linter configuration files are added and the linters are installed when possible.

    If language is not supported, it will raise an exception and inform the user.

    :param language: The programming language the project is written in.
    :type language: str
    :param project_name: The name of the project that is being created.
    :type project_name: str
    """
    if add_linters:
        install_linters(language)

    match language:
        case "py":
            with open("configs/python/pyproject.toml.template", "r") as file:
                template_content: dict[str, Any] = toml.load(file)

            with open("pyproject.toml", "w") as file:
                toml.dump(template_content, file)

            if add_linters:
                # Add pylintrc
                with open("configs/python/pylint.template", "r") as file:
                    rc_template_content: str = file.read()

                with open(".pylintrc", "w") as file:
                    file.write(rc_template_content)

                # Add pre-commit-config
                with open("config/pre-commit-config.yaml.template") as file:
                    pre_commit_template_content = yaml.safe_load(file)

                with open(".pre-commit-config.yaml", "w") as file:
                    yaml.safe_dump(pre_commit_template_content)

                # Add linters to pyproject.toml
                with open("pyproject.toml", "r") as project_toml:
                    pyproject_config: dict[str, Any] = toml.load(project_toml)

                pyproject_config["project"]["dev-dependencies"] = {
                    "pylint": "*",
                    "black": "*",
                    "isort": "*",
                    "pre-commit": "*",
                }

                pyproject_config["tool"]["isort"] = {"profile": "black"}

                with open("pyproject.toml", "w") as project_toml:
                    toml.dump(pyproject_config, project_toml)

        case _:
            # If language is not supported, an error is raised.
            raise exceptions.UnsupportedLanguageException()

    # Install all specified build tools
    install_build_system(language)


def install_build_system(language: str) -> None:
    """
    Will attempt to install a project's build system.

    For various languages some build tools are supported, check the :py:mod:`supported_linters` module to see which.

    :param language: The programming language the project is written in. Used to install the list of supported tools.
    :type language: str
    """
    match language:
        case "py":
            for tool in supported_linters.py_build:
                subprocess.run(["pip", "install", tool])
        case _:
            raise exceptions.UnsupportedLanguageException


def install_linters(language: str) -> None:
    """
    Will install the linters and other dependencies for a given language. You can find this in the
    :py:mod:`supported_linters` module.

    :param language: The programming language the project is written in. Used to install the list of supported tools.
    :type language: str
    """
    match language:
        case "py":
            try:
                for linter in supported_linters.py_linters:
                    subprocess.run(["pip", "install", linter])
            except subprocess.CalledProcessError as exc:
                print(
                    "\033[91mError: Pip does not seem to be installed on your system. Install it and try again.\033[0m"
                )
        case _:
            raise exceptions.UnsupportedLanguageException
