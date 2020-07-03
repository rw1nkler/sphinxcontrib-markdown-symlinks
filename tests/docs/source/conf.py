# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import subprocess
from markdown_code_symlinks import LinkParser, MarkdownSymlinksDomain

# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Markdown Symlinks Tests'
copyright = '2020, author'
author = 'author'

# The full version, including alpha/beta/rc tags
release = '1.0'
needs_sphinx = '3.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# --- Other configuration options --------------------------------------------

source_parsers = {
    '.md': 'markdown_code_symlinks.LinkParser',
}

source_suffix = ['.rst', '.md']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Print Used Python Packages -----------------------------------------------

print("\n### ---------- List of Used Python Packages ---------- ###\n\n")
subprocess.run("pip3 list --format=columns", shell=True)
print("----------------------------------------------------------\n")

# -- Markdown Symlinks Setup --------------------------------------------------

def setup(app):
    github_code_repo = 'https://github.com/rw1nkler/sphinxcontrib-markdown-symlinks/'
    github_code_branch = 'blob/fix_links/'

    docs_root_dir = os.path.realpath(os.path.dirname(__file__))
    code_root_dir = os.path.realpath(os.path.join(docs_root_dir, "..", ".."))

    MarkdownSymlinksDomain.init_domain(
        github_code_repo, github_code_branch, docs_root_dir, code_root_dir)
    MarkdownSymlinksDomain.find_links()
    app.add_domain(MarkdownSymlinksDomain)
    app.add_config_value(
        'recommonmark_config', {
            'github_code_repo': github_code_repo,
        }, True)
