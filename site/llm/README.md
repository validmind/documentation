# LLM corpus (markdown for RAG)

This directory holds tooling that renders the documentation site to plain Markdown for ingestion into LanceDB and the in-app assistant (Valerie).

## Output

Rendered files land in `site/llm/_llm-output/` (gitignored). CI publishes that directory after `make render-llm`. Deployed environments only pick up new assistant context after the LanceDB artifact is rebuilt from a fresh render.

## Render locally

From `site/`:

```bash
make render-llm
```

This runs `llm/render.sh` (temporary minimal `_quarto.yml`, Quarto → GFM) and `llm/clean.sh` (Pandoc cleanup). Equivalent to the **Validate LLM markdown render** step in `.github/workflows/validate-docs-site.yaml`.

Excluded from the LLM render (among others): notebooks, internal pages, contributor style guide, and most of `about/contributing/`. **Included:** `about/using-the-documentation.qmd` (docs IA hub for agents).

Copied into `_llm-output/` after render:

| File | Source |
|------|--------|
| `AGENTS.md` | Repo root |
| `chatbot-product-map.md` | Generated (see below) |
| `about/using-the-documentation.md` | Quarto render |

See also [`AGENTS.md`](../../AGENTS.md) for how agents should use the corpus.

## Chatbot product map

Valerie needs routes in the product UI (especially **Settings**) mapped to documentation URLs. Human docs sidebars are organized by topic (Configuration, Workflows, Inventory); the product groups features differently.

| Artifact | Purpose |
|----------|---------|
| `chatbot-product-map-frontend-snapshot.json` | Vendored extract from `validmind/frontend` (Settings tree, sidebar nav, `helpLink` / docs URLs) |
| `chatbot-product-map.md` | Retrieval-oriented map: routes → primary/related docs + section headings from `.qmd` |

### Why a frontend snapshot?

CI does **not** check out `validmind/frontend` (private repo; cross-repo PAT scope). The snapshot is committed in this repo so pipelines can regenerate the map without frontend access. It may lag the live product until someone refreshes it locally.

### Maintenance

| Change | Command (from `site/`) |
|--------|-------------------------|
| Docs only (new `.qmd`, heading updates) | `make generate-chatbot-product-map` |
| Product routes or in-app help links | `make refresh-chatbot-product-map` (requires a sibling `../frontend` checkout) |

Commit both `chatbot-product-map.md` and `chatbot-product-map-frontend-snapshot.json` when the snapshot changes. CI fails if either file is out of date after regeneration.
For same-repo pull requests, the validate workflow auto-commits docs-only refreshes of `chatbot-product-map.md`. Fork pull requests and any snapshot drift still fail and require a local regenerate + commit.

Generator: `site/scripts/generate_chatbot_product_map.py`  
Tests: `python3 -m unittest discover -s site/scripts -p 'test_generate_chatbot_product_map.py' -v` (from repo root).
