<p align="center">
<img
    style="display: block;
           margin-left: auto;
           margin-right: auto;
           width:40%"
    src="./index_logo.png"
    alt="Our logo">
</img>
</p>
<h2 align="center" style="text-decoration:underline">Building the nest for you</h2>

<h1>Install Nester</h1>

<h2> Notice</h2>

Nester is currently released to `PyPi`, the Python Packaging Index.

---
<h2>Index</h2>

- [Install via `pip`](#install-via-pip)
- [Install as `rpm`](#install-as-rpm)
- [Build from source](#build-from-source)

---
## Install via `pip`

To install Nester from `PyPi`, make sure you have `pip` aswell as a reasonably up-to-date version of Python 3 installed.

Nester has been validated to work with Python 3.10 and 3.11. However, it should work with older versions of python too,
as long as they can provide an appropriate version of both `Click` and `Questionary`.

If you run an outdated version of Python and run into issues with Nester, please note that we cannot provide a backwards
patch for these problems.

Open a Terminal and run:
```bash
pip install nester-struct
```

Note: The package name `nester` was already occupied by the time we released Nester to PyPi. Although we could not find
a package with that name.<br>
We are currently investigating if we can get the name assigned to us.

---

## Install as `rpm`

NOTE: This functionality is currently undergoing changes. We recommend installing Nester via `pip` to receive the newest
changes to the project.

Note: The `.rpm`-release of Nester can straggle behind in features to its `pip` release. This is because the OBS build
is being maintained by a volunteer so it can take a couple days for changes to be released here.

To install Nester via its OBS repository follow these steps (on openSUSE):

1. Add the repository
```bash
sudo zypper addrepo https://download.opensuse.org/repositories/home:kodymo/openSUSE_Tumbleweed/home:kodymo.repo
```
2. Refresh your repositories
```bash
sudo zypper ref
```
3. Install Nester
```bash
sudo zypper install python3-nester
```
Note: The repository contains three builds for nester for Python 3.9, 3.10 and 3.11. `zypper` will automatically decide
which version to use when running the command above.

You can visit the repository on the [package maintainer's OBS account](https://build.opensuse.org/package/show/home:kodymo/python-nester).


---

## Build from source

Nester uses `setuptools` as its build tool and `pyproject.toml` and `setup.cfg` as configuration files. To install the
requirements for Nester, you can use `pip` as follows:

1. Change to the Nester directory:

```shell
cd nester
```

2. Install the dependencies listed in `setup.cfg` using `pip`:

```shell
pip install -e .
```

This should install all necessary requirements for nester aswell as nester itself.

You can try it out now by calling

```shell
nester -h
```

>Note: If you encounter any issues with dependencies or installation, please refer to the troubleshooting section or
reach out for help in the issues section or via email.

---

<h3>Thank you for using Nester! <br> - Your Nester Team</h3>
