"""
Dark Strategist v3.10.0 — Retriever
Lexical (BM25) retrieval at the document-feed layer. Two jobs:
  R1 intra-document: replace blind document[:N] truncation with role-relevant chunks.
  R2 reference corpus: inject relevant reference passages (optional; empty -> no-op).
        v3.10.0: BYO per-case corpus (load_corpus_files) + R2 token-overlap
        floor so zero-overlap passages are never injected as grounding. The floor
        is overlap-based (NOT BM25-score-based): on tiny BYO corpora BM25 IDF can
        be 0 for genuinely relevant terms, so a score floor would drop valid
        grounding; token overlap is robust to corpus size.

Pure Python + numpy via rank_bm25. No model, no API, no daemon, no native extension.
STRICTLY ADDITIVE: if the document fits the window and there is no corpus, OR retrieval
is unavailable, the legacy document[:N] behavior is preserved byte-for-byte.
"""
from __future__ import annotations

import os
import re
import json

try:
    from rank_bm25 import BM25Okapi
    _BM25_AVAILABLE = True
except Exception:
    _BM25_AVAILABLE = False


def _tokenize(text):
    #--- Lowercase alnum tokenization; keeps legal terms/article numbers intact for BM25.
    return re.findall(r"[a-z0-9]+", (text or "").lower())


def chunk(document, size=1000, overlap=150):
    """Splits a document into overlapping windows, preferring paragraph/newline breaks."""
    if not document:
        return []
    if len(document) <= size:
        return [document]
    chunks = []
    start, n = 0, len(document)
    while start < n:
        end = min(start + size, n)
        if end < n:
            window = document[start:end]
            brk = max(window.rfind("\n\n"), window.rfind("\n"))
            if brk >= int(size * 0.75):
                end = start + brk
        piece = document[start:end].strip()
        if piece:
            chunks.append(piece)
        if end >= n:
            break
        start = max(end - overlap, start + 1)
    return chunks


class Retriever:
    """BM25 retriever over a fixed passage list. Index once, query many."""

    def __init__(self, passages):
        self.passages = [p for p in (passages or []) if p and p.strip()]
        self._bm25 = None
        if _BM25_AVAILABLE and self.passages:
            tokenized = [_tokenize(p) for p in self.passages]
            if any(tokenized):
                self._bm25 = BM25Okapi(tokenized)

    @property
    def available(self):
        return self._bm25 is not None

    def query(self, text, top_k=5, drop_zero_overlap=False):
        #--- drop_zero_overlap=False -> R1 behavior unchanged, byte-identical.
        #--- True -> drop passages that share NO token with the query (pure noise).
        #--- Overlap-based, not score-based: BM25 IDF can be 0 for relevant terms
        #--- on tiny corpora, so a score floor yields false negatives; overlap does not.
        if not self.available or top_k <= 0:
            return []
        q = _tokenize(text)
        if not q:
            return self.passages[:top_k]
        scores = self._bm25.get_scores(q)
        ranked = sorted(range(len(self.passages)), key=lambda i: -scores[i])[:top_k]
        if drop_zero_overlap:
            qset = set(q)
            ranked = [i for i in ranked if qset & set(_tokenize(self.passages[i]))]
        return [self.passages[i] for i in ranked]


def load_corpus(corpus_id, base_dir="corpus"):
    """Loads a jurisdictional corpus by id into a passage list. Missing/None -> []."""
    if not corpus_id:
        return []
    for ext in (".jsonl", ".txt"):
        path = os.path.join(base_dir, str(corpus_id) + ext)
        if os.path.exists(path):
            try:
                if ext == ".jsonl":
                    out = []
                    with open(path, encoding="utf-8") as f:
                        for line in f:
                            line = line.strip()
                            if not line:
                                continue
                            try:
                                obj = json.loads(line)
                                out.append(obj.get("text", "") if isinstance(obj, dict) else str(obj))
                            except Exception:
                                out.append(line)
                    return [p for p in out if p and p.strip()]
                with open(path, encoding="utf-8") as f:
                    raw = f.read()
                return [p.strip() for p in raw.split("\n\n") if p.strip()]
            except Exception:
                return []
    return []


