# ─── UNIT-INGEST — Document Ingestion Preprocessor ───────────────────────────
"""
UNIT-INGEST — Preprocessing utility (NOT a forensic finding-emitter).
Converts non-plaintext documents (PDF/DOCX/PPTX/XLSX/HTML) to Markdown via
markitdown so the pipeline always receives analyzable text. Plaintext passes
through. Never raises on unsupported/failed types — returns best-effort text
so the forensic pipeline is never starved of input.
"""
from pathlib import Path

# Extensions markitdown converts to Markdown
_CONVERT_EXTS = {".pdf", ".docx", ".pptx", ".xlsx", ".xls", ".html", ".htm"}


def ingest_document(path: str) -> str:
    """Return document content as text. Convertible types -> Markdown; everything
    else -> UTF-8 read with replacement. Degrades gracefully, never crashes."""
    p = Path(path)
    ext = p.suffix.lower()

    if ext in _CONVERT_EXTS:
        try:
            from markitdown import MarkItDown
            return MarkItDown().convert(str(p)).text_content
        except ImportError:
            # markitdown absent -> raw read, keep pipeline alive
            return p.read_text(encoding="utf-8", errors="replace")
        except Exception as exc:
            # conversion failed -> visible marker + raw fallback
            return (f"[UNIT-INGEST conversion failed for {p.name}: {exc}]\n"
                    + p.read_text(encoding="utf-8", errors="replace"))

    # plaintext or unknown -> direct read
    return p.read_text(encoding="utf-8", errors="replace")