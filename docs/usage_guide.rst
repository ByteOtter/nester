Usage
=====

Nester strives to be as easy to use as possible.


To achieve this it can be used in two ways:

CLI-Mode
--------

This is how Nester was intended to be used: As a small CLI-tool.
Nester has three main functions it can perform:

- `create`
- `validate`
- `clean`

Let us look into each three in more detail...

Nester create
~~~~~~~~~~~~~~~

.. function:: nester create(language, projectname, [-g|--git])

   Creates the project structure for the given project.
   If you are already in a directory which matches the name of the given project, the source files will be created in your current directory.
   If not Nester will automatically create a directory for your project.

   :param language: The shortform of a supported programming language. Refer to the :doc: `list of supported languages <supported_languages>`.
   :type language: str
   :param projectname: The name of the project package that will be created.
   :type projectname: str
   :param -g|--git: An optional flag to initialize a Git repository in the project directory. If specified, a Git repository will be created simultaneously with the project structure.
   :type -g|--git: flag
   :return: None
   :rtype: None

Nester validate
~~~~~~~~~~~~~~~

.. function:: nester validate(language, projectname)

  Validates the file structure of the given project against our JSON schmemas.
  Files you created, which are therefore not part of our schema, or such which have been created by other utilites (e.g. `git init`) will be ignored.

  :param language: The shortform of a supported programming language. Refer to the :doc: `list of supported languages <supported_languages>`.
  :type language: str
  :param projectname: The name of the project or package you want to validate
  :type projectname: str
  :return: Tells you via Terminal wether your structure lines up or not.
  :rtype: str

Nester clean
~~~~~~~~~~~~

.. function:: nester clean(projectname, [-y|--yes])

  Deletes the *entire* content of the given project directory.

  This action **cannot** be undone.

  :param projectname: The name of the project you want to delete.
  :type projectname: str
  :param -y|--yes: An optional flag to auto-confirm your decision and skip the "Are you sure?" dialogue.
  :type -y|--yes: flag
  :return: None
  :rtype: None
