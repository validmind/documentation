# Complete documentation rendering

Full HTML builds and the LLM corpus use `render_docs.py`. It renders all inputs
from `quarto inspect`, with two isolated workers by default. It does not reuse
HTML or Markdown from a previous build.

```sh
# Generated source repositories must already be populated, as in CI.
python3 scripts/render_docs.py --profile production
DOCS_RENDER_JOBS=4 python3 scripts/render_docs.py --profile development
DOCS_RENDER_JOBS=1 python3 scripts/render_docs.py --profile production
make -C site render-llm
```

`DOCS_RENDER_JOBS=1` runs the native full-project Quarto render for comparison
or troubleshooting. Additional workers require additional memory and disk space;
each gets its own source copy, Quarto cache, and output directory. The default
of two fits the standard CI runner. Targeted PR previews keep their existing
render selection.

Directory targets preserve the complete project input list, so cross-directory
links and navigation resolve normally. Each input belongs to exactly one worker.
Listings are temporarily deferred in worker copies of page metadata, then rendered
with their original metadata against the complete fresh HTML. This final pass is
necessary because Quarto reads listing descriptions and thumbnails from rendered
pages. Search and listing indexes are combined; differing shared resources or
conflicting index entries fail the build. Worker errors propagate, and output is
only replaced after rendering and merging succeed. Existing CI warning checks
still apply.

Custom project hooks (including the Docker profile), inherited listing metadata,
and native Quarto sitemap configurations use the serial path to preserve their
full-project behavior. The repository's separate sitemap Make target is unchanged.
Notebook execution settings and freeze behavior are preserved.

Run the safety and real-Quarto equivalence tests with:

```sh
python3 -m unittest discover -s scripts -p test_render_docs.py -v
```

They compare HTML, RevealJS, aliases, includes, listings, search, and GFM output
with a serial render, check that stale files disappear, and check that a failed
worker preserves the previous site. Full rendering still validates the complete
production profile. Production deployment still requires the successful staging
workflow's artifact for the exact prospective production Git tree.
