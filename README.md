README.md
===

## このリポジトリ

仮想マシン関連のメモです。

## ドキュメントのビルド方法

- venv のインストール

    ```bash
    sudo apt install python3-venv
    ```

- venv 環境作成と有効化

    ```bash
    python3 -m venv venv
    source ./venv/bin/activate
    ```

- ドキュメントのビルドツールのインストール

    ```bash
    pip install --break-system-packages \
        sphinx sphinx_rtd_theme \
        sphinxcontrib-actdiag \
        sphinxcontrib-blockdiag \
        sphinxcontrib-nwdiag \
        sphinxcontrib-seqdiag \
        myst_parser sphinx_markdown_tables
    ```

- 日本語フォントのインストール

    ```bash
    sudo apt install -y \
        fonts-ipafont fonts-ipaexfont
    ```

- 初期化

    ```bash
    sphinx-quickstart doc \
        --sep \
        --project "Virtual Machine Memo" \
        --author "hogehoge" \
        -v 0.1 \
        --release 0.1 \
        --language='en' \
        --no-batchfile
    ```

- source/conf.py の設定

    <details>
    <summary>主な変更差分</summary>
    ```diff
    --- /tmp/conf.py        2024-07-06 11:51:57.506867009 +0900
    +++ conf.py     2024-07-06 11:55:28.979027738 +0900
    @@ -16,7 +16,24 @@
     # -- General configuration ---------------------------------------------------
     # https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
    
    -extensions = []
    +extensions = [
    +    'sphinx.ext.autodoc',  # 自動生成ドキュメントの拡張
    +    'sphinx.ext.napoleon', # GoogleスタイルおよびNumpyスタイルのdocstringを解釈するための拡張
    +    'myst_parser',         # MyST (Markedly Structured Text) パーサーを有効化
    +    'sphinx_markdown_tables',
    +    'sphinxcontrib.blockdiag',
    +    'sphinxcontrib.seqdiag',
    +    'sphinxcontrib.actdiag',
    +    'sphinxcontrib.nwdiag',
    +    'sphinxcontrib.rackdiag',
    +    'sphinxcontrib.packetdiag',
    +]
    +
    +source_suffix = {
    +    '.rst': 'restructuredtext',
    +    '.md': 'markdown',  # Markdownの拡張子を設定
    +}
    +
    
     templates_path = ['_templates']
     exclude_patterns = []
    @@ -26,5 +43,5 @@
     # -- Options for HTML output -------------------------------------------------
     # https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
    
    -html_theme = 'alabaster'
    +html_theme = 'sphinx_rtd_theme'
     html_static_path = ['_static']
    ```
    <details>

- ドキュメントのビルド

    ```bash
    make html
    ```

    カレントディレクトリ配下に `build` ディレクトリが作成されます。

