# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------
import os
import sys

# Add project root to Python path so Sphinx can find your modules
sys.path.insert(0, os.path.abspath('/workspaces/scpoly/scpoly'))

# -- Project information -----------------------------------------------------
project = 'scPOLY demo'
copyright = '20xx, FamilyName'
author = 'FamilyName'

release = '0.1'
version = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',       # For extracting docstrings
    'sphinx.ext.autosummary',   # For generating summary tables
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',      # For Google/NumPy style docstrings
    'sphinx.ext.viewcode',      # Links to source code
]

# -- Autosummary configuration -----------------------------------------------
autosummary_generate = True          # Generate summary pages automatically
autosummary_import_members = True    # Import modules to generate docs
autosummary_ignore_module_all = False

# -- Autodoc configuration ---------------------------------------------------
autodoc_default_options = {
    'members': True,           # Include class/instance members
    'member-order': 'bysource',# Order as in source code
    'special-members': '__init__',  # Include __init__ methods
    'undoc-members': True,     # Include undocumented members
    'exclude-members': '__weakref__',
    'show-inheritance': True,  # Show class inheritance
}

autodoc_typehints = 'description'    # Place type hints in description
autodoc_member_order = 'bysource'    # Keep original order
autodoc_class_signature = 'separated'

# -- Napoleon configuration for docstring parsing ----------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_param = True
napoleon_use_keyword = True
napoleon_use_rtype = True

# -- Intersphinx configuration -----------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output -------------------------------------------------
html_theme = 'furo'

# Add these for better navigation
html_show_sourcelink = True
html_context = {
    'display_github': False,  # Set to True if you want GitHub links
    'github_user': 'yourusername',
    'github_repo': 'yourrepo',
    'github_version': 'main',
    'conf_py_path': '/docs/',
}

# -- Options for EPUB output -------------------------------------------------
epub_show_urls = 'footnote'