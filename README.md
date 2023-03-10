# Documentation framework

A home for our user-facing documentation and related infrastructure. If you need to make updates to our external docs site, you're in the right place.

## How our docs site is rendered

We use [Quarto](https://quarto.org) to render our docs, an open-source docs framework based on Pandoc that has good support for multiple input formats. We source input from multiple repositories: 

```bash
site
├── _site
│   └── *.html, *.css, *.png, *.js ...
├── index.qmd
├── *.qmd
├── notebooks
│   └── *.ipynb
└── python-library
    └── *.md
```

_quarto.yml
: Rendering options for the site, including navigation, search, footer, and more.

*.qmd
: Quarto Markdown that contains our core docs, including getting started information, how-to guides,  glue for generated content, and more. 

*.ipynb
: Jyupiter notebooks sourced from validmind/validmind-python.

*.md
: Markdown for the VM developer framework generated from Python docstrings and sourced from validmind/validmind-python.

Input files from 

## Prerequisites

To render or develop the docs locally, you need:

- [Quarto CLI](https://quarto.org/docs/get-started/), plus the Quarto extension for your IDE, such as [VS Code](https://marketplace.visualstudio.com/items?itemName=quarto.quarto).
- The https://github.com/validmind/validmind-python repo in parallel with this one so that we can fetch some source content from there.

## Preview the docs site

```bash
cd site
make get-source
quarto preview
```

## Ship a static docs site

Rendered HTML output lives in `site/_site`. You can place this site into an AWS S3 bucket, for example, and open it in a browser.
