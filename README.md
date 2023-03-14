# Documentation

The home for our user-facing documentation and related infrastructure. If you need to make updates to our external docs site, you're in the right place. 

## Prerequisites

We use [Quarto](https://quarto.org) to render our docs site, an open-source docs framework based on Pandoc that supports multiple input formats such as Quarto Markdown, Jupyter notebooks, and Markdown. Additionally, we use [Sphinx](https://www.sphinx-doc.org/en/master/) to source some Markdown content for our developer framework from Python docstrings.

To develop the docs site, you need:

- [Quarto CLI](https://quarto.org/docs/get-started/)
- The Quarto extension for your IDE, such as [VS Code](https://marketplace.visualstudio.com/items?itemName=quarto.quarto).

To run `make get-source`, you need:

- Sphinx `docutils` 
- Additional tooling, such as `sphinx_markdown_builder`, `myst_parser`, `dython`, `pandas_profiling`, and `shap`

## How our docs site is sourced

```bash
site
├── guide
│   └── *.qmd, *.svg, *.png
├── notebooks
│   └── *.ipynb
├── validmind
│   └── *.md
├── _quarto.yml
└── index.qmd
```

**guide/** — Core docs sourced in Quarto Markdown

**notebooks/** — Jyupiter notebooks copied from [validmind-python/notebooks](https://github.com/validmind/validmind-python/tree/main/notebooks)

**validmind/** — Developer framework docs built from [validmind-python/validmind/docs/](https://github.com/validmind/validmind-python/tree/main/validmind)

**_quarto.yml** — Rendering options for the site, including navigation, search, footer, and more

**index.qmd** — Main landing page sourced in Quarto Markdown

## Preview the docs site

```bash
cd site
quarto preview
```

## Update files sourced from other repos

```bash
cd site
make get-source
```

## Generate a static docs site

```bash
cd site
make get-source
quarto render
```

Ship the rendered static HTML ooutput for the docs site located in:

```bash
site
└── _site
    └── *.html, *.css, *.png, *.js ...
```

You can ship the generated static site as-is to a customer or deploy it on AWS S3 and point **docs.validmind.ai** there.