"""
FindUni.online Offers & Services MCP tools — 4 tools:
  1. get_exam_booking_info — English test booking with discounts
  2. get_current_offers — Active scholarship and admission offers
  3. get_ielts_class_info — IELTS preparation class details
  4. get_banking_partners — Education loan banking partners

All data embedded directly from FindUni.online.
Powered by GYCO Consultants / FindUni.online.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any, Optional

import structlog
from fastmcp import FastMCP

log = structlog.get_logger("mcp_server.tools.finduni_offers")

# ── Exam Booking Data ─────────────────────────────────────────────────────

_EXAM_INFO = {
    "ielts": {
        "name": "IELTS (International English Language Testing System)",
        "types": ["IELTS Academic", "IELTS General Training"],
        "for_students": "IELTS Academic — required for university admissions",
        "standard_price_npr": 34000,
        "finduni_discount": "Discounted through FindUni x IDP partnership",
        "booking_url": "https://finduni.online/booking.php",
        "results_timeline": "13 calendar days (paper) / 3-5 days (computer-delivered)",
        "validity": "2 years from test date",
        "sections": ["Listening (30 min)", "Reading (60 min)", "Writing (60 min)", "Speaking (11-14 min)"],
        "total_duration": "2 hours 45 minutes",
        "scoring": "Band 1-9 (0.5 increments)",
        "test_centres_nepal": [
            "British Council Kathmandu",
            "IDP IELTS Kathmandu",
            "IDP IELTS Pokhara",
            "IDP IELTS Chitwan",
        ],
        "tips": [
            "Book at least 3-4 weeks in advance for preferred dates",
            "Computer-delivered IELTS gives faster results (3-5 days)",
            "Practice with Cambridge IELTS books (14-18 are latest)",
            "IELTS Academic is required for university admission — NOT General Training",
        ],
    },
    "pte": {
        "name": "PTE Academic (Pearson Test of English)",
        "types": ["PTE Academic"],
        "for_students": "Accepted by most Australian universities as IELTS alternative",
        "standard_price_npr": 31000,
        "finduni_price_npr": 27000,
        "finduni_discount": "Book through FindUni for NPR 27,000 only — lowest rate in Nepal",
        "booking_url": "https://finduni.online/booking.php",
        "results_timeline": "Typically within 48 hours",
        "validity": "2 years from test date",
        "sections": ["Speaking & Writing (54-67 min)", "Reading (29-30 min)", "Listening (30-43 min)"],
        "total_duration": "Approximately 2 hours",
        "scoring": "10-90 points",
        "score_equivalence": {
            "ielts_6.0": "PTE 50",
            "ielts_6.5": "PTE 58",
            "ielts_7.0": "PTE 65",
            "ielts_7.5": "PTE 73",
            "ielts_8.0": "PTE 79",
        },
        "tips": [
            "PTE is 100% computer-based — no human examiner for speaking",
            "Results come in 48 hours — much faster than IELTS",
            "Many students find PTE speaking easier than IELTS face-to-face",
            "Unlimited score sends to universities (free)",
        ],
    },
    "toefl": {
        "name": "TOEFL iBT (Test of English as a Foreign Language)",
        "types": ["TOEFL iBT"],
        "for_students": "Widely accepted by US, UK, Australian, and Canadian universities",
        "standard_price_usd": 210,
        "finduni_discount": "Use promo code NPL1043101 for $20 off",
        "promo_code": "NPL1043101",
        "savings": "$20 USD",
        "booking_url": "https://www.ets.org/toefl",
        "results_timeline": "6-10 days after test",
        "validity": "2 years from test date",
        "sections": ["Reading (35 min)", "Listening (36 min)", "Speaking (16 min)", "Writing (29 min)"],
        "total_duration": "Under 2 hours",
        "scoring": "0-120 points (30 per section)",
        "score_equivalence": {
            "ielts_6.0": "TOEFL 60-78",
            "ielts_6.5": "TOEFL 79-93",
            "ielts_7.0": "TOEFL 94-101",
            "ielts_7.5": "TOEFL 102-109",
            "ielts_8.0": "TOEFL 110-114",
        },
        "tips": [
            "Use FindUni promo code NPL1043101 to save $20",
            "TOEFL Best Scores feature lets you combine best section scores",
            "Shorter test than IELTS — under 2 hours total",
            "Good option if you're also applying to US universities",
        ],
    },
}

# ── Current Offers ────────────────────────────────────────────────────────

_CURRENT_OFFERS = [
    # University & Admission Offers
    {
        "id": "uk-scholarship-june-2026",
        "title": "Study in the UK with GBP 3,000-3,500 Scholarship",
        "type": "university_scholarship",
        "destination": "UK",
        "description": "Study in London, Manchester, or Leeds in Business, Law, Psychology, IT, and more with up to GBP 3,500 Scholarship.",
        "intake": "June 2026",
        "value": "Up to GBP 3,500",
        "subjects": ["Business", "Law", "Psychology", "IT", "Engineering"],
        "cities": ["London", "Manchester", "Leeds"],
        "eligibility": "International students from Nepal",
        "how_to_apply": "Contact FindUni/GYCO counsellor via WhatsApp",
        "apply_url": "https://wa.link/2pd93s",
        "is_active": True,
    },
    {
        "id": "utas-35pct-scholarship",
        "title": "35% Scholarship at UTAS Sydney/Melbourne",
        "type": "university_scholarship",
        "destination": "Australia",
        "description": "Study at University of Tasmania (UTAS) Sydney and Melbourne campuses with 35% scholarship, bringing fees down to approximately AUD 22,000 per year.",
        "value": "35% tuition reduction → ~AUD 22,000/year",
        "university": "University of Tasmania (UTAS)",
        "cities": ["Sydney", "Melbourne"],
        "eligibility": "International students — limited seats available",
        "how_to_apply": "Contact FindUni/GYCO counsellor via WhatsApp",
        "apply_url": "https://wa.link/68wkmn",
        "is_active": True,
    },
    {
        "id": "canberra-ece-scholarship",
        "title": "Early Childhood Education Scholarship — University of Canberra",
        "type": "university_scholarship",
        "destination": "Australia",
        "description": "Study Bachelor of Early Childhood Education in Sydney from University of Canberra with 10-20% scholarship. No quota on seats.",
        "value": "10-20% tuition scholarship",
        "university": "University of Canberra",
        "cities": ["Sydney"],
        "course": "Bachelor of Early Childhood Education",
        "eligibility": "International students — no seat quota",
        "how_to_apply": "Contact FindUni/GYCO counsellor via WhatsApp",
        "apply_url": "https://wa.link/68wkmn",
        "is_active": True,
    },
    {
        "id": "curtin-merit-20pct",
        "title": "Curtin Global Merit Scholarship — 20% in Perth",
        "type": "university_scholarship",
        "destination": "Australia",
        "description": "The Curtin Global Merit Scholarship rewards academic performance. Eligible students receive 20% off tuition fee for the entire course duration.",
        "value": "20% off tuition for full course duration",
        "university": "Curtin University",
        "cities": ["Perth"],
        "eligibility": "Based on academic merit — strong GPA required",
        "how_to_apply": "Contact FindUni/GYCO counsellor via WhatsApp",
        "apply_url": "https://wa.link/68wkmn",
        "is_active": True,
    },
    # Exam Discounts
    {
        "id": "ielts-discount-idp",
        "title": "IELTS with Discount via IDP Partnership",
        "type": "exam_discount",
        "description": "Book your IELTS tests with discount through FindUni's IDP partnership. Includes exclusive practice materials and instant booking.",
        "test_type": "IELTS",
        "discount_details": "Discounted rate + free practice materials",
        "booking_url": "https://finduni.online/booking.php",
        "is_active": True,
    },
    {
        "id": "pte-27000",
        "title": "PTE Academic for NPR 27,000 Only",
        "type": "exam_discount",
        "description": "Book your PTE Academic for just NPR 27,000 through FindUni — the best rate in Nepal. Significantly cheaper than standard pricing.",
        "test_type": "PTE",
        "standard_price": "NPR 31,000",
        "finduni_price": "NPR 27,000",
        "savings": "NPR 4,000",
        "booking_url": "https://finduni.online/booking.php",
        "is_active": True,
    },
    {
        "id": "toefl-20-off",
        "title": "Save $20 on TOEFL Test",
        "type": "exam_discount",
        "description": "Use the FindUni promo code to save $20 off your TOEFL test registration.",
        "test_type": "TOEFL",
        "promo_code": "NPL1043101",
        "savings": "$20 USD",
        "booking_url": "https://finduni.online/booking.php",
        "is_active": True,
    },
]

# ── IELTS Class Data ──────────────────────────────────────────────────────

_IELTS_CLASS = {
    "provider": "GYCO Consultants",
    "format": "4-week rolling program",
    "max_students": 6,
    "note": "Maximum 6 students per class for personalized attention",
    "pricing": {
        "initial_payment": 4000,
        "continuation_payment": 3500,
        "total": 7500,
        "currency": "NPR",
        "payment_structure": "Pay NPR 4,000 to book your seat. Attend the first 2 days. Pay remaining NPR 3,500 to continue the full 4-week course.",
    },
    "what_you_get": [
        "4 weeks of intensive IELTS preparation",
        "Small class size (max 6 students) for individual attention",
        "All 4 sections covered: Listening, Reading, Writing, Speaking",
        "Practice tests and mock exams",
        "Expert feedback on writing and speaking",
        "Study materials provided",
        "Flexible scheduling",
    ],
    "booking_url": "https://finduni.online/class.php",
    "contact": {
        "whatsapp": "https://wa.link/wri8z2",
        "phone": "01-4545747",
    },
}

# ── Banking Partners ──────────────────────────────────────────────────────

_BANKING_PARTNERS = [
    {
        "bank": "Nabil Bank",
        "branch": "Maligaun Branch",
        "contact_person": "Utsab Shrestha",
        "phone": "9841339931",
        "whatsapp": "https://wa.me/9779841339931",
        "services": ["Education Loan", "Student Account", "Foreign Currency Exchange"],
    },
    {
        "bank": "Kumari Bank Limited",
        "branch": "Kirtipur Branch",
        "contact_person": "Bikesh Shrestha",
        "phone": "9852044433",
        "whatsapp": "https://wa.me/9779852044433",
        "services": ["Education Loan", "Student Account", "Foreign Currency Exchange"],
    },
]


from src.utils.analytics import log_search


def register_tools(mcp: FastMCP):
    """Register all 4 FindUni offers tools."""

    # ────────────────────────────────────────────────────────────────────
    # 1. get_exam_booking_info
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    @log_search("get_exam_booking_info")
    async def get_exam_booking_info(
        test_type: str = "ielts",
    ) -> dict[str, Any]:
        """Get English test booking information with FindUni discounts.
        Use when student asks about IELTS, PTE, or TOEFL — fees, booking, promo codes, or test centres.
        Do not use for checking university IELTS requirements.

        Includes pricing, discounts, promo codes, test centres, and booking links.
        Based on FindUni.online English Test Booking — powered by GYCO Consultants.

        Args:
            test_type: One of "ielts", "pte", "toefl", or "all" for comparison.
        """
        try:
            log.info("tool_call", tool="get_exam_booking_info")

            test_lower = test_type.lower().strip()

            if test_lower == "all":
                return {
                    "tests": {k: v for k, v in _EXAM_INFO.items()},
                    "comparison": {
                        "cheapest": "PTE Academic at NPR 27,000 through FindUni",
                        "fastest_results": "PTE Academic — 48 hours",
                        "most_accepted": "IELTS Academic — accepted by all Australian universities",
                        "recommendation": "IELTS Academic is the safest choice for Australian student visa. PTE is a good alternative if you prefer computer-based testing.",
                    },
                    "booking_url": "https://finduni.online/booking.php",
                    "source": "FindUni.online English Test Booking — powered by GYCO Consultants",
                    "data_freshness": datetime.now().isoformat(),
                }

            if test_lower not in _EXAM_INFO:
                return {
                    "error": f"Unknown test type: '{test_type}'. Valid options: ielts, pte, toefl, all",
                    "error_type": "validation_error",
                }

            exam = _EXAM_INFO[test_lower]
            return {
                "test": exam,
                "booking_url": exam.get("booking_url", "https://finduni.online/booking.php"),
                "promo_code": exam.get("promo_code"),
                "source": "FindUni.online English Test Booking — powered by GYCO Consultants",
                "data_freshness": datetime.now().isoformat(),
            }
        except Exception as e:
            log.error("tool_error", tool="get_exam_booking_info", error=str(e))
            return {"error": "Failed to get exam booking info.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 2. get_current_offers
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    @log_search("get_current_offers")
    async def get_current_offers(
        destination_country: Optional[str] = None,
        offer_type: str = "all",
    ) -> dict[str, Any]:
        """Get current scholarship, admission, and exam discount offers from FindUni.
        Use when student asks about current deals, discounts, special offers, or promotions.
        Do not use for searching the main scholarship database.

        Returns active offers curated by GYCO Consultants with direct apply links.

        Args:
            destination_country: Optional filter by country, e.g. "australia", "uk".
            offer_type: One of "university_scholarship", "exam_discount", or "all" (default).
        """
        try:
            log.info("tool_call", tool="get_current_offers")

            offers = [o for o in _CURRENT_OFFERS if o.get("is_active")]

            # Filter by destination
            if destination_country:
                dest_lower = destination_country.lower().strip()
                offers = [o for o in offers if dest_lower in (o.get("destination", "").lower())]

            # Filter by type
            if offer_type != "all":
                offers = [o for o in offers if o.get("type") == offer_type]

            university_offers = [o for o in offers if o.get("type") == "university_scholarship"]
            exam_offers = [o for o in offers if o.get("type") == "exam_discount"]

            return {
                "university_scholarship_offers": university_offers,
                "exam_discount_offers": exam_offers,
                "total_offers": len(offers),
                "filters_applied": {
                    "destination_country": destination_country,
                    "offer_type": offer_type,
                },
                "note": "These are exclusive offers through FindUni/GYCO Consultants. Contact via WhatsApp for application assistance.",
                "contact": {
                    "whatsapp": "https://wa.link/68wkmn",
                    "phone": "01-4545747",
                },
                "source": "FindUni.online Offers — powered by GYCO Consultants",
                "data_freshness": datetime.now().isoformat(),
            }
        except Exception as e:
            log.error("tool_error", tool="get_current_offers", error=str(e))
            return {"error": "Failed to get current offers.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 3. get_ielts_class_info
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    @log_search("get_ielts_class_info")
    async def get_ielts_class_info() -> dict[str, Any]:
        """Get IELTS preparation class details from GYCO Consultants.
        Use when student asks about IELTS preparation classes, coaching, or tutoring in Nepal.
        Do not use for IELTS test booking or score requirements.

        Returns class format, pricing, schedule, and what's included.

        No arguments required.
        """
        try:
            log.info("tool_call", tool="get_ielts_class_info")

            return {
                "class_details": _IELTS_CLASS,
                "highlights": [
                    f"Small class — maximum {_IELTS_CLASS['max_students']} students only",
                    f"Try before you commit — attend 2 days for just NPR {_IELTS_CLASS['pricing']['initial_payment']:,}",
                    f"Total course cost: NPR {_IELTS_CLASS['pricing']['total']:,} for 4 weeks",
                    "Expert instructors from GYCO Consultants",
                    "Rolling enrollment — start any week",
                ],
                "source": "FindUni.online IELTS Class — powered by GYCO Consultants",
                "data_freshness": datetime.now().isoformat(),
            }
        except Exception as e:
            log.error("tool_error", tool="get_ielts_class_info", error=str(e))
            return {"error": "Failed to get IELTS class info.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 4. get_banking_partners
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    @log_search("get_banking_partners")
    async def get_banking_partners() -> dict[str, Any]:
        """Get education loan banking partner details for Nepali students.
        Use when student asks about education loans, bank loan contacts, or financing options in Nepal.
        Do not use for calculating loan amounts.

        Returns partner banks with branch details and direct contact information.

        No arguments required.
        """
        try:
            log.info("tool_call", tool="get_banking_partners")

            return {
                "banking_partners": _BANKING_PARTNERS,
                "total_partners": len(_BANKING_PARTNERS),
                "loan_tips": [
                    "Apply for education loan at least 6-8 weeks before visa application",
                    "Loan sanction letter is accepted as financial evidence for visa",
                    "Most banks require property collateral for education loans",
                    "Interest rates for education loans in Nepal range from 8-12%",
                    "Some banks offer moratorium period — no EMI during study period",
                    "Compare offers from multiple banks before deciding",
                    "Ensure the sanction letter clearly states the loan amount and purpose (education)",
                ],
                "note": "These are FindUni/GYCO verified banking partners. Contact them directly for education loan processing.",
                "source": "FindUni.online Banking Partners — powered by GYCO Consultants",
                "data_freshness": datetime.now().isoformat(),
            }
        except Exception as e:
            log.error("tool_error", tool="get_banking_partners", error=str(e))
            return {"error": "Failed to get banking partners.", "error_type": "tool_error"}
