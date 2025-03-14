# ValidMind

![](site/about/ValidMind-logo-color.svg)

This is the home for the user-facing documentation and related infrastructure for ValidMind. If you want to make updates to our external docs site, you're in the right place!

## Contributing to the documentation

We believe in the power of collaboration and welcome contributions from the community. If you've noticed an issue or have ideas for improvement, please create a pull request or submit an issue. A member of ValidMind's documentation team will review your suggestions and support you in contributing to the docs. 

- Follow the [Quickstart](https://docs.validmind.ai/get-started/developer/try-with-jupyterhub.html) for a 15-minute introduction to the ValidMind Library and ValidMind Platform.

- Read the [ValidMind Library docs](https://docs.validmind.ai/developer/get-started-validmind-library.html) for more information about ValidMind's open source tests and Jupyter notebooks.

- Join the [Community Slack](https://docs.validmind.ai/about/contributing/join-community.html) to ask questions, get support, and connect with Model Risk Management (MRM) practioners.

## Prerequisites

We use [Quarto](https://quarto.org) to develop our docs site, an open-source docs framework based on Pandoc that supports multiple input formats such as Quarto Markdown, Jupyter notebooks, and Markdown.

You need:

- [Quarto CLI](https://quarto.org/docs/get-started/)
- The Quarto extension for your IDE, such as [VS Code](https://marketplace.visualstudio.com/items?itemName=quarto.quarto)
- For Windows operating systems, install the `make` command via [Cygwin](https://cygwin.com/install.html)

### Additional dependencies

Some interactive tables, such as our breaking changes and dependency history rely you have R and some R packages installed in order for you to be able to preview or render certain pages of the docs site locally.

**Refer to the [Breaking changes and deprecations](site/releases/breaking-changes/README.md) guide** for more information on how to install R and set up these tables.

## How to contribute

> [!IMPORTANT]
> First, read through and familiarize yourself with our [ValidMind style guide](https://docs.validmind.ai/about/contributing/style-guide/style-guide.html).

- Our core user guides are sourced in Quarto Markdown under [`site/guide`](https://github.com/validmind/documentation/tree/main/site/guide). 
- If you create new documentation, make sure to add it to the [`_quarto.yml`](https://github.com/validmind/documentation/blob/main/site/_quarto.yml) file.

If you are creating a pull request, test your changes by rendering or previewing the site. Note that if this is your first time contributing, you will be asked to sign a contributor license agreement (CLA).

### Preview the docs site

```bash
cd site
quarto preview
```

### Render the docs site

To render the site:

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

## Directory map

### `site`
Core files you manipulate live under `site` in these key directories that more or less correlate to the sections of the docs site reachable via the top navigation bar:

- `about` 
- `developer` 
- `faq` 
- `get-started` 
- `guide`  
- `support` 

These directories may have sub-directories depending on their size and grouped sub-topics contained within. 

#### Special `site` directories
- `releases` — Correlates to the "Releases" section under [About](https://docs.validmind.ai/about/overview.html).
- `training` — Correlates to the "Training" section under [Get Started](https://docs.validmind.ai/training/training-overview.html).

#### Supporting `site` directories
- `_site` — This is where static files rendered by `quarto render` get placed.
- `assets` — This is where general shared assets live (stylesheets, promotional images, all videos, etc.).
- `internal` — For internal testing only.
- `notebooks` — This is where notebooks retrieved from the [`validmind-library` repo](https://github.com/validmind/validmind-library) live.
- `tests` — This is where test descriptions generated from the Python source in the [`validmind-library` repo](https://github.com/validmind/validmind-library) live.

### Auxiliary `internal` directories

- `templates` — You can find generic structural templates in this folder here to help you build your guides.
- `testing` — When tests are complete, they get moved here from `site/internal`.

## Working with files

### `.qmd`

Files for the docs site are created using [Quarto Markdown](https://quarto.org/docs/authoring/markdown-basics.html) (`.qmd`). These, along with any Jupyter Notebooks pulled in from `validmind-library`, get rendered into HTML files. 

#### Hyperlinks

When constructing links, refer to the `.qmd` file as Quarto will properly render these into `.html` links on your behalf and check to see if the destinations are able to be resolved:

| Correct | Incorrect |
|---|---|
| `[Get started with JupyterHub](get-started/developer/try-with-jupyterhub.qmd)` | `[Get started with JupyterHub](get-started/developer/try-with-jupyterhub.html)` |

When constructing filepaths, including while using [Quarto's Includes](https://quarto.org/docs/authoring/includes.html) (single-sourcing feature), you'll also want start with the root directory whenever possible as this minimizes usage of unclear relative paths: 

| Correct | Incorrect |
|---|---|
| `[Register models in the inventory](/guide/model-inventory/register-models-in-inventory.qmd)` | `[Register models in the inventory](../../register-models-in-inventory.qmd)` |

### Column layouts

Use the installed [Tachyons Extension For Quarto](https://github.com/nareal/tachyons) to build column layouts so that they are properly mobile responsive. 

Refer to the [`tachyons-flexbox.qmd`](templates/tachyons-flexbox.qmd) template for an example.

### Asset files

If there are additional files that Quarto does not copy over automatically, place them into `/assets`. These files might include: 

- Videos
- Stylesheets
- Font files

### Jupyter Notebooks

Notebooks (`.ipynb` files) are NOT edited via this `documentation` repo, as any changes will be overridden. 

Changes need to be made in the [root repository `validmind-library`](https://github.com/validmind/validmind-library) and pulled into this one with:

```bash
make get-source
```

After you pull in the changes, commit them to this repo as part of the release notes process.

> [!TIP]
> **Want to author new code samples?** Refer to our [Jupyter Notebook template Quickstart](https://github.com/validmind/validmind-library/tree/main/notebooks/templates)!

<!-- September 16, 2024: Need to mention rendered Python `.html` docs and generated `.md` test descriptions -->

## Build and serve the site with Docker

You can build and serve the static HTML docs site using Docker — for deployment as part of our product or for testing in a consistent local environment.

### Prerequisites  

- [Docker](https://docs.docker.com/get-docker/)

### Build the site  

```bash
cd site
make docker-build
```

This command:

1. Gets all the source files.
2. Renders the static site in `site/_site`.  
3. Builds a Docker image using the `Dockerfile`.  

### Serve the site  

```bash
cd site
make docker-serve
```

Access the site locally: http://localhost:4444  
