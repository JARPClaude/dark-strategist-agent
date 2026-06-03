# Jurisdictional Corpus (v3.8.0)

Optional local corpora for RAG R2 (jurisdictional grounding). Empty by default:
the retrieval MECHANISM ships in v3.8.0; CONTENT is populated incrementally.

- File per corpus id: `corpus/<id>.txt` (passages separated by blank lines) or
  `corpus/<id>.jsonl` (one JSON object per line with a `text` field).
- Map domain -> corpus id in `orchestrator/catalogs.py::JURISDICTION_CORPUS_MAP`.
- Missing / unmapped corpus => retriever falls back to the legacy [:N] document
  feed (non-breaking).
