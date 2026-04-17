"""
CV Parser — Extract text + structured profile from uploaded PDF files in-memory.

No files are written to disk. The PDF bytes are read, text is extracted
using PyPDF2, cleaned up, and returned as a trimmed string.

The structured profile extraction uses regex patterns + LLM to extract
all possible fields for form auto-population.
"""

from __future__ import annotations

import io
import json
import re
from typing import Optional

import structlog

log = structlog.get_logger("utils.cv_parser")

MAX_CV_CHARS = 10000  # Increased to capture more detail from CVs


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


# ── Regex-based extraction helpers ──────────────────────────────────────────

def _extract_gpa_regex(cv_text: str) -> Optional[str]:
    """Extract GPA using multiple regex patterns."""
    patterns = [
        r'(?:cumulative\s*)?(?:c)?gpa[:\s]*([0-4]\.\d{1,2})\s*(?:out of|/|on a scale of)?\s*(?:4\.?0?)?',
        r'([0-4]\.\d{1,2})\s*/\s*4\.?0?',
        r'(?:grade point average|gpa)[:\s]*([0-4]\.\d{1,2})',
        r'([0-4]\.\d{1,2})\s*(?:gpa|grade point)',
    ]
    for pattern in patterns:
        match = re.search(pattern, cv_text, re.IGNORECASE)
        if match:
            try:
                gpa = float(match.group(1))
                if 0.0 < gpa <= 4.0:
                    return str(gpa)
            except ValueError:
                pass
    return None


def _extract_ielts_regex(cv_text: str) -> dict:
    """Extract IELTS scores (overall + band scores) using regex."""
    results = {}
    
    # Overall score
    overall_patterns = [
        r'ielts[:\s]*(?:overall[:\s]*)?([4-9]\.?[05]?)',
        r'ielts\s*(?:score|band)[:\s]*([4-9]\.?[05]?)',
        r'(?:english\s*proficiency|language)[:\s]*ielts[:\s]*([4-9]\.?[05]?)',
        r'ielts\s*academic[:\s]*([4-9]\.?[05]?)',
    ]
    for pattern in overall_patterns:
        match = re.search(pattern, cv_text, re.IGNORECASE)
        if match:
            try:
                score = float(match.group(1))
                if 4.0 <= score <= 9.0:
                    results['ielts_overall'] = str(score)
                    break
            except ValueError:
                pass
    
    # Band scores
    for band in ['reading', 'writing', 'speaking', 'listening']:
        band_patterns = [
            rf'{band}[:\s]*([4-9]\.?[05]?)',
            rf'(?:ielts|band)\s*{band}[:\s]*([4-9]\.?[05]?)',
        ]
        for pattern in band_patterns:
            match = re.search(pattern, cv_text, re.IGNORECASE)
            if match:
                try:
                    score = float(match.group(1))
                    if 4.0 <= score <= 9.0:
                        results[f'ielts_{band}'] = str(score)
                        break
                except ValueError:
                    pass
    
    return results


def _extract_qualification_regex(cv_text: str) -> Optional[str]:
    """Extract highest qualification level from CV text."""
    cv_lower = cv_text.lower()
    
    # Check for PhD first (highest)
    if any(k in cv_lower for k in ('ph.d', 'phd', 'doctor of philosophy', 'doctoral')):
        return 'doctorate'
    
    # Then Masters
    if any(k in cv_lower for k in ('master', 'msc', 'mba', 'meng', 'm.s.', 'm.a.', 'ma ', 'ms ')):
        return 'masters'
    
    # Then Bachelors
    if any(k in cv_lower for k in ('bachelor', 'bsc', 'b.sc', 'btech', 'b.tech', 'b.e.', 'be ', 'ba ', 'b.a.')):
        return 'bachelors'
    
    # Then High School
    if any(k in cv_lower for k in ('high school', 'secondary', '+2', '12th', 'a-level', 'a level', 'slc', 'ssc', 'hsc', 'intermediate')):
        return 'high_school'
    
    return None


