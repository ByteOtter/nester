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

To install Nester from `PyPi`, make sure you have `pip` aswell as at least `python 3.10.10` installed.

Open a Terminal and run:
```bash
pip install nester-struct
```

Note: The package name `nester` was already occupied by the time we released Nester to PyPi. Although we could not find a package with that name.<br>
We are currently investigating if we can get the name assigned to us.

---

## Install as `rpm`

We plan to build a Nester `rpm` package.

---

## Build from source

Nester uses `setuptools` as its build tool and `pyproject.toml` and `setup.cfg` as configuration files. To install the requirements for Nester, you can use `pip` as follows:

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

>Note: If you encounter any issues with dependencies or installation, please refer to the troubleshooting section or reach out for help in the issues section or via email.

---

<h3>Thank you for using Nester! <br> - Your Nester Team</h3>
