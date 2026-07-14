# Agent Guidelines for ValidMind Documentation

This repository contains the source files for [ValidMind's documentation site](https://docs.validmind.ai).

## Start here

For an overview of the documentation structure and how to navigate it, see:

**[Using the documentation](https://docs.validmind.ai/about/using-the-documentation.html)**

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

Route and help-link data from the product UI is vendored as **`site/llm/chatbot-product-map-frontend-snapshot.json`**. Regenerate it with `make -C site refresh-chatbot-product-map` when frontend routes or `helpLink` values change (requires a local `validmind/frontend` checkout).

Use the map when the user’s question is tied to where they are in the product — especially **Settings**, where the UI groups features differently than the documentation sidebars (Configuration, Workflows, Inventory, and so on).

For documentation organized by topic, continue to use **Using the documentation** (above) and the section table in this file.

## File format

Documentation is written in Quarto Markdown (`.qmd`). Key conventions:
- Variables use `{{< var name >}}` syntax (defined in `_variables.yml`)
- Cross-references use relative paths ending in `.qmd`
- Images are stored alongside their `.qmd` files

## Pull requests and release notes

Documentation pull requests must follow the repository's release-note policy:

- Internal workflow, tooling, or maintenance changes use the `internal` label.
- External changes use an appropriate release-note label and include content in the pull request's release-notes section.

The required `validate` check is the pull-request feedback gate. For ordinary content changes, it renders only safely targetable changed pages and assets and builds the preview on top of the validated staging site. It falls back to a complete preview render for changes that can have global or ambiguous effects, including Quarto configuration or metadata, generated content, deletions, and renames.

## Documentation delivery

Documentation moves through `main` → `staging` → `prod`:

1. Pull requests into `main` receive preview validation and normal review.
2. After merge, the staging workflow renders the complete staging site and the prospective production site in parallel.
3. The prospective production build runs the complete production-profile validation and uploads an immutable artifact keyed to the exact Git tree that a `staging` → `prod` merge will create.
4. The production workflow deploys only that exact-tree artifact from a successful staging workflow run. If the artifact is missing, expired, or came from another workflow, production deployment must fail before loading AWS credentials or modifying production.

The merge-queue `validate` bridge does not render the site again. It records that the pull-request revision passed preview validation; the complete production safety boundary is the post-merge staging artifact.

## CI invariants

When changing documentation workflows, preserve these constraints:

- Do not add a fallback build to the production deployment workflow. Missing validated artifacts must fail closed.
- Keep full Git history available when preparing the prospective production tree. A shallow checkout cannot establish the shared `staging`/`prod` history and causes Git to reject the merge as unrelated histories.
- Keep targeted preview runs cancelable so a newer commit supersedes obsolete work.
- Treat preview rendering and production validation as different responsibilities: previews provide fast author feedback; only the complete post-merge production-profile build can authorize a production artifact.
