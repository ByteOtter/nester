Usage
=====

Nester strives to be as easy to use as possible.


To achieve this it can be used in two ways:

CLI-Mode
--------

This is how Nester was intended to be used: As a small CLI-tool.
Nester has four main functions it can perform:

- `create`
- `validate`
- `list`
- `clean`

Let us look into each of the four commands in more detail...

Nester create
~~~~~~~~~~~~~~~

.. function:: nester create(language, project_name, [-g|--git])

   Creates the project structure for the given project.
   If you are already in a directory which matches the name of the given project, the source files will be created in your current directory.
   If not Nester will automatically create a directory for your project.

   :param language: The shortform of a supported programming language. Refer to the :doc: `list of supported languages <supported_languages>`.
   :type language: str
   :param project_name: The name of the project package that will be created.
   :type project_name: str
   :param -g|--git: An optional flag to initialize a Git repository in the project directory. If specified, a Git repository will be created simultaneously with the project structure.
   :type -g|--git: flag
   :param --no-log: An optional flag to disable project logging for the current project.
   :type --no-log: flag
   :return: None
   :rtype: None

Nester validate
~~~~~~~~~~~~~~~

.. function:: nester validate(language, project_name)

  Validates the file structure of the given project against our JSON schmemas.
  Files you created, which are therefore not part of our schema, or such which have been created by other utilites (e.g. `git init`) will be ignored.

  :param language: The shortform of a supported programming language. Refer to the :doc: `list of supported languages <supported_languages>`.
  :type language: str
  :param project_name: The name of the project or package you want to validate
  :type project_name: str
  :return: Tells you via Terminal wether your structure lines up or not.
  :rtype: str

Nester log
~~~~~~~~~~~

.. function:: nester log()

  Lists all previously created projects, which had logging enabled, in a table.

  :param --clean: An optional flag to clean up orphaned log entries.
  :type --clean: flag
  :return: None
  :rtype: None

Nester clean
~~~~~~~~~~~~

.. function:: nester clean(project_name, [-y|--yes])

  Deletes the *entire* content of the given project directory.

  This action **cannot** be undone.

  :param project_name: The name of the project you want to delete.
  :type project_name: str
  :param -y|--yes: An optional flag to auto-confirm your decision and skip the "Are you sure?" dialogue.
  :type -y|--yes: flag
  :return: None
  :rtype: None

Interactive Mode
----------------

Calling Nester in the Terminal without providing any additional arguments launches `interactive mode`.

Here you can choose the operation to perform and are guided through the process for each of them.
