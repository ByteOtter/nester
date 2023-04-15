# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Nester"
copyright = "2023, Christopher Hock aka ByteOtter"
author = "Christopher Hock aka ByteOtter"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc"]

templates_path = ["_templates"]
exclude_patterns = ["_build"]

source_suffix = ".rst"

master_doc = "index"

language = "en"

pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "navigation_with_keys": False,
    "logo_only": True,  # Hide the title and home icon in navigation bar
}
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]  # WIP
html_logo = "_static/index_logo.png"
