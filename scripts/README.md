# Complete documentation rendering

Full HTML builds and the LLM corpus use `render_docs.py`. It renders all inputs
from `quarto inspect`, with up to four isolated workers by default. It does not reuse
HTML or Markdown from a previous build.

```sh
# Generated source repositories must already be populated, as in CI.
uv run --with pyyaml python scripts/render_docs.py --profile production
DOCS_RENDER_JOBS=2 uv run --with pyyaml python scripts/render_docs.py --profile development
DOCS_RENDER_JOBS=1 uv run --with pyyaml python scripts/render_docs.py --profile production
make -C site render-llm
```

`DOCS_RENDER_JOBS=1` runs the native full-project Quarto render for comparison
or troubleshooting. Additional workers require additional memory and disk space;
each gets its own source copy, Quarto cache, and output directory. The default
uses the available CPUs, capped at four. Targeted PR previews keep their existing
render selection.

Directory targets preserve the complete project input list, so cross-directory
links and navigation resolve normally. Each input belongs to exactly one worker.
Listings are temporarily deferred in worker copies of page metadata, then rendered
with their original metadata against the complete fresh HTML. This final pass is
necessary because Quarto reads listing descriptions and thumbnails from rendered
pages. The listing pass groups nearby pages into directory renders to avoid
repeating project finalization for every listing. It clears only the supplemental
listing cache between groups because all listings are explicitly covered. A listing whose description or thumbnail depends on another listing
uses the native render instead. Search and listing indexes are combined; differing shared resources or
conflicting index entries fail the build. Worker errors propagate, and output is
only replaced after rendering and merging succeed. Existing CI warning checks
still apply.

Custom project hooks (including the Docker profile), inherited listing metadata,
and native Quarto sitemap configurations use the serial path to preserve their
full-project behavior. The repository's separate sitemap Make target is unchanged.
Notebook execution settings and freeze behavior are preserved. `uv` supplies
PyYAML for reading page metadata. Multi-format training aliases consistently target the first configured format.
Quarto can otherwise choose the alternate HTML output during incremental renders;
this normalization makes training redirects point to their slide decks.

Run the safety and real-Quarto equivalence tests with:

```sh
uv run --with pyyaml python -m unittest discover -s scripts -p test_render_docs.py -v
```

They compare HTML, RevealJS, aliases, includes, listings, search, and GFM output
with a serial render, check that stale files disappear, and check that a failed
worker preserves the previous site. Full rendering still validates the complete
production profile. Production deployment still requires the successful staging
workflow's artifact for the exact prospective production Git tree.
