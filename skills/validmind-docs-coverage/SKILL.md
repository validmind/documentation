---
name: validmind-docs-coverage
description: Verify and implement documentation coverage for a ValidMind Shortcut story or engineering change by comparing final merged frontend/backend behavior with current documentation, classifying the gap, updating shared Quarto sources, validating every affected guide and training output, and preparing reviewer-ready pull requests and release-tracker updates. Use for single-story docs checks, `needs-docs` tickets, release documentation subtasks, or requests to create a documentation PR for a shipped change.
---

# ValidMind Documentation Coverage

Validate coverage from implementation evidence, then make the smallest complete documentation change when authorized.

## 1. Establish scope

1. Read the repository `AGENTS.md`.
2. Fetch the full Shortcut story, including comments, related stories, epic, linked branches, and pull requests.
3. Identify the final implementation PRs in every affected repository.
4. Inspect the PR bodies, changed files, relevant patches, tests, merge status, and later corrective PRs.

Treat the final implementation diff as authoritative for behavior when it differs from the Shortcut description. Verify merge and release state separately. Distinguish:

- Customer problem and expected behavior
- Implemented product behavior
- Explicit limitations and out-of-scope behavior
- Proposed architecture that did not ship

Do not treat an `internal` implementation label as evidence that a customer-visible capability needs no documentation.

## 2. Compare with current documentation

1. Fetch the latest `origin/main`.
2. Extract user-facing terminology, UI labels, routes, configuration, limits, errors, and edge cases from the implementation.
3. Search documentation with `rg`, starting in the most relevant section under `site/`.
4. When the change is tied to a product route, consult `chatbot-product-map.md` and its frontend snapshot.
5. Search for Quarto includes that consume any candidate shared source.

Classify the result:

| Status | Meaning |
|---|---|
| Covered | Current docs match the shipped behavior and important limitations. |
| Partial | The feature is mentioned, but new options or behavior are missing. |
| Outdated | Current instructions or stated behavior are now wrong. |
| Missing | No appropriate documentation coverage exists. |
| Source Gap | Implementation or release state is too uncertain to document safely. |

For a verification-only request, stop after reporting the classification, evidence, affected pages, and recommended scope. Do not edit files or external trackers until authorized.

## 3. Implement an approved update

1. Confirm the worktree and current branch before editing.
2. Start from current `origin/main` on a `codex/sc-<story-id>-<slug>` branch.
3. Update the smallest authoritative source.
4. Preserve Quarto variables, `.qmd` cross-references, conditional HTML/RevealJS variants, and existing terminology.
5. If editing an include, find every consumer:

```bash
rg -n "_source-name\\.qmd" site --glob '*.qmd'
```

Document operationally important limitations without exposing unnecessary backend mechanics.

## 4. Validate every consumer

Render every affected parent page and every output format. Quarto accepts one page reliably per invocation for this repository; do not pass multiple page paths to one `quarto render` command.

Use the bundled helper from the repository root:

```bash
skills/validmind-docs-coverage/scripts/render-pages.sh \
  guide/example/page.qmd \
  training/example/module.qmd
```

Then:

1. Run `git diff --check`.
2. Inspect rendered HTML under `site/_site/` for the new copy and anchors.
3. Report render warnings explicitly and determine whether they are introduced by the change.
4. Do not claim hosted preview success until the GitHub `validate` check passes.

## 5. Prepare the pull request

Follow `.github/pull_request_template.md` and the repository release-note policy.

Include:

- Shortcut story and final implementation PRs
- Before/after documentation behavior
- Exact local render commands or helper invocation
- Special-review assumptions and limitations
- A user-facing release-note entry
- The `documentation` label for external content changes

The hosted preview is created only after a draft PR becomes ready for review. Its base path is:

```text
https://docs-staging.validmind.ai/pr_previews/<branch>/
```

After `validate` succeeds:

1. Verify each relevant preview page returns successfully.
2. Add direct links to every changed rendered page, including useful section or RevealJS slide anchors.
3. Prefer direct reviewer destinations over the preview root.

## 6. Update release tracking

When asked to update a release documentation tracker:

1. Resolve the exact tracker and subtask for the engineering story.
2. Comment with the documentation PR link and the behavior covered.
3. Re-read GitHub state immediately before describing review, validation, or merge status.
4. Do not mark the tracker task complete unless the user explicitly asks you to do so.

## Evidence rules

- Do not infer deployment or release from a merged PR alone when release evidence is required.
- Do not describe a PR as approved, validated, or merging without checking current state.
- If private-repository connectors return `404`, use authenticated `gh` as the fallback and preserve the same evidence standard.
- Keep `Source Gap` explicit when implementation, configuration, or ownership cannot be verified.
