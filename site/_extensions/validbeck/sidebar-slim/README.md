# Sidebar slim

Optional **site sidebar** control: on large viewports, readers can collapse the Quarto **docked** sidebar to a narrow vertical strip and expand it again. State is kept for the browser tab (`sessionStorage`).

## Enable for a section (directory)

**1. Register the filter once** in the project `format` section (e.g. `site/_quarto.yml`):

```yaml
filters:
  - tachyons
  - preview
  - validbeck/sidebar-slim
```

**2. Opt in** with directory metadata, e.g. `some/section/_metadata.yml`:

```yaml
sidebar-slim: true
```

Any `.qmd` under that directory inherits this unless overridden in the file.

## Per-page override

In a single document’s YAML:

```yaml
sidebar-slim: false
```

## Alternative: filter only in a directory

If you do not want a global filter entry, add both lines under the same `_metadata.yml`:

```yaml
filters:
  - validbeck/sidebar-slim
sidebar-slim: true
```

(Confirm how your Quarto version merges `filters` lists with the project; you may need to repeat other project filters.)

## Notes

- Only runs for **HTML** (`html:js`) output when `sidebar-slim` is truthy.
- Toolbar appears at **≥992px** width; below that, Quarto’s own responsive sidebar behavior applies and this extension removes its UI.
- When collapsed, **main content is widened** by adjusting Quarto’s **CSS grid** placement (docked and floating layouts at the `lg` breakpoint): the sidebar span is shortened and `.content` / `.page-navigation` / `.column-body` start at `page-start-inset` so they use the space the full sidebar used. If a Quarto theme changes grid line names, these rules may need updating.
- Does not replace Quarto’s built-in **reader mode** (`website: reader-mode`); you can use either or both.
