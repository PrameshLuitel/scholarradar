"""
CV Parser — Extract text from uploaded PDF files in-memory.

No files are written to disk. The PDF bytes are read, text is extracted
using PyPDF2, cleaned up, and returned as a trimmed string.
"""

from __future__ import annotations

import io
import re
from typing import Optional

import structlog

log = structlog.get_logger("utils.cv_parser")

MAX_CV_CHARS = 6000  # Keep CV text within LLM context limits


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """
    Extract text content from a PDF file's raw bytes.

    Returns cleaned text capped at MAX_CV_CHARS characters.
    Raises ValueError if the file cannot be parsed.
    """
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        raise ImportError(
            "PyPDF2 is required for CV parsing. Run: pip install PyPDF2"
        )

    try:
        reader = PdfReader(io.BytesIO(pdf_bytes))
        pages_text: list[str] = []

        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                pages_text.append(text.strip())

        if not pages_text:
            raise ValueError("No text could be extracted from the PDF. The file may be image-based or corrupted.")

        raw_text = "\n\n".join(pages_text)
        cleaned = _clean_cv_text(raw_text)

        if len(cleaned) > MAX_CV_CHARS:
            cleaned = cleaned[:MAX_CV_CHARS] + "\n\n[... CV text truncated for processing ...]"

        log.info(
            "cv_parsed",
            pages=len(reader.pages),
            raw_chars=len(raw_text),
            cleaned_chars=len(cleaned),
        )
        return cleaned

    except ValueError:
        raise
    except Exception as e:
        log.error("cv_parse_failed", error=str(e))
        raise ValueError(f"Failed to parse PDF: {str(e)}")


def _clean_cv_text(text: str) -> str:
    """Clean extracted CV text — normalize whitespace, remove artifacts."""
    # Collapse multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Collapse multiple spaces
    text = re.sub(r" {2,}", " ", text)
    # Remove common PDF artifacts
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text)
    # Strip each line
    lines = [line.strip() for line in text.split("\n")]
    text = "\n".join(lines)
    return text.strip()


def summarize_cv_for_prompt(cv_text: str) -> str:
    """
    Wrap CV text in a clear section header for the LLM prompt.
    """
    if not cv_text or not cv_text.strip():
        return ""
    return f"""## Student's CV/Resume Content
<cv>
{cv_text}
</cv>

Please analyze the CV above to understand the student's:
- Educational background and qualifications
- Work experience and skills
- Research experience or publications (if any)
- Extracurricular activities and achievements
- Any gaps or areas that need strengthening
"""
