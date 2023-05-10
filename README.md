<p align="center">
<img
    style="display: block;
           margin-left: auto;
           margin-right: auto;
           width:60%"
    src="./index_logo.png"
    alt="Our logo">
</img>
</p>
<h2 align="center" style="text-decoration:underline">Building the nest for you</h2>

<h3 style="text-decoration:underline">Welcome to Nester!</h3>
A small command line tool to set up the basic structure for your Python, C#, C++, Java or Ruby project.

**Index**
- [Introduction](#introduction)
- [Our Goal](#our-goal)
- [Installation](#installation)
  - [Get it on PyPi!](#get-it-on-pypi)
  - [Get it as an `.rmp` package](#get-it-as-an-rmp-package)
  - [Build it from source](#build-it-from-source)
- [Usage](#usage)
  - [CLI Mode](#cli-mode)
  - [Interactive / GUI - Mode (coming soon)](#interactive--gui---mode-coming-soon)
  - [Supported Languages](#supported-languages)
- [Documentation](#documentation)
    - [Read the Docs (wip)](#read-the-docs-wip)
    - [Towncrier (wip)](#towncrier-wip)
- [Contributing](#contributing)

## Introduction

When you are reading this, you are probably thinking "what?", "how?" and "why?".

**Nester** was born out of the desire to have an easier way to set up new projects without having to check what file or folder goes where.<br>
Just run a command, select a language and everything will be set up for you ready to go.

Now, you might say "but \<Your IDE HERE> can do this all on its own!", yes I realize that many modern IDEs will set up a new project perfectly fine for you. And some languages, such as GoLang, have their own CLI utilites to set everything up where it belongs.<br>
Let me tell you though, who cares?

## Our Goal

Our goal with **Nester** is to provide developers a quick and easy way to set up new projects adhearing to the given language's standard giving you more time to actually build your application without having to deal with mkdir-hell.

One simple cli-Command and Nester will do the rest for you, optionally even initializing a new git-repository for you.

## Installation

### Get it on PyPi!

`Nester` is finally released on [PyPi](https://pypi.org)!<br>
To do so, make sure you have at least `Python 3.10` and `pip` installed.<br>
To get `Nester` simply run:

```bash
pip install nester-struct
```
Your done! Have fun with `Nester`!

### Get it as an `.rmp` package

We plan to release Nester to pypi first and as an `.rpm` package in the future.

TBA

### Build it from source

If you want to contribute to `Nester` or just prefer building it yoursef, refer to the [Contributing Guide](docs/CONTRIBUTING.md) to find out how.


## Usage

**Nester** strives to be easy to use and will have to modes of operation:

### CLI Mode

This mode will be the default and how **Nester** is supposed to be used.<br>
Simply call `nester`, hand it the operation and the language you want and whether you want to initialize a git repository alongside it. Done!

```
nester <OPERATION> <OPTIONAL -git FLAG> <LANGUAGE> <PROJECT_NAME>
```
The following operations will be available:
|`Operation`|Flags|Argument|Argument|Effect|
|-|-|-|-|-|
|`create`|`-g/--git`|`Language`|`Projectname`|Creates the project structure for the selected lanugage in *the current directory*. IF `-git` is set it will also call `git init` in this directory|
|`validate`|n/A|`Language`|`Projectname`|Checks the current directory and its sub-directories if it corresponds to the schema provided for the language|
|`clean`|`-y/--yes`|`Projectname`|n/A|Deletes the content of the specified project|

### Interactive / GUI - Mode (coming soon)

This is considered to be the fallback mode. If **Nester** is called without any arguments you will be asked to enter all parameters manually.

The parameters themselves will stay the same though.

```
nester
```

### Supported Languages

Currently planned support for the following languages is planned.

|Language|Parameter|Supported yet?|
|-|-|-|
|Python|`py`|:heavy_check_mark:|
|C|`c`|:heavy_check_mark:|
|C++|`cpp`|:heavy_check_mark:|
|C#|`cs`|:heavy_check_mark:|
|Ruby|`rb`|:heavy_check_mark:|
|Java|`java`|:heavy_check_mark:|

*Note:* Python will be set up with the `src-Layout` which currently seems to be the standard for Python projects and was the stone that started it all.

For the future we are also looking into supporting languages with built-in set up features simply by calling them aswell as other languages with standardized structure layouts, but for now this list is all which will be supported.

## Documentation

Good documentation is very important to us, even with such a small project like Nester. To this end we have two methods in place to build documentation for us:

#### Read the Docs (wip)

On our [Read the Docs](https://nester.readthedocs.io/en/latest/index.html#) we build the general documentation for the project. You can find the installation and usage guides there, aswell as an overview over the languages we support oder want to support.

Also there is the automatically build documentation of functions and modules that make Nester go.

#### Towncrier (wip)

Towncrier is used to build changelogs for us. It is required that Pull Requests, which change Nesters behaviour, include a changelog file.

## Contributing

We are happy to welcome you to the group of Nester contributors. Please check the [Contributing Guide](docs/CONTRIBUTING.md) to find out how you can help achieve our goal.
