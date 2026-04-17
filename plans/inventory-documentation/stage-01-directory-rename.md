# Stage 1 — Rename directory to `inventory` + patch references + aliases

**Parent index:** [README.md](README.md)

## Goal

[`site/guide/model-inventory`](../../site/guide/model-inventory) becomes [`site/guide/inventory`](../../site/guide/inventory) with every internal and cross-site path updated, without yet renaming individual `.qmd` files or rewriting body copy (except mechanical path strings).

## Mechanical edits

1. **Move/rename folder** `model-inventory` → `inventory` under [`site/guide/`](../../site/guide/).
2. **Replace path prefixes everywhere in the repo** (at minimum `site/`, plus [`README.md`](../../README.md) link table if it references the old segment):
   - `/guide/model-inventory/` → `/guide/inventory/`
   - `{{< include /guide/model-inventory/` → `{{< include /guide/inventory/`
   - Listing paths in [`site/guide/guides.qmd`](../../site/guide/guides.qmd): `model-inventory/...` → `inventory/...`
3. **Update the guide hub section** that still points at old listing paths and (for now) keep the visible heading "**Model inventory**" and anchor `#model-inventory` unless you prefer to bundle anchor renames with Stage 2 — default is **defer heading/anchor text to Stage 2** so Stage 1 only moves filesystem paths.
4. **Standalone `.qmd` files** (not prefixed with `_`) under the new folder: add a **new** YAML alias for the **previous directory URL**, one per page, e.g.  
   `aliases: - /guide/model-inventory/<same-basename>.html`  
   Merge with any existing `aliases` entries (several pages already have legacy flat paths like [`register-models-in-inventory.qmd`](../../site/guide/model-inventory/register-models-in-inventory.qmd) → `/guide/register-models-in-model-inventory.html`).

## Scope note

Partials named `_model-inventory-*.qmd` / `_view-model-activity-*.qmd` keep their filenames in Stage 1; includes already use absolute `/guide/...` paths and will pick up the new directory after search-replace.

## Checkpoint (merge-ready)

`quarto render` (or project-equivalent CI) succeeds; spot-check internal links to `/guide/inventory/...`; published URLs `/guide/model-inventory/<page>.html` resolve via new aliases; commit titled for Stage 1.

## Next

[Stage 2 — Filenames and terminology](stage-02-filenames-terminology.md)
