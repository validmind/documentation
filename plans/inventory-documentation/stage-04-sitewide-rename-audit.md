# Stage 4 — Site-wide discovery and *draft plans* (no full execution required in this stage)

**Parent index:** [README.md](README.md)

## Goal

Identify **additional** `site/` content that is still **model-centric** in filenames, paths, or titles; produce a **written backlog** of proposed renames (file → file), alias strategy, reference update lists, and content notes — **example:** [`site/guide/model-validation/managing-model-validation.qmd`](../../site/guide/model-validation/managing-model-validation.qmd) → *Managing validation* / `managing-validation.qmd` after product terminology is fixed.

## Suggested discovery method

1. **Path/filename heuristics:** Grep `site/guide/model-`, titles starting with "Managing model", "Working with model", etc.
2. **Hub pages:** [`site/guide/guides.qmd`](../../site/guide/guides.qmd) sections "Model documentation", "Model validation" — evaluate whether sections should become "Documentation" / "Validation" with inclusive intros (may parallel inventory work).
3. **Glossary / key concepts:** e.g. [`site/about/glossary/_validmind-features.qmd`](../../site/about/glossary/_validmind-features.qmd) (`platform-model-inventory` id) — plan id/anchor preservation or redirects.
4. **Training / get-started:** Paths under [`site/training/`](../../site/training/), [`site/get-started/`](../../site/get-started/) that assume "model" as the only governed object.
5. **Output artifact:** A short table per candidate area: **current path**, **proposed path**, **aliases**, **estimated reference count**, **content strategy** (title + intro changes only vs full pass).

## Checkpoint

Deliverable is the **draft plan document** (issue/Notion/PR comment acceptable); implementation can be split into future stories after review.

## Prev / next

- Previous: [Stage 3](stage-03-content-refresh.md)
- Next: [Stage 5 — Sidebar and setting up](stage-05-sidebar-setting-up.md)
