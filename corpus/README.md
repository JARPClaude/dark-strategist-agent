# Reference Corpus (BYO per-case)

The forensic pipeline attaches **case-specific reference texts at runtime** via the
`--corpus` flag (or the wizard's "Attach reference texts?" step). This repo ships the
retrieval **MECHANISM only** and intentionally holds **no laws or jurisdictional
content**, so it scales to any jurisdiction with zero maintenance.

- Attach any number of files at run time, e.g.:
  `python main.py --type legal --subscenario lease --objective "..." --tribunal --corpus laws/x.pdf laws/y.txt`
- Supported: `.txt` / `.md` / `.jsonl` direct; `.pdf` / `.docx` / `.pptx` / `.xlsx` / `.html`
  via markitdown, then chunked.
- R2 floor is **token-overlap** based: passages with zero token overlap with the query
  are dropped as noise (robust to small corpora).
- Without `--corpus`, R2 is a no-op and the legacy `[:N]` document feed is preserved
  byte-identical (non-breaking).
- `JURISDICTION_CORPUS_MAP` in `orchestrator/catalogs.py` is an empty, dormant hook --
  NOT the active path. Do not pre-load jurisdictional content into this repo.
