# ValidMind

ValidMind helps model developers and model validators streamline communication and automate the model documentation process.

# Documentation

The home for our user-facing documentation and related infrastructure. If you want to make updates to our external docs site, you're in the right place.

## How to contribute

We believe in the power of collaboration and welcome contributions from the community. If you've noticed an issue or have ideas for improvement, please submit an issue or create a pull request. A member of ValidMind's documentation team will review your suggestions and support you in contributing to the docs.

If you are creating a pull request, make sure to test your changes by rendering or previewing the site.

If this is your first time contributing, you will be asked to sign a contributer agreement.

**ValidMind documentation:** https://docs.validmind.ai/guide/get-started.html
**Community Slack:** site/guide/join-community.qmd

## Prerequisites

We use [Quarto](https://quarto.org) to develop our docs site, an open-source docs framework based on Pandoc that supports multiple input formats such as Quarto Markdown, Jupyter notebooks, and Markdown.

You need:

- [Quarto CLI](https://quarto.org/docs/get-started/)
- The Quarto extension for your IDE, such as [VS Code](https://marketplace.visualstudio.com/items?itemName=quarto.quarto)

## How our docs site is sourced

```bash
site
├── _source
|   └── validmind-python
|       └── docs
|           └── _build
|               └── validmind
|                   └── *.html, *.js
├── guide
│   └── *.qmd, *.svg, *.png
├── notebooks
|   ├── how_to
|   |   └── *.ipynb
│   └── *.ipynb
├── _quarto.yml
└── index.qmd
```
**_source/ ... validmind/** — Built Developer Framework API docs

**guide/** — Core docs sourced in Quarto Markdown

**notebooks/** — Jupyter notebooks copied from [validmind-python/notebooks](https://github.com/validmind/validmind-python/tree/main/notebooks) or Google Drive

**_quarto.yml** — Rendering options for the site, including navigation, search, footer, and more

**index.qmd** — Main landing page sourced in Quarto Markdown and HTML

## Preview the docs site

```bash
cd site
quarto preview
```

## Generate the docs site

Including fetching the source from other repos:

```bash
cd site
make docs-site
```

Just render the site:

```bash
cd site
quarto render
```

The rendered static HTML output lives in:

```bash
site
└── _site ...
    └── *.html, *.css, *.png, *.js ...
```