def _extract_work_experience_regex(cv_text: str) -> Optional[int]:
    """Extract approximate years of work experience from CV."""
    # Look for explicit mentions
    patterns = [
        r'(\d+)\+?\s*years?\s*(?:of\s*)?(?:experience|work)',
        r'(?:experience|work)[:\s]*(\d+)\+?\s*years?',
        r'(\d+)\+?\s*years?\s*(?:in\s*the\s*)?(?:industry|field|sector)',
    ]
    for pattern in patterns:
        match = re.search(pattern, cv_text, re.IGNORECASE)
        if match:
            try:
                years = int(match.group(1))
                if 0 <= years <= 50:
                    return years
            except ValueError:
                pass
    
    # Try counting date ranges in experience sections
    date_ranges = re.findall(
        r'(20\d{2}|19\d{2})\s*[-–—to]+\s*(20\d{2}|19\d{2}|present|current|now)',
        cv_text, re.IGNORECASE
    )
    if date_ranges:
        total_years = 0
        for start, end in date_ranges:
            try:
                start_year = int(start)
                end_year = 2026 if end.lower() in ('present', 'current', 'now') else int(end)
                total_years += max(0, end_year - start_year)
            except ValueError:
                pass
        if total_years > 0:
            return min(total_years, 50)
    
    return None


def _extract_nationality_regex(cv_text: str) -> Optional[str]:
    """Try to extract nationality from CV text."""
    # Common nationality patterns
    patterns = [
        r'nationality[:\s]*([\w\s]+?)(?:\n|$|,|;)',
        r'citizen(?:ship)?[:\s]*([\w\s]+?)(?:\n|$|,|;)',
        r'passport[:\s]*([\w\s]+?)(?:\n|$|,|;)',
        r'national(?:ity)?[:\s]*([\w\s]+?)(?:\n|$|,|;)',
    ]
    
    nationality_map = {
        'nepal': 'nepalese', 'nepalese': 'nepalese', 'nepali': 'nepalese',
        'india': 'indian', 'indian': 'indian',
        'bangladesh': 'bangladeshi', 'bangladeshi': 'bangladeshi',
        'pakistan': 'pakistani', 'pakistani': 'pakistani',
        'sri lanka': 'sri lankan', 'sri lankan': 'sri lankan',
        'china': 'chinese', 'chinese': 'chinese',
        'vietnam': 'vietnamese', 'vietnamese': 'vietnamese',
        'philippines': 'filipino', 'filipino': 'filipino',
        'indonesia': 'indonesian', 'indonesian': 'indonesian',
        'nigeria': 'nigerian', 'nigerian': 'nigerian',
        'ghana': 'ghanaian', 'ghanaian': 'ghanaian',
        'kenya': 'kenyan', 'kenyan': 'kenyan',
        'ethiopia': 'ethiopian', 'ethiopian': 'ethiopian',
        'egypt': 'egyptian', 'egyptian': 'egyptian',
        'brazil': 'brazilian', 'brazilian': 'brazilian',
        'colombia': 'colombian', 'colombian': 'colombian',
        'mexico': 'mexican', 'mexican': 'mexican',
        'turkey': 'turkish', 'turkish': 'turkish',
        'iran': 'iranian', 'iranian': 'iranian',
        'thailand': 'thai', 'thai': 'thai',
        'myanmar': 'myanmar', 'burmese': 'myanmar',
        'cambodia': 'cambodian', 'cambodian': 'cambodian',
        'mongolia': 'mongolian', 'mongolian': 'mongolian',
        'afghanistan': 'afghan', 'afghan': 'afghan',
    }
    
    for pattern in patterns:
        match = re.search(pattern, cv_text, re.IGNORECASE)
        if match:
            raw = match.group(1).strip().lower()
            for key, val in nationality_map.items():
                if key in raw:
                    return val
    
    return None


def _extract_email_regex(cv_text: str) -> Optional[str]:
    """Extract email address from CV."""
    match = re.search(r'[\w.+-]+@[\w-]+\.[\w.]+', cv_text)
    return match.group(0) if match else None


def _extract_phone_regex(cv_text: str) -> Optional[str]:
    """Extract phone number from CV."""
    match = re.search(r'(?:\+?\d{1,3}[-.\s]?)?\(?\d{2,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}', cv_text)
    return match.group(0).strip() if match else None


def _extract_name_regex(cv_text: str) -> Optional[str]:
    """Try to extract name — typically the first significant line."""
    lines = [l.strip() for l in cv_text.split('\n') if l.strip()]
    for line in lines[:5]:
        # Skip lines that look like headers, emails, phones, addresses
        if any(skip in line.lower() for skip in ['curriculum', 'resume', 'cv', '@', 'http', 'address', 'phone', 'tel']):
            continue
        # Skip very long lines (likely paragraphs)
        if len(line) > 60:
            continue
        # Skip lines with mostly numbers
        if sum(c.isdigit() for c in line) > len(line) * 0.3:
            continue
        # This is likely a name
        if 2 <= len(line.split()) <= 5:
            return line
    return None


# ── Comprehensive profile extraction ───────────────────────────────────────

