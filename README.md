# Documentation framework

A home for our user-facing documentation and related infrastructure. If you need to make updates to our docs site, you're in the right place.

## Prerequisites

To work on the docs locally, you need:

- [Quarto CLI](https://quarto.org/docs/get-started/), plus the Quarto extension for your IDE, such as [VS Code](https://marketplace.visualstudio.com/items?itemName=quarto.quarto).
- The https://github.com/validmind/validmind-python repo in parallel with this one so that we can fetch some source content from there.

## Preview the docs site locally

```bash
cd site
make get-source
quarto preview
```
