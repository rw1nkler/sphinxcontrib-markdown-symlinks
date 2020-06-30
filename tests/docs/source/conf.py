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
# import sys
# sys.path.insert(0, os.path.abspath('.'))

from markdown_code_symlinks import LinkParser, MarkdownSymlinksDomain

# -- Project information -----------------------------------------------------

project = 'Markdown Symlinks Tests'
copyright = '2020, Author'
author = 'Author'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'python'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

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

def setup(app):
    github_code_repo = 'https://github.com/rw1nkler/sphinxcontrib-markdown-symlinks'
    github_code_branch = 'fix_images'

    docs_root_dir = os.path.realpath(os.path.dirname(__file__))
    # Create code root dir relative to docs_root_dir
    code_root_dir = os.path.realpath(os.path.join(docs_root_dir, "..", ".."))

    MarkdownSymlinksDomain.init_domain(
        github_code_repo, github_code_branch, docs_root_dir, code_root_dir)
    MarkdownSymlinksDomain.find_links()
    app.add_domain(MarkdownSymlinksDomain)
    app.add_config_value(
        'recommonmark_config', {
            'github_code_repo': github_code_repo,
        }, True)
