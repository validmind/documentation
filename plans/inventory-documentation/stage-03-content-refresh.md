# Stage 3 — Content refresh on renamed inventory pages (models → inclusive “records” / primary record types)

**Parent index:** [README.md](README.md)

## Goal

Update **bodies** of the pages touched in Stages 1–2 so they match [sc-14816](https://app.shortcut.com/validmind/story/14816/documentation-primary-record-types-unified-ai-governance-inventory) / epic **13988**: primary record types, default Model type, and inventory as unified AI governance (not model-only).

## Content directions (page-level, not exhaustive)

- **Intro/overview** (`working-with-inventory`, `managing-inventory`): State that the inventory holds **records** of configurable **primary record types** (Models, AI Systems, Use Cases, etc.), with **Model** as the default backward-compatible type where applicable.
- **Registration** (`register-records-in-inventory`): Describe creating **records** and choosing type where the product supports it; keep UI steps accurate to current release.
- **Fields / layout / overview / activity** guides: Prefer **record**-neutral language; where behavior is type-specific, say so (e.g. “for each record type” / “in Settings”).
- **Prerequisites** lines that read “models registered in the inventory” → “records” or “at least one record” as appropriate.
- **Screenshots / alt text:** Update captions if UI strings changed (coordinate with product screenshots if needed).

## Checkpoint

Editorial review against story scope; CI green; optional Vale pass per [`content-qa` skill](../../.cursor/skills/content-qa/SKILL.md); commit for Stage 3.

## Prev / next

- Previous: [Stage 2](stage-02-filenames-terminology.md)
- Next: [Stage 4 — Sitewide rename audit](stage-04-sitewide-rename-audit.md)
