# Stage 2 — Rename inventory standalone files + terminology (model inventory → inventory; models → records)

**Parent index:** [README.md](README.md)

## Goal

Rename **standalone** pages under [`site/guide/inventory`](../../site/guide/inventory) whose **filenames** still encode `model` / `model-inventory` where that reflects old terminology; update **all** references (relative links, absolute `/guide/...` links, listings, footnotes, notebooks’ `docs.validmind.ai` URLs); add **aliases** for **previous filenames** (Stage 1 directory + prior basename); apply **copy-level renames** as specified.

## Proposed rename mapping (confirm before implementing)

| Current (after Stage 1) | Likely new basename | Notes |
|-------------------------|---------------------|--------|
| `working-with-model-inventory.qmd` | `working-with-inventory.qmd` | Hub page with nested `listing`; update `contents` entries |
| `managing-model-inventory.qmd` | `managing-inventory.qmd` | Same |
| `register-models-in-inventory.qmd` | `register-records-in-inventory.qmd` | Cross-links sitewide |
| `manage-model-inventory-fields.qmd` | `manage-inventory-fields.qmd` | Heavy cross-link surface |
| `edit-model-inventory-fields.qmd` | `edit-inventory-fields.qmd` | |
| `customize-model-inventory-layout.qmd` | `customize-inventory-layout.qmd` | Existing alias `/guide/customize-model-inventory-layout.html` — **retain** in frontmatter |
| `customize-model-overview-page.qmd` | `customize-record-overview-page.qmd` (or `customize-overview-page.qmd`) | Pick one naming scheme |
| `configure-model-interdependencies.qmd` | `configure-record-interdependencies.qmd` | |
| `view-model-activity.qmd` | `view-record-activity.qmd` | |
| `archive-delete-models.qmd` | `archive-delete-records.qmd` | |

## Terminology rules (Stage 2)

- **"Model inventory"** (and title-case variants) → **"Inventory"** where it names the product area (guide titles, [`guides.qmd`](../../site/guide/guides.qmd) section heading, [`_quarto.yml`](../../site/_quarto.yml) nav label, listing ids like `guides-model-inventory` → e.g. `guides-inventory`).
- **"Model(s)" → "record(s)"** in doc-authored phrases such as *registering models*, *models in your inventory*, *select a model* — per your instruction for non–"model inventory" concepts. **Exception handling:** Leave **verbatim UI labels** (e.g. button text **Register Model**) until confirmed against the live product; footnotes can say "labeled Register Model in the UI" if needed.
- **Anchor IDs:** If headings change (e.g. `## Search, filter, and sort models`), Quarto will generate new fragment IDs — **every** link ending in `#search-filter-and-sort-models` must be updated in the same stage, or keep the old heading text strictly for anchor stability until Stage 3. Recommend: **batch-update anchors with filenames** in Stage 2 to avoid broken deep links.

## Partial includes (optional same stage or fast follow)

Rename `_model-inventory-fields.qmd` → `_inventory-fields.qmd`, `_view-model-activity-*.qmd` → `_view-record-activity-*.qmd`, etc., and update `{{< include >}}` targets. If deferred, leave includes as-is temporarily.

## Sweep areas

Same grep as Stage 1 plus [`site/notebooks/**/*.ipynb`](../../site/notebooks/) (hard-coded `docs.validmind.ai/guide/...` strings), [`README.md`](../../README.md), and workflow partials under [`site/guide/workflows/`](../../site/guide/workflows/).

## Checkpoint

Link checker / broken-anchor check; `guides.qmd` grid lists correct files; nav anchor updated if section id changes (e.g. `#model-inventory` → `#inventory`); commit for Stage 2.

## Prev / next

- Previous: [Stage 1](stage-01-directory-rename.md)
- Next: [Stage 3 — Content refresh](stage-03-content-refresh.md)
