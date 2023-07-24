# Documentation

The home for our user-facing documentation and related infrastructure. If you need to make updates to our external docs site, you're in the right place.

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

**notebooks/** — Jyupiter notebooks copied from [validmind-python/notebooks](https://github.com/validmind/validmind-python/tree/main/notebooks) or Google Drive

**_quarto.yml** — Rendering options for the site, including navigation, search, footer, and more

**index.qmd** — Main landing page sourced in Quarto Markdown and HTML

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

Important: This action doesn't copy the Jupyter notebooks sourced from [Google Drive](https://drive.google.com/drive/folders/1o2TcY9PM-OkjBKdfenymuaeAIqarY4T2). You need to update these notebooks _manually_. 

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

## Deploy the production docs site

Automatically from the `prod` branch: merge a commit into the branch with the latest changes from `main`.

Manually from the `main` or `prod` branches:

```bash
make deploy-prod
```

## Deploy the docs demo site

Automatically from the `docs-demo` branch: merge a commit into the branch, e.g. with the files you want to deploy.

Manually from the `docs-demo` branch:

```bash
make deploy-demo
```

## Generate release notes

From the tag for the upcoming release, click 'Create release from tag', and then 'Generate release notes' to generate a list of pull requests to include in the upcoming release. Do this in the documentation, validmind-python, and frontend repos.

From the documentation repo:

```bash
cd site
make release-notes
```
Enter the release tag for each repo, and the date for the upcoming release.