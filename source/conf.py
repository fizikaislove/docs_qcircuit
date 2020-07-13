# # Configuration file for the Sphinx documentation builder.
# #
# # This file only contains a selection of the most common options. For a full
# # list see the documentation:
# # https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# # -- Path setup --------------------------------------------------------------
#
# # If extensions (or modules to document with autodoc) are in another directory,
# # add these directories to sys.path here. If the directory is relative to the
# # documentation root, use os.path.abspath to make it absolute, like shown here.
# #
# # import os
# # import sys
# # sys.path.insert(0, os.path.abspath('.'))
#
#
# # -- Project information -----------------------------------------------------
#
# project = 'QCircuit'
# copyright = '2020, Ilia Besedin'
# author = 'Ilia Besedin'
#
# # The full version, including alpha/beta/rc tags
# release = '13072020'
#
#
# # -- General configuration ---------------------------------------------------
#
# # Add any Sphinx extension module names here, as strings. They can be
# # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# # ones.
# extensions = [
# ]
#
# # Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']
#
# # The language for content autogenerated by Sphinx. Refer to documentation
# # for a list of supported languages.
# #
# # This is also used if you do content translation via gettext catalogs.
# # Usually you set "language" from the command line for these cases.
# language = 'English'
#
# # List of patterns, relative to source directory, that match files and
# # directories to ignore when looking for source files.
# # This pattern also affects html_static_path and html_extra_path.
# exclude_patterns = []
#
#
# # -- Options for HTML output -------------------------------------------------
#
# # The theme to use for HTML and HTML Help pages.  See the documentation for
# # a list of builtin themes.
# #
# html_theme = 'alabaster'
#
# # Add any paths that contain custom static files (such as style sheets) here,
# # relative to this directory. They are copied after the builtin static files,
# # so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']


import sys, os
import sphinx_rtd_theme

from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer
from pygments.lexers.web import HtmlLexer
from pygments.lexers.web import JsonLexer

from datetime import datetime

lexers['php'] = PhpLexer(startinline=True)
lexers['php-annotations'] = PhpLexer(startinline=True)
lexers['html'] = HtmlLexer(startinline=True)
lexers['json'] = JsonLexer(startinline=True)

extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sensio.sphinx.configurationblock']

source_suffix = '.rst'
master_doc = 'index'

project = 'QCircuit'
copyright = ''
author = 'Ilia Besedin'

version = '1'
release = '13072020'

exclude_patterns = ['_build']

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']
templates_path = ['_templates']

html_theme_options = {
    'collapse_navigation': True,
    'display_version': True,
}

# html_context = {
#     'copyright_url': 'https://www.acme.com',
#     'current_year': datetime.utcnow().year
# }

def setup(app):
    app.add_stylesheet("css/style.css")