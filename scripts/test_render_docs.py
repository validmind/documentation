# Copyright © 2026 ValidMind Inc. All rights reserved.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial
"""Safety checks for complete parallel documentation renders."""

import json
from pathlib import Path
import shutil
import sys
import subprocess
import tempfile
import unittest

from render_docs import dependent_listings, listing_targets, merge_outputs, partition


class RenderTests(unittest.TestCase):
    def test_partition_covers_each_input_once(self):
        inputs = ["index.qmd", "a/one.qmd", "a/two.qmd", "b/deep/one.qmd", "b/two.md"]
        for jobs in (1, 2, 8):
            targets = sum(partition(inputs, jobs), [])
            for source in inputs:
                self.assertEqual(
                    sum(source == t or source.startswith(t + "/") for t in targets), 1
                )

    def test_listing_batches_cover_every_listing_once(self):
        inputs = ["index.qmd", "guide/list.qmd", "guide/page.qmd", "large/list.qmd"]
        inputs += [f"large/{i}.qmd" for i in range(200)]
        listings = ["index.qmd", "guide/list.qmd", "large/list.qmd"]
        targets = sum(listing_targets(inputs, listings, 2), [])
        self.assertIn("guide", targets)
        self.assertNotIn("large", targets)
        for page in listings:
            self.assertEqual(
                sum(page == t or page.startswith(t + "/") for t in targets), 1
            )

    def test_merge_preserves_all_search_and_listing_entries(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            outputs = [root / "a", root / "b"]
            destination = root / "merged"
            destination.mkdir()
            for i, output in enumerate(outputs):
                output.mkdir()
                (output / "shared.css").write_text("body {}")
                (output / "search.json").write_text(
                    json.dumps([{"objectID": f"{i}.html", "text": str(i)}])
                )
                (output / "listings.json").write_text(
                    json.dumps([{"listing": f"{i}.html", "items": []}])
                )
            merge_outputs(outputs, destination)
            self.assertEqual(
                len(json.loads((destination / "search.json").read_text())), 2
            )
            self.assertEqual(
                len(json.loads((destination / "listings.json").read_text())), 2
            )
            (outputs[1] / "shared.css").write_text("body {color:red}")
            with self.assertRaisesRegex(RuntimeError, "Conflicting worker output"):
                merge_outputs(outputs, destination)

    def test_rejects_conflicting_index_entries(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            outputs = [root / "a", root / "b"]
            destination = root / "merged"
            destination.mkdir()
            for i, output in enumerate(outputs):
                output.mkdir()
                (output / "search.json").write_text(
                    json.dumps([{"objectID": "same.html", "text": str(i)}])
                )
            with self.assertRaisesRegex(ValueError, "Conflicting search.json"):
                merge_outputs(outputs, destination)

    def test_dependent_listing_content_requires_native_render(self):
        with tempfile.TemporaryDirectory() as temp:
            site = Path(temp).resolve()
            output = site / "_site"
            output.mkdir()
            (site / "cards.qmd").write_text("Cards")
            metadata = {
                "index.qmd": {
                    "listing": {"contents": "cards.qmd", "fields": ["description"]}
                },
                "cards.qmd": {"listing": {"contents": "posts/*.qmd"}},
            }
            (output / "cards.html").write_text(
                "<main><div>Listing placeholder</div></main>"
            )
            self.assertTrue(dependent_listings(site, output, metadata, list(metadata)))
            (output / "cards.html").write_text(
                "<main><p>Independent introduction.</p></main>"
            )
            self.assertFalse(dependent_listings(site, output, metadata, list(metadata)))
            (output / "cards.html").write_text("<main></main>")
            # A broad contents glob also matches the listing's own source;
            # Quarto excludes that page from its own listing.
            metadata["cards.qmd"]["listing"]["contents"] = "*.qmd"
            self.assertFalse(
                dependent_listings(
                    site, output, {"cards.qmd": metadata["cards.qmd"]}, ["cards.qmd"]
                )
            )
            metadata["cards.qmd"]["description"] = "Explicit summary"
            self.assertFalse(dependent_listings(site, output, metadata, list(metadata)))

    @unittest.skipUnless(shutil.which("quarto"), "Quarto required for integration test")
    def test_real_quarto_matches_serial_links_listings_aliases_and_slides(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            site = root / "site"
            site.mkdir()
            (site / "_quarto.yml").write_text(
                "project:\n  type: website\nwebsite:\n  title: Fixture\n  sidebar:\n    contents: auto\nformat: html\n"
            )
            (site / "index.qmd").write_text(
                '---\ntitle: Home\nlisting:\n  contents: "posts/*.qmd"\n---\n[Guide](guide/page.qmd)\n'
            )
            # Two listing pages, with one reading the other's rendered summary.
            (site / "index.qmd").write_text(
                '---\ntitle: Home\nlisting:\n  contents: ["posts/*.qmd", "guide/cards.qmd"]\n---\n[Guide](guide/page.qmd)\n'
            )
            (site / "_quarto-production.yml").write_text(
                "website:\n  page-footer: Production fixture\n"
            )
            (site / "_include.qmd").write_text("Shared included text.\n")
            for directory in ("posts", "guide", "training", "nested"):
                (site / directory).mkdir()
            (site / "guide/cards.qmd").write_text(
                '---\ntitle: Cards\nlisting:\n  contents: "../posts/*.qmd"\n---\nCard introduction.\n'
            )
            for i in range(4):
                (site / f"posts/{i}.qmd").write_text(
                    f"---\ntitle: Post {i}\n---\nDescription {i}.\n\n[Guide](/guide/page.qmd)\n"
                )
            (site / "guide/page.qmd").write_text(
                '---\ntitle: Guide\naliases: ["/old-guide.html"]\n---\n{{< include ../_include.qmd >}}\n'
            )
            (site / "training/slides.qmd").write_text(
                "---\ntitle: Slides\naliases: [old-slides.html]\nformat:\n  revealjs: default\n  html:\n    output-file: _slides.html\n---\n## First\n\n{{< include ../_include.qmd >}}\n"
            )
            (site / "nested/_quarto.yml").write_text(
                "project:\n  type: default\nformat: gfm\n"
            )
            (site / "nested/page.qmd").write_text(
                "---\ntitle: Nested\n---\n{{< include /_include.qmd >}}\n"
            )
            subprocess.run(
                ["quarto", "render", str(site), "--profile", "production"],
                check=True,
                capture_output=True,
            )
            serial = root / "serial"
            shutil.move(site / "_site", serial)
            result = subprocess.run(
                [
                    sys.executable,
                    str(Path(__file__).with_name("render_docs.py")),
                    "--site",
                    str(site),
                    "--jobs",
                    "2",
                    "--profile",
                    "production",
                ],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            parallel = site / "_site"
            files = {p.relative_to(serial) for p in serial.rglob("*") if p.is_file()}
            self.assertEqual(
                files,
                {p.relative_to(parallel) for p in parallel.rglob("*") if p.is_file()},
            )
            for path in files:
                if path.name in ("search.json", "listings.json"):
                    self.assertEqual(
                        sorted(json.loads((serial / path).read_text()), key=str),
                        sorted(json.loads((parallel / path).read_text()), key=str),
                        str(path),
                    )
                else:
                    self.assertEqual(
                        (serial / path).read_bytes(),
                        (parallel / path).read_bytes(),
                        str(path),
                    )

    @unittest.skipUnless(shutil.which("quarto"), "Quarto required for integration test")
    def test_gfm_and_failed_render_preserve_existing_output(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            site = root / "site"
            site.mkdir()
            (site / "_quarto.yml").write_text(
                "project:\n  type: default\n  output-dir: _markdown\nformat: gfm\n"
            )
            for name in ("a", "b"):
                (site / name).mkdir()
                (site / name / "page.qmd").write_text(
                    f"---\ntitle: {name}\n---\nText **{name}**.\n"
                )
            subprocess.run(
                ["quarto", "render", str(site), "--to", "gfm"],
                check=True,
                capture_output=True,
            )
            expected = {
                p.relative_to(site / "_markdown"): p.read_bytes()
                for p in (site / "_markdown").rglob("*")
                if p.is_file()
            }
            (site / "_markdown/stale.md").write_text("obsolete")
            command = [
                sys.executable,
                str(Path(__file__).with_name("render_docs.py")),
                "--site",
                str(site),
                "--to",
                "gfm",
                "--jobs",
                "2",
            ]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            actual = {
                p.relative_to(site / "_markdown"): p.read_bytes()
                for p in (site / "_markdown").rglob("*")
                if p.is_file()
            }
            self.assertEqual(actual, expected)
            # Valid YAML with an invalid filter fails during rendering, after
            # inspection and worker creation. The previous site must survive.
            (site / "b/page.qmd").write_text(
                "---\ntitle: Broken\nfilters: [missing-filter.lua]\n---\nBad.\n"
            )
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            actual = {
                p.relative_to(site / "_markdown"): p.read_bytes()
                for p in (site / "_markdown").rglob("*")
                if p.is_file()
            }
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
