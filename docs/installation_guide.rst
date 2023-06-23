Installing Nester
=================

Nester will initially be offered in three ways:

- Installation using `pip` from pypi.org
- Installation as `rpm` package (coming soon)
- Building from source

Installation via `pip`
----------------------

`pip`, if you are not aware already, is the Python package manager. You can use it to install a huge variety of python packages stored on `PyPi <https://pypi.org>`_.

Simply run this in your terminal:

.. code-block:: shell

  pip install nester-struct


`pip` now installs nester with all its dependencies. That should be it!

Installation as `rpm` package
-----------------------------

Some systems may not initially ship with `python3` or `pip` or you may simply do not want to use `pip`.
For this reason we are planning to offer Nester in a varietly of different Linux packages.

As we are most familiar with the `rpm` format for openSUSE this is what we will offer first.

We can now offer a `.rpm` package!

To do so follow these steps (on openSUSE):

1. Add the repository

.. code-block:: shell

  sudo zypper addrepo `https://download.opensuse.org/repositories/home:kodymo/openSUSE_Tumbleweed/home:kodymo.repo`_

.. _`https://download.opensuse.org/repositories/home:kodymo/openSUSE_Tumbleweed/home:kodymo.repo`:


2. Refresh your repositories

.. code-block:: shell

  sudo zypper ref


3. Install Nester

.. code-block:: shell

  sudo zypper install python3-nester


Note: The repository contains three builds for nester for Python 3.9, 3.10 and 3.11. `zypper` will automatically decide which version to use when running the command above.

You can visit the repository on the [package maintainer's OBS account](https://build.opensuse.org/package/show/home:kodymo/python-nester).

Building from source
--------------------

Sometimes installing from shady sources may not be your thing. Fear nought!
You can also build it from source.

To do that simply clone or download `Nester's GitHub repository <https://github.com/ByteOtter/nester>`_ enter the `nester/` directory and run `pip install .` to install Nester.

Done!

We hope you have as much fun using Nester as we have building it!