# Copyright © 2023-2026 ValidMind Inc. All rights reserved.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial

import unittest

from select_docs_preview_targets import parse_changed_files, select


class SelectDocsPreviewTargetsTest(unittest.TestCase):
    def test_selects_changed_pages_and_assets(self):
        result = select(
            [
                ("M", ("site/guide/example.qmd",)),
                ("A", ("site/guide/images/example.png",)),
            ]
        )

        self.assertTrue(result.is_targeted)
        self.assertEqual(result.targets, ("guide/example.qmd",))
        self.assertEqual(result.assets, ("guide/images/example.png",))

    def test_global_quarto_change_requires_full_render(self):
        result = select([("M", ("site/_quarto.yml",))])

        self.assertFalse(result.is_targeted)

    def test_shared_metadata_requires_full_render(self):
        result = select([("M", ("site/releases/_metadata.yml",))])

        self.assertFalse(result.is_targeted)

    def test_deleted_page_requires_full_render(self):
        result = select([("D", ("site/guide/old.qmd",))])

        self.assertFalse(result.is_targeted)

    def test_non_site_change_requires_full_render(self):
        result = select([("M", (".github/workflows/example.yaml",))])

        self.assertFalse(result.is_targeted)

    def test_asset_only_change_requires_full_render(self):
        result = select([("M", ("site/guide/images/example.png",))])

        self.assertFalse(result.is_targeted)

    def test_generated_corpus_change_requires_full_render(self):
        result = select([("M", ("site/llm/AGENTS.md",))])

        self.assertFalse(result.is_targeted)

    def test_parses_renames_for_safe_fallback(self):
        changes = parse_changed_files(
            "renamed\tsite/guide/new.qmd\tsite/guide/old.qmd\n"
        )

        self.assertEqual(
            changes,
            [("R", ("site/guide/new.qmd", "site/guide/old.qmd"))],
        )
        self.assertFalse(select(changes).is_targeted)


if __name__ == "__main__":
    unittest.main()
