import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '_ext')))

myst_roles = ["spec", "uc", "scmp"]

project = 'Fog Specification'
copyright = '2026, plachacwa'
author = 'plachacwa'

extensions = [
    'spec_tests',          # extension from _ext/spec_tests.py
    'myst_parser',
]

myst_enable_extensions = ["colon_fence"]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'furo'
html_title = 'Fog Specification'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = ['custom.js']

html_theme_options = {
    "light_css_variables": {
        "font-stack": "Bitter, Arial, sans-serif",
        "font-stack--monospace": "'Ubuntu Sans Mono', Consolas, monospace",
        "font-stack--headings": "'Open Sans', Arial, serif",
    },
}