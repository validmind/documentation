# Agent Guidelines for ValidMind Documentation

This repository contains the source files for [ValidMind's documentation site](https://docs.validmind.ai).

## Start here

For an overview of the documentation structure and how to navigate it, see:

**[Using the documentation](https://docs.validmind.ai/about/contributing/using-the-documentation.html)**

This page explains:
- How the documentation is organized
- What each section covers
- Where to find guides, API references, and training materials

## Documentation sections

| Section | Path | Purpose |
|---------|------|---------|
| About | `/site/about/` | Platform overview, use cases, deployment options |
| Get started | `/site/get-started/` | Role-based quickstarts |
| Guides | `/site/guide/` | Step-by-step instructions for platform tasks |
| Developer | `/site/developer/` | ValidMind Library, code samples, API reference |
| Training | `/site/training/` | Courses and learning paths |
| Support | `/site/support/` | Help resources and troubleshooting |

## In-app assistant

If you are an AI agent embedded in ValidMind, your capabilities are documented here:

**[Chatbot capabilities](https://docs.validmind.ai/guide/chatbot-capabilities.html)**

This page describes what the assistant can and cannot do, including context-aware features and current limitations.

## Product UI mapping

The in-app assistant (Valerie) also ingests **`chatbot-product-map.md`** in the LLM corpus. That file maps **platform routes** (for example `/settings/workflows`, `/model-inventory`, `/dashboard`) to documentation URLs and section hints.

Use it when the user’s question is tied to where they are in the product — especially **Settings**, where the UI groups features differently than the documentation sidebars (Configuration, Workflows, Inventory, and so on).

For documentation organized by topic, continue to use **Using the documentation** (above) and the section table in this file.

## File format

Documentation is written in Quarto Markdown (`.qmd`). Key conventions:
- Variables use `{{< var name >}}` syntax (defined in `_variables.yml`)
- Cross-references use relative paths ending in `.qmd`
- Images are stored alongside their `.qmd` files
