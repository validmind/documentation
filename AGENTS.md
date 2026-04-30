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

## File format

Documentation is written in Quarto Markdown (`.qmd`). Key conventions:
- Variables use `{{< var name >}}` syntax (defined in `_variables.yml`)
- Cross-references use relative paths ending in `.qmd`
- Images are stored alongside their `.qmd` files
