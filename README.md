# ValidMind

![](site/logo.svg)

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
| `[Quickstart — Model Development](get-started/developer/quickstart-developer.qmd)` | `[Quickstart — Model Development](get-started/developer/quickstart-developer.html)` |

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

### URL configuration for Docker

If you need to change where our docs site links to ValidMind or JupyterHub, this section explains how.

Two parameters can be configured:

- `VALIDMIND_URL` — where to access the platform, defaults to our public ValidMind app
- `JUPYTERHUB_URL` — where to access JupyterHub, defaults to our public instance

#### How to configure

Pass environment variables through a Kubernetes manifest, use a config file, or use public defaults if none are specified.

Configure in a [Kubernetes manifest](validmind-docs.yaml):

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: validmind-docs
  labels:
    app: validmind-docs
spec:
  replicas: 1
  selector:
    matchLabels:
      app: validmind-docs
  template:
    metadata:
      labels:
        app: validmind-docs
    spec:
      containers:
      - name: validmind-docs
        image: validmind/docs:latest
        ports:
        - containerPort: 80
        env:
        - name: VALIDMIND_URL
          value: "https://your-custom-app.validmind.ai"
        - name: JUPYTERHUB_URL
          value: "https://your-custom-jupyter.validmind.ai"
```

Configure in `config.json`, generated with the Docker image:

```json
{
   "VALIDMIND_URL": "https://your-custom-app.validmind.ai",
   "JUPYTERHUB_URL": "https://your-custom-jupyter.validmind.ai"
 }
```

## Configuring Lighthouse checks

Lighthouse is an open-source tool that audits web pages for accessibility, performance, best practices, and SEO. We automatically run Lighthouse against PR preview sites to enable a better, accessible documentation for everyone.

By default, Lighthouse checks only the top-level pages in our site navigation, such as `/index.html`, `/guide/guides.html`, `/developer/validmind-library.html`, and so forth. You can configure this behavior in the workflow:

```sh
env:
  # To change the default depth level:
  # 0 — Top-level navigation only (e.g. /index.html, /guide/guides.html, /developer/validmind-library.html, etc.)
  # 1 — All first-level subdirectories (e.g. /guide/*.html)
  # 2 — All second-level subdirectories (e.g. /guide/attestation/*.html)
  # Note: While the crawler technically supports deeper levels, expect the workflow to take >2-12 hours to complete
  DEFAULT_DEPTH: '0'
```

**Tips:**

- On the first run, the workflow waits for a preview site to become available. For subsequent runs, it checks the currently available site, which may be behind HEAD. The PR comment shows which commit SHA was checked — rerun the check if needed.
- Use folder depths greater than zero only on working branches when you need a thorough site audit. Deeper checks take 2-12 hours to complete and significantly slow down the CI/CD pipeline. Do not merge depth changes to `main`.

## Vale linter

The Vale linter is used to enforce consistent writing style and catch common language issues in our documentation source. Vale runs automatically on pull requests but can also be run locally when addressing source issues.

### Running Vale locally

```sh
brew install vale
vale site/
```

**Tip:** Locally, you can use Vale to check specific content areas you are working on, such as `site/guides/`.

### Configuring Vale

- The linter is configured via a `vale.ini` file in the root of the repository. This file specifies which styles to use and which files or directories to skip.
- Community styles such as `Vale` and `Google` are installed automatically in the CI workflow.
- The workflow is set up to ignore files and folders starting with an underscore (`_`) and the `site/plugin` directory.

### FUTURE: Customizing rules

- To add or remove styles, edit the `BasedOnStyles` lines in your `vale.ini`.
- To skip additional files or folders, update the `Skips` setting in `vale.ini` or adjust the workflow globs.
