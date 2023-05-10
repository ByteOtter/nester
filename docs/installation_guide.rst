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

--COMING SOON--

Some systems may not initially ship with `python3` or `pip` or you may simply do not want to use `pip`.
For this reason we are planning to offer Nester in a varietly of different Linux packages.

As we are most familiar with the `rpm` format for openSUSE this is what we will offer first.

Note: This is a feature we will offer at some point. No dates are planned yet!

To install it run

.. code-block:: shell

  sudo zypper in nester

This should install the package.

Building from source
--------------------

Sometimes installing from shady sources may not be your thing. Fear nought!
You can also build it from source.

To do that simply clone or download `Nester's GitHub repository <https://github.com/ByteOtter/nester>`_ enter the `nester/` directory and run `pip install .` to install Nester.

Done!

We hope you have as much fun using Nester as we have building it!