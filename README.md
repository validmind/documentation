# ValidMind

![](site/guide/ValidMind-logo-color.svg)

ValidMind helps model developers and model validators streamline communication and automate the model documentation process.

This is the home for the user-facing documentation and related infrastructure for ValidMind. If you want to make updates to our external docs site, you're in the right place.

## Contributing to the documentation

We believe in the power of collaboration and welcome contributions from the community. If you've noticed an issue or have ideas for improvement, please create a pull request or submit an issue. A member of ValidMind's documentation team will review your suggestions and support you in contributing to the docs. 

- Follow the [Quickstart](https://docs.validmind.ai/guide/quickstart.html) for a 20 minute introduction to the Developer Framework and ValidMind Platform.

- Read the [Developer Framework docs](https://docs.validmind.ai/guide/developer-framework.html) for more information about ValidMind's open source tests and Jupyter notebooks.

- Join the [Community Slack](site/guide/join-community.qmd) to ask questions, get support, and connect with Model Risk Management (MRM) practioners.

## Prerequisites

We use [Quarto](https://quarto.org) to develop our docs site, an open-source docs framework based on Pandoc that supports multiple input formats such as Quarto Markdown, Jupyter notebooks, and Markdown.

You need:

- [Quarto CLI](https://quarto.org/docs/get-started/)
- The Quarto extension for your IDE, such as [VS Code](https://marketplace.visualstudio.com/items?itemName=quarto.quarto)

## How to contribute

Our core docs are sourced in Quarto Markdown under [site/guide/](https://github.com/validmind/documentation/tree/main/site/guide). If you create new documentation, make sure to add it to the [_quarto.yml](https://github.com/validmind/documentation/blob/main/site/_quarto.yml) file.

If you are creating a pull request, test your changes by rendering or previewing the site. Note that if this is your first time contributing, you will be asked to sign a contributor license agreement (CLA).

## Preview the docs site

```bash
cd site
quarto preview
```

## Render the docs site

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