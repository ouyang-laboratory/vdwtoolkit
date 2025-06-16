# -- Path setup --------------------------------------------------------------
import os
import sys

# conf.py 的目录
conf_dir = os.path.dirname(__file__)
# 项目根目录（docs/ 上一级）
project_root = os.path.abspath(os.path.join(conf_dir, '..', '..'))
# 将项目根目录插入到 sys.path
sys.path.insert(0, project_root)

# -- Project information -----------------------------------------------------
project = 'vdW-Toolkit'
author = 'Hekai Bu'
release = '0.1'
version = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
]

autosummary_generate = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_title = f"{project} v{release} Documentation"

# -- Options for EPUB output -------------------------------------------------
epub_show_urls = 'footnote'