async def extract_structured_profile(cv_text: str) -> dict:
    """
    Extract a comprehensive structured profile from CV text.
    
    Combines fast regex extraction with an LLM pass to fill gaps.
    Returns a dict with all possible profile fields for form auto-population.
    """
    if not cv_text:
        return {}
    
    # Phase 1: Fast regex extraction
    profile = {}
    
    name = _extract_name_regex(cv_text)
    if name:
        profile['name'] = name
    
    email = _extract_email_regex(cv_text)
    if email:
        profile['email'] = email
    
    phone = _extract_phone_regex(cv_text)
    if phone:
        profile['phone'] = phone
    
    nationality = _extract_nationality_regex(cv_text)
    if nationality:
        profile['nationality'] = nationality
    
    gpa = _extract_gpa_regex(cv_text)
    if gpa:
        profile['gpa'] = gpa
    
    ielts = _extract_ielts_regex(cv_text)
    if ielts:
        profile.update(ielts)
    
    qualification = _extract_qualification_regex(cv_text)
    if qualification:
        profile['current_qualification'] = qualification
    
    work_years = _extract_work_experience_regex(cv_text)
    if work_years is not None:
        profile['work_experience_years'] = work_years
    
    log.info("cv_regex_extraction", fields_found=list(profile.keys()))
    
    # Phase 2: LLM extraction to fill gaps and get semantic fields
    try:
        from src.utils.groq_cascade import non_streaming_groq
        
        # Build a prompt that asks for ONLY what regex missed
        missing_fields = []
        if 'nationality' not in profile:
            missing_fields.append('"nationality": "lowercase nationality (e.g. nepalese, indian) or null"')
        if 'current_qualification' not in profile:
            missing_fields.append('"current_qualification": "one of: high_school, bachelors, masters, doctorate (highest completed) or null"')
        if 'gpa' not in profile:
            missing_fields.append('"gpa": "GPA out of 4.0 as string, or null"')
        if 'ielts_overall' not in profile:
            missing_fields.append('"ielts_overall": "IELTS overall score as string, or null"')
        if 'work_experience_years' not in profile:
            missing_fields.append('"work_experience_years": "integer years of work experience, or 0"')
        
        # Always ask for fields regex can't handle well
        always_fields = [
            '"target_subject": "the best subject for this student to study next based on their background (2-4 words, e.g. Computer Science, Data Science, MBA). IMPORTANT: infer this from their education + experience"',
            '"career_goal": "likely career goal based on their experience and education (1 sentence)"',
            '"skills": ["list", "of", "top", "5-8", "skills"]',
            '"education_summary": "one line summary of highest education, e.g. BSc Computer Science from Tribhuvan University (2020)"',
            '"strengths": ["2-3 key strengths that make this student competitive"]',
            '"gaps": ["1-2 areas the student should work on before applying"]',
        ]
        
        all_fields = missing_fields + always_fields
        
        system_prompt = f"""You are an expert CV parser and education counselor. Analyze the CV below and extract the requested fields as a JSON object.

CRITICAL RULES:
1. Return ONLY valid JSON — no markdown, no explanation, no code fences
2. For nationality, use lowercase (e.g. "nepalese", "indian", "chinese")
3. For current_qualification, use ONLY: "high_school", "bachelors", "masters", "doctorate"
4. For target_subject, infer what makes MOST sense as the NEXT degree based on their education + career trajectory
5. Be specific and actionable — no generic advice
6. If you can't determine a field, use null (not "unknown")

Return JSON with these fields:
{{{', '.join(all_fields)}}}"""

        user_prompt = f"CV Content:\n{cv_text[:8000]}"
        
        res = await non_streaming_groq(system_prompt, user_prompt, max_tokens=500, temperature=0.1)
        content = res.get("content", "").strip()
        
        # Clean up LLM response — remove code fences if present
        content = re.sub(r'^```(?:json)?\s*', '', content)
        content = re.sub(r'\s*```$', '', content)
        content = content.strip()
        
        llm_data = json.loads(content)
        
        # Merge LLM results — regex takes priority for fields it found
        for key, value in llm_data.items():
            if value is not None and value != "" and value != [] and key not in profile:
                profile[key] = value
        
        # Always take LLM's semantic analysis fields (skills, career_goal, etc.)
        for key in ['target_subject', 'career_goal', 'skills', 'education_summary', 'strengths', 'gaps']:
            if key in llm_data and llm_data[key]:
                profile[key] = llm_data[key]
        
        log.info("cv_llm_extraction_complete", total_fields=len(profile))
        
    except json.JSONDecodeError as e:
        log.warning("cv_llm_json_parse_failed", error=str(e))
    except Exception as e:
        log.warning("cv_llm_extraction_failed", error=str(e))
    
    return profile