def load_corpus_files(paths, *, chunk_size=1000, chunk_overlap=150):
    """BYO per-case corpus: load arbitrary reference files into a passage list.

    Accepts a single path or a list. .jsonl/.txt parse as passages directly;
    other types (PDF/DOCX/PPTX/XLSX/HTML/MD/...) are converted to text via
    UNIT-INGEST (markitdown, lazy import) and chunked. Missing/unreadable files
    are skipped silently so the pipeline is never starved. Empty/None -> [].
    """
    if not paths:
        return []
    if isinstance(paths, str):
        paths = [paths]
    out = []
    for raw in paths:
        if not raw:
            continue
        path = str(raw)
        if not os.path.exists(path):
            continue
        ext = os.path.splitext(path)[1].lower()
        try:
            if ext == ".jsonl":
                with open(path, encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            obj = json.loads(line)
                            out.append(obj.get("text", "") if isinstance(obj, dict) else str(obj))
                        except Exception:
                            out.append(line)
            elif ext == ".txt":
                with open(path, encoding="utf-8") as f:
                    out.extend(p.strip() for p in f.read().split("\n\n"))
            else:
                #--- binary/markup -> UNIT-INGEST (markitdown) -> chunk.
                try:
                    from ingest import ingest_document
                    text = ingest_document(path)
                except Exception:
                    with open(path, encoding="utf-8", errors="replace") as f:
                        text = f.read()
                out.extend(chunk(text, chunk_size, chunk_overlap))
        except Exception:
            continue
    return [p for p in out if p and p.strip()]


def build_agent_context(document, query_text, *, window,
                        chunk_size=1000, chunk_overlap=150,
                        doc_top_k=6, corpus=None, corpus_top_k=3,
                        signals=None, signals_top_k=3):
    """Assembles the context fed to an agent.

    Non-breaking contract:
      - retrieval unavailable, OR (document fits `window` AND no corpus)
        -> returns document[:window]  (EXACT legacy behavior).
      - else -> role-relevant document chunks (R1) + optional corpus passages (R2),
        within the `window` budget; never returns empty doc context.
    """
    legacy = document[:window]
    if not _BM25_AVAILABLE:
        return legacy
    fits = len(document) <= window
    has_corpus = bool(corpus)
    has_signals = bool(signals)
    if fits and not has_corpus and not has_signals:
        return legacy  #--- preserve byte-identical legacy path

    parts = []
    budget = window
    if not fits:
        pieces = chunk(document, chunk_size, chunk_overlap)
        r = Retriever(pieces)
        picked = r.query(query_text, doc_top_k) if r.available else []
        if not picked:
            picked = [legacy]  #--- never hand an agent an empty document
        doc_block = "\n\n[...]\n\n".join(picked)[:budget]
        parts.append(doc_block)
        budget -= len(doc_block)
    else:
        parts.append(document)
        budget -= len(document)

    if has_corpus and budget > 200:
        cr = Retriever(corpus)
        cps = cr.query(query_text or document[:500], corpus_top_k, drop_zero_overlap=True) if cr.available else []
        if cps:
            block = "\n\n[JURISDICTIONAL CORPUS - REFERENCE GROUNDING]\n" + "\n\n".join(cps)
            block = block[:budget]
            parts.append(block)
            budget -= len(block)

    if has_signals and budget > 200:
        #--- P4 (v3.14.0): external signals = time-sensitive EVIDENCE, a channel distinct
        #--- from jurisdictional grounding. drop_zero_overlap keeps pure-noise passages out.
        #--- The directive travels inside the block so it reaches the agent verbatim with NO
        #--- prompt_engine change. NON-BINDING: signals may substantiate a Finding; they never
        #--- set the verdict (severity rule governs).
        sr = Retriever(signals)
        sps = sr.query(query_text or document[:500], signals_top_k, drop_zero_overlap=True) if sr.available else []
        if sps:
            header = ("\n\n[EXTERNAL SIGNALS - TIME-SENSITIVE EVIDENCE]\n"
                      "(External evidence. Weigh against the document's claims; a contradiction "
                      "or gap here MAY substantiate a Finding under the normal severity rule. "
                      "This is evidence, NOT a verdict input.)\n")
            block = header + "\n\n".join(sps)
            parts.append(block[:budget])

    return "\n\n".join(parts)
