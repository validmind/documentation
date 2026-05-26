#!/usr/bin/env python3
"""Unit tests for lighthouse_urls.py"""

import tempfile
import unittest
from pathlib import Path
from unittest import mock

from lighthouse_urls import (
    ROOT_PAGES,
    _matches_global_pattern,
    asset_path_to_html,
    changed_file_to_html,
    qmd_path_to_html,
    urls_from_changed_files,
)


class TestQmdMapping(unittest.TestCase):
    def test_simple_qmd(self):
        self.assertEqual(
            qmd_path_to_html("site/guide/foo.qmd"),
            "guide/foo.html",
        )

    def test_index_qmd(self):
        self.assertEqual(
            qmd_path_to_html("site/guide/foo/index.qmd"),
            "guide/foo/index.html",
        )

    def test_root_index(self):
        self.assertEqual(
            qmd_path_to_html("site/index.qmd"),
            "index.html",
        )


class TestGlobalPatterns(unittest.TestCase):
    def test_quarto_yml(self):
        self.assertTrue(_matches_global_pattern("site/_quarto.yml"))

    def test_theme_scss(self):
        self.assertTrue(_matches_global_pattern("site/theme.scss"))

    def test_extensions(self):
        self.assertTrue(_matches_global_pattern("site/_extensions/foo/bar.lua"))

    def test_page_qmd_not_global(self):
        self.assertFalse(_matches_global_pattern("site/guide/foo.qmd"))


class TestChangedFileToHtml(unittest.TestCase):
    def test_global_returns_root_pages(self):
        result = changed_file_to_html("site/_quarto.yml")
        self.assertEqual(result, ROOT_PAGES)

    def test_asset_with_index_qmd(self):
        import os

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "site" / "guide" / "foo").mkdir(parents=True)
            (root / "site" / "guide" / "foo" / "index.qmd").write_text("---\n")
            (root / "site" / "guide" / "foo" / "pic.png").write_bytes(b"")
            prev = os.getcwd()
            try:
                os.chdir(tmp)
                html = asset_path_to_html("site/guide/foo/pic.png")
            finally:
                os.chdir(prev)
            self.assertEqual(html, "guide/foo/index.html")


class TestUrlsFromChangedFiles(unittest.TestCase):
    def test_empty_diff(self):
        with mock.patch("lighthouse_urls.git_changed_files", return_value=[]):
            paths, fallback = urls_from_changed_files("main")
            self.assertEqual(paths, [])
            self.assertFalse(fallback)

    def test_single_qmd(self):
        with mock.patch(
            "lighthouse_urls.git_changed_files",
            return_value=["site/developer/how-to/test-sandbox.qmd"],
        ):
            paths, fallback = urls_from_changed_files("main")
            self.assertEqual(paths, ["developer/how-to/test-sandbox.html"])
            self.assertFalse(fallback)

    def test_global_fallback(self):
        with mock.patch(
            "lighthouse_urls.git_changed_files",
            return_value=["site/_variables.yml", "site/guide/foo.qmd"],
        ):
            paths, fallback = urls_from_changed_files("main")
            self.assertEqual(set(paths), set(ROOT_PAGES))
            self.assertTrue(fallback)


if __name__ == "__main__":
    unittest.main()
