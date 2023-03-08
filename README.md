# Documentation framework

A place for our user-facing documentation and related infrastructure.

## Prerequisites

To work on the docs locally, you need:

- [Quarto CLI](https://quarto.org/docs/get-started/), plus the Quarto extension for your IDE, such as [VS Code](https://marketplace.visualstudio.com/items?itemName=quarto.quarto).
- The https://github.com/validmind/validmind-python repo in parallel with this one so that we can fetch the source from there.

## Preview the docs site locally

```bash
cd site
make get-source
quarto preview
```
