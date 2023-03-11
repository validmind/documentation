# Documentation

The home for our user-facing documentation and related infrastructure. If you need to make updates to our external docs site, you're in the right place.

We use [Quarto](https://quarto.org) to render our docs site, an open-source docs framework based on Pandoc that supports multiple formats such as Quarto Markdown, Jupyter notebooks, and Markdown for content generated from Python docstrings. 

## Prerequisites

To develop the docs site locally, you need:

- [Quarto CLI](https://quarto.org/docs/get-started/), plus the Quarto extension for your IDE, such as [VS Code](https://marketplace.visualstudio.com/items?itemName=quarto.quarto).
- The [validmind-python](https://github.com/validmind/validmind-python) repo cloned in parallel with this one to fetch some source content.

## How our docs site is sourced

The source files for our docs site live in:

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

**notebooks/** — Jyupiter notebooks source copied from [validmind-python/notebooks](https://github.com/validmind/validmind-python/tree/main/notebooks)

**validmind/** — Developer framework Markdown source copied from [validmind-python/validmind](https://github.com/validmind/validmind-python/tree/main/validmind)

**_quarto.yml** — Rendering options for the site, including navigation, search, footer, and more

**index.qmd** — Main landing page sourced in Quarto Markdown

## Preview the docs site

```bash
cd site
make get-source
quarto preview
```

## Ship a static docs site

The rendered output HTML for our static site lives in:

```bash
site
└── _site
    └── *.html, *.css, *.png, *.js ...
```

You can ship the generated static site as-is to a customer or deploy it on AWS S3 and point **docs.validmind.ai** there.