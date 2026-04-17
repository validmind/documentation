# Stage 5 — Sidebar IA: `INVENTORY`, “Setting up the inventory”, new record-types guide

**Parent index:** [README.md](README.md)

## Goal

Reorganize the guide sidebar under a single **INVENTORY** label, introduce a parent page **Setting up the inventory** (accordion parent) that lists two setup tasks, add a new task page for primary record types, and move **Manage model inventory fields** out of the “Managing …” branch into **Setting up**.

## Depends on path naming

Implement on top of **Stage 1** so paths use `guide/inventory/...`. If Stage 5 ships in the **same release as Stage 2**, use the renamed fields page (e.g. `manage-inventory-fields.qmd`) in both the sidebar and the parent listing; if Stage 5 lands **between** Stage 1 and Stage 2, keep `manage-model-inventory-fields.qmd` in YAML and update again when Stage 2 renames the file.

## 1. New file: `site/guide/inventory/manage-inventory-record-types.qmd`

- **Title (suggested):** “Manage inventory record types” (sentence case per style guide).
- **Purpose:** Document admin configuration of **primary record types** per [sc-14816](https://app.shortcut.com/validmind/story/14816/documentation-primary-record-types-unified-ai-governance-inventory) (Settings, name/description/slug/tag, enabled state, field visibility per type, default Model type / backward compatibility, RBAC per type where product supports it).
- **Structure:** Follow task template from [`create-user-documentation` skill](../../.cursor/skills/create-user-documentation/SKILL.md): prerequisites → numbered steps → optional troubleshooting / what’s next with links to `manage-inventory-fields` and `working-with-inventory` as appropriate.
- **Frontmatter:** `date: last-modified`, copyright block consistent with sibling pages; optional `aliases: []` only if replacing a prior URL (none on first publish).

## 2. New file: `site/guide/inventory/setting-up-the-inventory.qmd`

- **Title (suggested):** “Setting up the inventory”.
- **Role:** Parent **hub** page (same pattern as [`managing-model-inventory.qmd`](../../site/guide/model-inventory/managing-model-inventory.qmd)): short intro, then a **Quarto `listing`** in YAML whose `contents` are exactly:
  - `manage-inventory-record-types.qmd`
  - `manage-model-inventory-fields.qmd` — after Stage 2, `manage-inventory-fields.qmd`
- **Body:** Minimal — an intro paragraph plus `::: {#listing-id}` placeholder matching the listing `id` (mirror the `managing-model-inventory` / `working-with-model-inventory` listing pattern).
- **Cross-links:** Add this hub to [`site/guide/guides.qmd`](../../site/guide/guides.qmd) only if product wants it on the main guide grid (optional; default **skip** unless you expand the inventory listing section).

## 3. Update `site/guide/_sidebar.yaml` (current block ~68–81)

Replace the **Model Inventory** label and nested structure with:

1. **Section label:** `- text: "INVENTORY"` (replacing `"Model Inventory"`).
2. **First child (new accordion parent):** `- text: "Setting up the inventory"` with `file: guide/inventory/setting-up-the-inventory.qmd` and `contents:`:
   - `guide/inventory/manage-inventory-record-types.qmd`
   - `guide/inventory/manage-model-inventory-fields.qmd` (or `manage-inventory-fields.qmd` post–Stage 2)
3. **Second block (unchanged intent):** `- text: "Working with the inventory"` with `file: guide/inventory/working-with-model-inventory.qmd` (or post–Stage 2 basename) and the **same** `contents` as today **except** do not duplicate the fields-management page here (today `edit-model-inventory-fields` stays; only **manage** fields moves to Setting up).
4. **`managing-model-inventory.qmd` branch:** `contents` should list **only** `configure-model-interdependencies` and `archive-delete-models` — **remove** `manage-model-inventory-fields` from this branch (it now lives under Setting up).
5. **Standalone:** `view-model-activity.qmd` remains a peer as today.
6. **Paths:** All `guide/model-inventory/` segments become `guide/inventory/` consistently with Stage 1.

### Sidebar sketch (logical tree)

```yaml
# Pseudocode — adjust basenames after Stage 2
- text: "INVENTORY"
- text: "Setting up the inventory"
  file: guide/inventory/setting-up-the-inventory.qmd
  contents:
    - guide/inventory/manage-inventory-record-types.qmd
    - guide/inventory/manage-model-inventory-fields.qmd
- text: "Working with the inventory"
  file: guide/inventory/working-with-model-inventory.qmd
  contents:
    - guide/inventory/register-models-in-inventory.qmd
    - ...
- file: guide/inventory/managing-model-inventory.qmd
  contents:
    - guide/inventory/configure-model-interdependencies.qmd
    - guide/inventory/archive-delete-models.qmd
- guide/inventory/view-model-activity.qmd
```

## 4. Sync hub page listings (not only the sidebar)

- **[`managing-model-inventory.qmd`](../../site/guide/model-inventory/managing-model-inventory.qmd)** (or `managing-inventory.qmd` after Stage 2): Remove `manage-model-inventory-fields.qmd` from the YAML `listing.contents` so the on-page grid matches the sidebar (only interdependencies + archive/delete remain). Optionally add a **What’s next** bullet pointing to `setting-up-the-inventory.qmd`.
- **`working-with-model-inventory.qmd`:** No change to its listing unless you want a cross-link in intro or What’s next to **Setting up the inventory** (optional editorial pass).

## Checkpoint

- Sidebar renders with **INVENTORY** → **Setting up** (2 children) → **Working with** → **Managing** (2 children) → **View activity**.
- `setting-up-the-inventory.qmd` listing grid matches sidebar children; **Managing** hub page grid no longer lists fields management.
- No duplicate sidebar entries for the fields-management page; internal links to `/guide/inventory/manage-...-fields` still resolve (aliases from Stage 1–2 preserved).

## Prev / next

- Previous: [Stage 4](stage-04-sitewide-rename-audit.md)
- Next: [Stage 6 — Feature gap review](stage-06-feature-gap-review.md)
