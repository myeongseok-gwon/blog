# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
project = 'Myeongseok Blog'
copyright = '2024, Myeongseok Gwon'
author = 'Myeongseok Gwon'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx_book_theme',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_book_theme'
html_theme_options = {
    'repository_url': 'https://github.com/myeongseok-gwon/blog',
    'use_repository_button': True,
    'use_issues_button': True,
    'use_download_button': True,
}

# -- Giscus 댓글 시스템 설정 -------------------------------------------------
html_context = {
    'giscus_repo': 'myeongseok-gwon/blog',
    'giscus_repo_id': 'R_kgDONNXfQw',
    'giscus_category': 'Announcements',
    'giscus_category_id': 'DIC_kwDONNXfQ84Cuhyx',
    'giscus_mapping': 'pathname',
    'giscus_strict': '0',
    'giscus_reactions_enabled': '1',
    'giscus_emit_metadata': '0',
    'giscus_input_position': 'bottom',
    'giscus_theme': 'preferred_color_scheme',
    'giscus_dark_theme': 'dark',
    'giscus_lang': 'ko',
}

# -- MyST 설정 -------------------------------------------------------------
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
    "html_admonition",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]
