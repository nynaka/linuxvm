# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Virtual Machine Memo'
copyright = '2024, hogehoge'
author = 'hogehoge'

version = '0.1'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # 自動生成ドキュメントの拡張
    'sphinx.ext.napoleon', # GoogleスタイルおよびNumpyスタイルのdocstringを解釈するための拡張
    'myst_parser',         # MyST (Markedly Structured Text) パーサーを有効化
    'sphinx_markdown_tables',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.seqdiag',
    'sphinxcontrib.actdiag',
    'sphinxcontrib.nwdiag',
    'sphinxcontrib.rackdiag',
    'sphinxcontrib.packetdiag',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',  # Markdownの拡張子を設定
}


templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
