# Sidebar slim

When `sidebar-slim: true` is set, users can collapse the docked side navigation to a narrow vertical strip to reduce visual clutter. State is kept for the browser tab (`sessionStorage`).

## Usage

### Setup

Enable the filter globally in the project `format` section (`site/_quarto.yml`) so that its functionality can be called:

```yaml
filters:
  - tachyons
  - preview
  - validbeck/sidebar-slim
```

This is the currently applied functionality.

### Enabling

#### Enable for a single page

In the `.qmd` YAML frontmatter set:

```yaml
sidebar-slim: true
```

#### Enable for an entire section (directory)

In that directory's `_metadata.yml` set:

```yaml
sidebar-slim: true
```

Any `.qmd` under that directory inherits this unless overridden per file.

This is the current functionality that applies to `site/guide/`.

#### Enable for the entire project

In the project configuration (`site/_quarto.yml`), set default metadata so every page inherits it:

```yaml
metadata:
  sidebar-slim: true
```

Per-directory `_metadata.yml` or a single document’s YAML can still override this (for example, `sidebar-slim: false` on one page).

### Configuration

#### Default to collapsed (narrow) sidebar

Use **`sidebar-narrow: true`** so the first visit in a tab starts **collapsed** (until the user toggles). Preference is stored in `sessionStorage` (`1` = collapsed, `0` = expanded).

Example:

```yaml
sidebar-narrow: true
```

This is the functionality currently set on `site/guide/guides.qmd`.

## Notes

- Extension only applies to **HTML** (`html:js`) output.
- Toolbar appears at **≥992px** width; below that, Quarto’s own responsive sidebar behavior applies and this extension removes its UI.
- When collapsed, the **main column width stays the same**; only the sidebar UI narrows inside its layout area (the grid tracks for the article are unchanged).
- Does not replace Quarto’s built-in **reader mode** (`website: reader-mode`); you can use either or both.
