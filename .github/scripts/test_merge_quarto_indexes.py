# Copyright © 2023-2026 ValidMind Inc. All rights reserved.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial

import json
import tempfile
import unittest
from pathlib import Path

from merge_quarto_indexes import merge_file, merge_items


class MergeQuartoIndexesTest(unittest.TestCase):
    def test_partial_items_replace_matching_base_items(self):
        base = [{"objectID": "old", "text": "keep"}, {"objectID": "changed", "text": "old"}]
        partial = [{"objectID": "changed", "text": "new"}, {"objectID": "new", "text": "add"}]

        self.assertEqual(
            merge_items(base, partial, "objectID"),
            [
                {"objectID": "old", "text": "keep"},
                {"objectID": "changed", "text": "new"},
                {"objectID": "new", "text": "add"},
            ],
        )

    def test_merge_file_updates_partial_path(self):
        with tempfile.TemporaryDirectory() as directory:
            base_path = Path(directory) / "base.json"
            partial_path = Path(directory) / "partial.json"
            base_path.write_text(json.dumps([{"listing": "/old", "items": ["a"]}]))
            partial_path.write_text(json.dumps([{"listing": "/new", "items": ["b"]}]))

            merge_file(base_path, partial_path, "listing")

            self.assertEqual(
                json.loads(partial_path.read_text()),
                [
                    {"listing": "/old", "items": ["a"]},
                    {"listing": "/new", "items": ["b"]},
                ],
            )

    def test_missing_key_is_rejected(self):
        with self.assertRaises(ValueError):
            merge_items([], [{"text": "missing object id"}], "objectID")


if __name__ == "__main__":
    unittest.main()
