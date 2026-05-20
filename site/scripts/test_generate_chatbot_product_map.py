# Copyright © 2023-2026 ValidMind Inc. All rights reserved.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial

"""Unit tests for generate_chatbot_product_map.py"""

import unittest
from pathlib import Path

import generate_chatbot_product_map as gen


class TestGenerateChatbotProductMap(unittest.TestCase):
    def test_resolve_doc_path_alias(self) -> None:
        self.assertEqual(
            gen.resolve_doc_path(
                "/guide/model-workflows/setting-up-model-workflows.html"
            ),
            "/guide/workflows/setting-up-workflows.html",
        )

    def test_parse_doc_refs_from_help_link(self) -> None:
        text = (
            "helpLink={`${CONFIG.VALIDMIND_DOCS_URL}"
            "/guide/configuration/managing-users.html`}"
        )
        refs = gen.parse_doc_refs_from_text(text)
        self.assertEqual(len(refs), 1)
        self.assertEqual(refs[0].path, "/guide/configuration/managing-users.html")

    def test_html_path_to_qmd(self) -> None:
        site = Path(__file__).resolve().parents[1]
        qmd = gen.html_path_to_qmd(site, "/guide/workflows/setting-up-workflows.html")
        self.assertIsNotNone(qmd)
        self.assertEqual(qmd.name, "setting-up-workflows.qmd")

    def test_extract_headings(self) -> None:
        qmd = (
            Path(__file__).resolve().parents[1]
            / "guide/workflows/setting-up-workflows.qmd"
        )
        headings = gen.extract_headings(qmd)
        self.assertTrue(any("workflows" in h.lower() for h in headings))

    def test_is_user_facing_doc(self) -> None:
        self.assertTrue(gen.is_user_facing_doc("/guide/workflows/manage-workflow-tasks.html"))
        self.assertFalse(gen.is_user_facing_doc("/_source/release-notes/foo.html"))
        self.assertFalse(gen.is_user_facing_doc("/guide/workflows/_partial.html"))


if __name__ == "__main__":
    unittest.main()
