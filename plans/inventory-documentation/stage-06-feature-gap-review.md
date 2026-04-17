# Stage 6 — Feature gap review: additional changes suggested by primary record types

**Parent index:** [README.md](README.md)

## Goal

After inventory-focused work (Stages 1–5), systematically identify **net-new** or **expanded** documentation that the **product functionality** in [sc-14816](https://app.shortcut.com/validmind/story/14816/documentation-primary-record-types-unified-ai-governance-inventory) implies—beyond path renames (Stage 4) and the single new task page (Stage 5). Treat this as a **prioritized backlog** (Shortcut stories optional).

## How Stage 6 differs from Stage 4

Stage 4 emphasizes **filenames, paths, aliases, and “model → record” wording** across the site. Stage 6 emphasizes **behavioral coverage**: permissions, workflows, org admin surfaces, developer APIs, and cross-cutting concepts so users understand **primary record types vs. other objects** (e.g. artifacts, documents) end-to-end.

## Suggested areas (review each; implement only where product ships the behavior)

1. **Concepts & glossary**
   - **Primary record types vs. secondary records / artifacts:** Add or extend a short concept page (or glossary entries) so readers know what “record type” means vs. model documentation templates, validation artifacts, etc. Touchpoints: [`site/about/glossary/`](../../site/about/glossary/), key concepts includes if present.
   - **Unified AI governance framing:** Overview pages such as [`site/about/overview-model-risk-management.qmd`](../../site/about/overview-model-risk-management.qmd) may need a paragraph on multi-type inventory—not only “models.”

2. **Organization & Settings (non-inventory guides)**
   - If **primary record types** are configured outside the inventory-specific guides (e.g. under **Manage your organization** / **Set up your organization**), add **cross-links** from [`site/guide/configuration/`](../../site/guide/configuration/) into **Setting up the inventory** / **Manage inventory record types**, or a short subsection where admins expect it.
   - **Field visibility per record type:** Ensure [`manage-inventory-fields`](../../site/guide/model-inventory/manage-model-inventory-fields.qmd) (post-rename) and the record-types page don’t contradict each other; split or cross-link responsibilities clearly.

3. **Permissions & access control**
   - Document **type-scoped RBAC** (read/create/update/delete per record type) on [`site/guide/configuration/manage-permissions.qmd`](../../site/guide/configuration/manage-permissions.qmd) or a dedicated subsection—aligned with whatever the product UI exposes.
   - Review **roles** and **stakeholder types** docs for “model-only” assumptions (e.g. [`manage-model-stakeholder-types`](../../site/guide/configuration/manage-model-stakeholder-types.qmd)) if stakeholders attach to non-model record types.

4. **Workflows**
   - [`site/guide/workflows/`](../../site/guide/workflows/) partials (e.g. `_add-new-workflows.qmd`, triggers like **Inventory Model**, **On Model Registration**, **model field to monitor**) may need **record-neutral** explanations or notes when workflows apply per record type.
   - Conditional requirements referencing **model inventory fields** should be reconciled with **inventory fields** / **record-type** wording after Stage 2.

5. **Integrations & MCP**
   - [`site/guide/integrations/managing-integrations.qmd`](../../site/guide/integrations/managing-integrations.qmd) (diagrams and copy mentioning “Model inventory,” MCP “manage your model inventory”) should describe **querying/managing inventory records** if the integration behavior is type-aware.

6. **Developer & notebooks**
   - [`site/developer/`](../../site/developer/), library init pages, and [`site/notebooks/`](../../site/notebooks/) often assume **model** registration and **model** objects—add guidance when the library supports **record types** or multiple entity types (even if only “coming soon” or version-matrix).
   - Update embedded **docs.validmind.ai** links after Stages 1–2 (already partially in earlier stages); Stage 6 verifies **semantic** alignment (examples use “record” where API does).

7. **Downstream product areas (prerequisites & flows)**
   - **Model documentation, validation, attestation, monitoring, reporting:** Sweep prerequisite lines (“model registered in the inventory,” “select a model”) for **record**-inclusive phrasing and, where the product allows non-model types, **type-specific** notes (can parallel Stage 3–4 but Stage 6 owns **consistency** with record-type rollout).
   - **Templates / document types:** If document types bind to **record types**, document that in [`site/guide/templates/`](../../site/guide/templates/) as needed.

8. **Training & get-started**
   - [`site/training/`](../../site/training/), [`site/get-started/`](../../site/get-started/), and [`site/training/program/training-faq.qmd`](../../site/training/program/training-faq.qmd) (“Model inventory” FAQ section)—update curricula and slides when **terminology** and **first-run** paths change; coordinate with app URL `/model-inventory` separately (product).

9. **Compliance & use-case narratives**
   - Pages such as [`site/about/use-cases/eu-ai-act.qmd`](../../site/about/use-cases/eu-ai-act.qmd) that cite inventory capabilities may need **inventory of AI systems / use cases**, not models only.

10. **AI/agent discoverability**
    - Regenerate or extend [`llms.txt` / `agents.txt`](../../.cursor/skills/content-architecture/SKILL.md) after major IA changes so agents surface **inventory** and **record types** consistently.

11. **Internal assets**
    - [`internal/templates/videos/index.html`](../../internal/templates/videos/index.html) (`id="model-inventory"` slide section)—update if recordings or deck structure should reflect new terminology.

## Checkpoint

- A **written backlog** (table): area → suggested change → dependency on product behavior → priority (P0/P1/P2).
- No requirement to implement every row in one release; Stage 6 is **scoping and prioritization**.

## Prev

- Previous: [Stage 5](stage-05-sidebar-setting-up.md)
