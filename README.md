# Documentation framework

A home for our user-facing documentation and related infrastructure. If you need to make updates to our external docs site, you're in the right place.

## How our docs site is rendered

We use [Quarto](https://quarto.org) to render our docs, an open-source docs framework based on Pandoc that supports multiple formats. Source content lives in `site/`, with HTML output rendered in `site/_site`:

```bash
site
├── _site
│   └── *.html, *.css, *.png, *.js ...
├── _quarto.yml
├── index.qmd
├── *.qmd
├── notebooks
│   └── *.ipynb
└── python-library
    └── *.md
```

**_quarto.yml** — Rendering options for the site, including navigation, search, footer, and more.

**index.qmd**, ***.qmd** — Quarto Markdown that contains our core docs and landing page.

***.ipynb** — Jyupiter notebooks sourced from validmind/validmind-python.

***.md** — Developer framework sourced from validmind/validmind-python.


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

The generated static site can be shipped or deployed as-is.

For example, you should be able to deploy the contents of `site/_site` into an AWS S3 bucket that you point **docs.validmind.ai** to.
