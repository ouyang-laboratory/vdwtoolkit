# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------
# Add project root (two levels up) to Python path, so Sphinx can import vdwtoolkit
sys.path.insert(0, os.path.abspath(os.path.join('..', '..')))

# -- Project information -----------------------------------------------------
project = 'vdwtoolkit'
copyright = '2025, Hekai Bu'
author = 'Hekai Bu'

# The full version, including alpha/beta/rc tags
release = '0.1'
version = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]

# Generate autosummary pages automatically
autosummary_generate = True

# Intersphinx mapping for cross-referencing other projects
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

# Paths that contain templates, relative to this directory
templates_path = ['_templates']

# List of patterns, relative to source directory, to ignore when looking for source files
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
import sphinx_rtd_theme

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_title = f"{project} v{release} Documentation"

# -- Options for EPUB output -------------------------------------------------
epub_show_urls = 'footnote'
