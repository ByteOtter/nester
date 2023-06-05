.. _nester_contributing:

Contributing to Nester
=======================

Thank you for your interest in contributing to Nester! Nester is a tool for setting up programming project structures using JSON schemas stored in `src/nester/templates`. To make the contribution process smooth and efficient, please read the following guide.

Clone the Repository
--------------------

To start contributing to Nester, you will first need to clone the GitHub repository. You can do this by following these steps:

1. Go to the `Nester's GitHub repository`_
2. Click on the "Fork" button in the top right corner to create a fork of the repository on your GitHub account.
3. Clone your forked repository to your local machine using `git clone` command. Replace `yourusername` with your actual GitHub username:

.. code-block:: bash

  git clone git@github.com:yourusername/nester.git


Now you have a local copy of the Nester repository on your machine.

Install Requirements
--------------------

Nester uses `setuptools` as its build tool and `pyproject.toml` and `setup.cfg` as configuration file.

1. Change to the Nester directory:

.. code-block:: shell

  cd nester


2. Install the dependencies listed in `setup.cfg` using `pip`:

.. code-block:: shell

  pip install -e .

.. _Nester's GitHub repository:
  https://github.com/ByteOtter/nester

This should install all necessary requirements for nester as well as nester itself.

Use Pull Request and Issue Templates
------------------------------------

As a project owner, I encourage you to use the provided Pull Request and Issue templates when contributing to Nester. These templates provide guidelines and instructions for creating effective Pull Requests (PRs) and Issues. Please follow the template and provide as much information as possible to help us understand your contribution or question.

When creating a PR, make sure to include a detailed description of the changes you made, including any relevant code changes, tests, and documentation updates. If your contribution requires a new feature or a bug fix, please explain the rationale behind it and provide any necessary context.

For issues, please provide a clear and concise description of the problem, along with any relevant steps to reproduce it, error messages, and expected behavior.

By using the provided templates, you can help ensure that your contributions are reviewed and addressed in a timely manner, and that your questions are answered effectively.

Thank you for your contribution to Nester! We appreciate your effort and look forward to reviewing your contributions. If you have any questions, feel free to ask in the issues section or via email.

Feature Requests
----------------

Like most other projects out there we strive to expand Nester's functionality and language support. However, there are some guidelines we would like you to respect when it comes to suggesting new languages specifically.

- The suggested language must have at least a widely accepted standard of how a project needs to be structured. This structure must make sense and must be able to be read by the language's compiler or build systems

- Documentation needs to be provided as context when suggesting a new language structure or the change of an existing one. A good example would be official style guides found in the language's documentation

- Languages with existing set up commands. We are aware that there are languages (Like Go, Ruby or Rust) which come with some form of CLI setup utility. And despite us being interested in linking them into Nester as well (by calling their utility), for now we would like you to refrain from suggesting these as they do not have priority for us.

Keeping Style
-------------

To maintain consistent code style in Nester, we use the `Black`_ code formatter. Before submitting your changes, please run the Black formatter on your code to ensure it adheres to the project's style guidelines.

After installing the dependencies and setting up the development environment with `pip install -e .`, you should have Black already installed. You can now run the following command from the root directory of the Nester repository:

.. code-block:: shell

  black .

.. _Black:
   https://black.readthedocs.io/en/stable/index.html

Additionally, you can make your life simpler by having `pre-commit` installed.

This tool uses the `.pre-commit-config.yaml` to run checks on your code before you commit your changes with `git`.

**Note**: If the black runner of `pre-commit` changes a file you need to `git add` it again. It is a little quirky sometimes.

Documentation
-------------

We highly value good documentation to help users understand and use Nester effectively. When contributing to Nester, please make sure to follow these documentation guidelines:

1. Every commit must have a changelog file containing a sensible changelog message. These files will be built by Towncrier.
2. When contributing new features, please update the existing documentation or add new documentation as necessary. Nester's documentation is built using `Sphinx`_ and published on Read the Docs.

**Note**: If you need help with writing documentation, please reach out to us for assistance. Your contributions to documentation are highly appreciated!

.. _Sphinx:
  https://www.sphinx-doc.org/en/master/

Submitting a Pull Request
-------------------------

When you are ready to submit your contribution, please follow these steps:

1. Create a new branch for your changes. Use a descriptive branch name that summarizes the purpose of your changes.

2. Make your changes and commit them with a clear commit message.

3. Push your branch to your forked repository on GitHub.

4. Open a pull request against the `main` branch of the Nester repository. Please provide a clear title and description for your pull request, and reference any relevant issues or discussions.

5. Your pull request will be reviewed by the project maintainers, and feedback will be provided. Please be responsive to any comments or requests for changes.

6. Once your pull request is approved and all checks pass, it will be merged into the `main` branch.

7. Thank you for your contribution to Nester! Your efforts are greatly appreciated.

**Note**: We advise you to pull the latest changes from the upstream repository and rebase your branch before submitting your Pull Request to avoid Merge Conflicts.

Happy hacking!

\- Your Nester Team!