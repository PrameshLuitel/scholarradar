"""
FindUni.online Genuine Student (GS) MCP tools — 2 tools:
  1. get_gs_document_checklist — Complete GS document checklist by income type
  2. generate_gs_statement_guide — GS statement writing guidance

Full document database embedded directly from FindUni.online GS Cheatsheet.
Powered by GYCO Consultants / FindUni.online.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any, Optional

import structlog
from fastmcp import FastMCP

log = structlog.get_logger("mcp_server.tools.finduni_gs")

# ══════════════════════════════════════════════════════════════════════════
# GS DOCUMENT DATABASE — Complete checklist from FindUni.online
# ══════════════════════════════════════════════════════════════════════════

_GENERAL_DOCUMENTS = [
    {"document": "Valid Passport", "description": "Must be valid for 6+ months beyond intended stay. All pages scanned.", "required": True},
    {"document": "Citizenship Certificate (Nagarikta)", "description": "Nepali citizenship certificate — original and notarized copy.", "required": True},
    {"document": "Academic Transcripts", "description": "All academic records from SLC/SEE to latest qualification. Certified copies.", "required": True},
    {"document": "Character Certificates", "description": "From all institutions attended.", "required": True},
    {"document": "Offer Letter / CoE", "description": "Confirmation of Enrolment from CRICOS-registered provider.", "required": True},
    {"document": "OSHC Policy", "description": "Overseas Student Health Cover for the duration of your visa.", "required": True},
    {"document": "Health Examination", "description": "From Bupa-approved panel physician. Complete before visa lodgement.", "required": True},
    {"document": "Police Clearance Certificate", "description": "From Nepal Police — must be recent (within 6 months).", "required": True},
    {"document": "Passport-size Photographs", "description": "Recent photos meeting Australian visa specifications.", "required": True},
    {"document": "Birth Certificate", "description": "Original or notarized copy.", "required": True},
    {"document": "Relationship Certificates", "description": "If sponsored by family — showing relationship to sponsor.", "required": True},
    {"document": "Statement of Purpose (SOP)", "description": "Why this course, why this university, why Australia, career plans. This is part of your GS statement.", "required": True},
]

_WARD_DOCUMENTS = [
    {"document": "Ward Recommendation Letter", "description": "Recommendation letter from your local ward office.", "required": True},
    {"document": "Ward Verified Copies", "description": "Ward office verified copies of key documents.", "required": True},
    {"document": "Ward Office Letter", "description": "General verification letter from ward office confirming residency.", "required": True},
    {"document": "Land Ownership Certificate (Lalpurja)", "description": "If claiming property — ward office verified copy of land certificate.", "required": False},
    {"document": "House Ownership Certificate", "description": "If applicable — ward verified.", "required": False},
    {"document": "Business Registration (Ward level)", "description": "If self-employed — ward level business verification.", "required": False},
]

_INCOME_DOCUMENTS = {
    "salaried": {
        "label": "Salaried Income",
        "documents": [
            {"document": "Salary Certificate", "description": "Official salary certificate from employer on company letterhead with designation, salary breakdown, and joining date.", "required": True},
            {"document": "Appointment Letter", "description": "Original job appointment/offer letter.", "required": True},
            {"document": "Bank Statements (12 months)", "description": "Salary credit bank statements for the last 12 months showing regular salary deposits.", "required": True},
            {"document": "Tax Clearance Certificate", "description": "Annual tax clearance from IRD (Inland Revenue Department).", "required": True},
            {"document": "PAN Card", "description": "Permanent Account Number card.", "required": True},
            {"document": "Provident Fund Statement", "description": "EPF/PF statement if applicable.", "required": False},
            {"document": "Pay Slips (6 months)", "description": "Recent monthly pay slips.", "required": False},
            {"document": "Employment ID Card", "description": "Company-issued ID card copy.", "required": False},
        ],
    },
    "pension": {
        "label": "Pension Income",
        "documents": [
            {"document": "Pension Certificate", "description": "Official pension/retirement certificate from employer or government body.", "required": True},
            {"document": "Pension Book / ID", "description": "Pension identification document.", "required": True},
            {"document": "Bank Statements (12 months)", "description": "Showing regular pension credit.", "required": True},
            {"document": "Tax Clearance Certificate", "description": "If applicable on pension income.", "required": False},
            {"document": "Retirement Letter", "description": "Official retirement/superannuation letter.", "required": False},
        ],
    },
    "rental": {
        "label": "Rental Income",
        "documents": [
            {"document": "Rental Agreement", "description": "Current rental/lease agreement between landlord and tenant.", "required": True},
            {"document": "Land/House Ownership Certificate", "description": "Lalpurja or house ownership proving you own the rented property.", "required": True},
            {"document": "Tenant Verification", "description": "Ward office tenant verification document.", "required": True},
            {"document": "Bank Statements (12 months)", "description": "Showing regular rental income deposits.", "required": True},
            {"document": "TDS Certificate", "description": "Tax Deducted at Source certificate for rental income.", "required": False},
            {"document": "Property Valuation", "description": "Recent property valuation report.", "required": False},
        ],
    },
    "land_lease": {
        "label": "Land Lease Income",
        "documents": [
            {"document": "Land Lease Agreement", "description": "Formal lease agreement for agricultural or commercial land.", "required": True},
            {"document": "Land Ownership Certificate (Lalpurja)", "description": "Original or certified copy of land ownership.", "required": True},
            {"document": "Bank Statements (12 months)", "description": "Showing lease income deposits.", "required": True},
            {"document": "Ward Verification of Lease", "description": "Ward office verification of the lease arrangement.", "required": True},
            {"document": "Tax Clearance on Lease Income", "description": "Tax cleared on lease income.", "required": False},
        ],
    },
    "business_full": {
        "label": "Business Income (Full Ownership)",
        "documents": [
            {"document": "Company Registration Certificate", "description": "Registration from Office of Company Registrar or Cottage Industry.", "required": True},
            {"document": "PAN/VAT Registration", "description": "PAN certificate and VAT registration if applicable.", "required": True},
            {"document": "Audit Report (2 years)", "description": "Audited financial statements for the last 2 fiscal years.", "required": True},
            {"document": "Tax Clearance Certificate (2 years)", "description": "Tax clearance from IRD for last 2 fiscal years.", "required": True},
            {"document": "Bank Statements (12 months)", "description": "Business account bank statements showing turnover.", "required": True},
            {"document": "Company Profile", "description": "Brief company profile with nature of business, employees, and turnover.", "required": True},
            {"document": "Business License / Renewal", "description": "Current year business license and renewals.", "required": True},
            {"document": "Profit & Loss Statement", "description": "Latest P&L statement certified by auditor.", "required": False},
            {"document": "Board Resolution (if company)", "description": "Board resolution authorizing financial sponsorship.", "required": False},
            {"document": "Utility Bills", "description": "Business premises utility bills confirming active operation.", "required": False},
        ],
    },
    "business_partial": {
        "label": "Business Income (Partnership/Partial Ownership)",
        "documents": [
            {"document": "Partnership Deed", "description": "Registered partnership agreement showing ownership percentage.", "required": True},
            {"document": "Profit Sharing Agreement", "description": "Agreement showing how profits are distributed.", "required": True},
            {"document": "Company Registration Certificate", "description": "Firm/company registration.", "required": True},
            {"document": "Audit Report (2 years)", "description": "Audited financial statements showing partner's share.", "required": True},
            {"document": "Tax Clearance Certificate", "description": "Individual and business tax clearance.", "required": True},
            {"document": "Bank Statements (12 months)", "description": "Personal and business bank statements.", "required": True},
            {"document": "Share Certificate", "description": "If company — share certificate showing ownership.", "required": False},
        ],
    },
    "foreign": {
        "label": "Foreign Income (Remittance)",
        "documents": [
            {"document": "Employment Contract (Abroad)", "description": "Current employment contract from foreign employer.", "required": True},
            {"document": "Salary Certificate (Abroad)", "description": "Salary certificate from foreign employer.", "required": True},
            {"document": "Remittance Receipts (12 months)", "description": "Remittance receipts showing regular transfers to Nepal.", "required": True},
            {"document": "Bank Statements (12 months)", "description": "Nepal bank statements showing remittance credits.", "required": True},
            {"document": "Foreign Tax Returns", "description": "Tax returns or certificates from the country of employment.", "required": False},
            {"document": "Work Permit / Visa (Abroad)", "description": "Valid work permit or employment visa from abroad.", "required": False},
        ],
    },
    "vehicle": {
        "label": "Vehicle Income",
        "documents": [
            {"document": "Vehicle Registration (Bluebook)", "description": "Vehicle registration certificate (Bluebook).", "required": True},
            {"document": "Route Permit", "description": "Route permit if public transport vehicle.", "required": True},
            {"document": "Income Records", "description": "Income records from vehicle operation — bank statements or account books.", "required": True},
            {"document": "Tax Clearance Certificate", "description": "Tax cleared on vehicle income.", "required": True},
            {"document": "Insurance Certificate", "description": "Vehicle insurance showing active coverage.", "required": False},
        ],
    },
}

_FUND_SOURCE_DOCUMENTS = {
    "education_loan": {
        "label": "Education Loan",
        "documents": [
            {"document": "Loan Sanction Letter", "description": "Bank-issued loan sanction/approval letter showing approved amount.", "required": True},
            {"document": "Loan Agreement", "description": "Signed loan agreement between borrower and bank.", "required": True},
            {"document": "Repayment Schedule", "description": "EMI/repayment schedule from the bank.", "required": True},
            {"document": "Collateral Documents", "description": "Property or other collateral documents if secured loan.", "required": False},
            {"document": "Guarantor Documents", "description": "Guarantor's income and identity documents if required.", "required": False},
            {"document": "Loan Disbursement Proof", "description": "Bank statement showing loan disbursement.", "required": False},
        ],
    },
    "savings": {
        "label": "Personal/Family Savings",
        "documents": [
            {"document": "Bank Statements (6+ months)", "description": "Bank statements showing consistent savings for at least 6 months. Avoid sudden large deposits.", "required": True},
            {"document": "Fixed Deposit (FD) Certificates", "description": "FD certificates showing long-term savings.", "required": True},
            {"document": "Source of Savings Explanation", "description": "Letter explaining how savings were accumulated over time.", "required": True},
            {"document": "CA-Certified Financial Summary", "description": "Chartered Accountant certified summary of total financial position.", "required": False},
            {"document": "Investment Certificates", "description": "Share certificates, mutual fund statements, or other investments.", "required": False},
        ],
    },
}


from src.utils.analytics import log_search


def register_tools(mcp: FastMCP):
    """Register all 2 FindUni GS tools."""

    # ────────────────────────────────────────────────────────────────────
    # 1. get_gs_document_checklist
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    @log_search("get_gs_document_checklist")
    async def get_gs_document_checklist(
        income_types: str = "salaried",
        fund_sources: str = "savings",
        include_ward_docs: bool = True,
    ) -> dict[str, Any]:
        """Generate a complete GS (Genuine Student) document checklist for Australian student visa.
        Use when student asks what documents they need, GS documentation, or visa paperwork.
        Do not use for calculating financial amounts or visa prediction.

        Based on FindUni.online GS Cheatsheet — the most comprehensive GS document guide
        for Nepali students. Powered by GYCO Consultants.

        Args:
            income_types: Comma-separated income types of sponsor(s). Options: "salaried", "pension", "rental", "land_lease", "business_full", "business_partial", "foreign", "vehicle". E.g. "salaried,rental".
            fund_sources: Comma-separated fund sources. Options: "education_loan", "savings". E.g. "education_loan,savings".
            include_ward_docs: Include ward office documents (default True for Nepali applicants).
        """
        try:
            log.info("tool_call", tool="get_gs_document_checklist")

            income_list = [t.strip().lower() for t in income_types.split(",") if t.strip()]
            fund_list = [f.strip().lower() for f in fund_sources.split(",") if f.strip()]

            checklist = {
                "general_documents": {
                    "label": "General Documents (Required for All Applicants)",
                    "documents": list(_GENERAL_DOCUMENTS),
                    "count": len(_GENERAL_DOCUMENTS),
                },
            }

            if include_ward_docs:
                checklist["ward_documents"] = {
                    "label": "Ward Office Documents",
                    "documents": list(_WARD_DOCUMENTS),
                    "count": len(_WARD_DOCUMENTS),
                }

            # Income documents
            income_sections = {}
            for income_type in income_list:
                if income_type in _INCOME_DOCUMENTS:
                    section = _INCOME_DOCUMENTS[income_type]
                    income_sections[income_type] = {
                        "label": section["label"],
                        "documents": list(section["documents"]),
                        "count": len(section["documents"]),
                    }
                else:
                    income_sections[income_type] = {
                        "label": income_type,
                        "documents": [],
                        "count": 0,
                        "warning": f"Unknown income type: '{income_type}'. Valid options: salaried, pension, rental, land_lease, business_full, business_partial, foreign, vehicle",
                    }
            checklist["income_documents"] = income_sections

            # Fund source documents
            fund_sections = {}
            for fund_source in fund_list:
                if fund_source in _FUND_SOURCE_DOCUMENTS:
                    section = _FUND_SOURCE_DOCUMENTS[fund_source]
                    fund_sections[fund_source] = {
                        "label": section["label"],
                        "documents": list(section["documents"]),
                        "count": len(section["documents"]),
                    }
                else:
                    fund_sections[fund_source] = {
                        "label": fund_source,
                        "documents": [],
                        "count": 0,
                        "warning": f"Unknown fund source: '{fund_source}'. Valid options: education_loan, savings",
                    }
            checklist["fund_source_documents"] = fund_sections

            # Count totals
            total_required = 0
            total_recommended = 0
            for section in checklist.values():
                if isinstance(section, dict) and "documents" in section:
                    for doc in section.get("documents", []):
                        if doc.get("required"):
                            total_required += 1
                        else:
                            total_recommended += 1
                elif isinstance(section, dict):
                    for sub_section in section.values():
                        if isinstance(sub_section, dict):
                            for doc in sub_section.get("documents", []):
                                if doc.get("required"):
                                    total_required += 1
                                else:
                                    total_recommended += 1

            return {
                "checklist": checklist,
                "summary": {
                    "total_required_documents": total_required,
                    "total_recommended_documents": total_recommended,
                    "total_documents": total_required + total_recommended,
                    "income_types_selected": income_list,
                    "fund_sources_selected": fund_list,
                },
                "preparation_tips": [
                    "Start gathering documents at least 8-10 weeks before visa application",
                    "All non-English documents must have certified translations",
                    "Get documents notarized/certified by a licensed notary",
                    "Bank statements should show funds held for 6+ months — avoid sudden deposits",
                    "CA-certified financial documents carry more weight than self-declarations",
                    "Keep both originals and color scans of every document",
                    "Ward office documents must be recent — within 3-6 months",
                    "Audit reports should cover the last 2 complete fiscal years",
                ],
                "common_mistakes": [
                    "Submitting bank statements with recent large deposits — looks fabricated",
                    "Missing tax clearance certificates — major red flag",
                    "Generic SOP/GTE statement — must be specific to your course and career path",
                    "Not certifying translated documents",
                    "Incomplete financial documentation — partial evidence is worse than comprehensive",
                    "Not including ward-level documents for property claims",
                ],
                "source": "FindUni.online GS Cheatsheet — powered by GYCO Consultants",
                "contact": {
                    "phone": "01-4545747",
                    "email": "hello@gyconepal.com",
                    "whatsapp": "https://wa.link/68wkmn",
                },
                "data_freshness": datetime.now().isoformat(),
            }
        except Exception as e:
            log.error("tool_error", tool="get_gs_document_checklist", error=str(e))
            return {"error": "Failed to generate GS checklist.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 2. generate_gs_statement_guide
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    @log_search("generate_gs_statement_guide")
    async def generate_gs_statement_guide(
        course_name: str,
        university_name: str,
        student_background: str,
        career_goal: str = "",
        why_australia: str = "",
        why_this_course: str = "",
    ) -> dict[str, Any]:
        """Generate a structured guide for writing a Genuine Student (GS) statement.
        Use when student asks for help writing their GTE/GS statement, SOP, or visa personal statement.
        Do not use for document checklists or financial calculations.

        Provides section-by-section guidance, common mistakes, red flags to avoid,
        and expert tips from GYCO Consultants' experience with Australian visa applications.

        Args:
            course_name: The course the student is applying for, e.g. "Master of Data Science".
            university_name: The university, e.g. "University of Melbourne".
            student_background: Brief background, e.g. "Bachelors in IT from Tribhuvan University, 3 years work experience at Deerwalk".
            career_goal: What they plan to do after graduation, e.g. "data engineer at a Nepali fintech startup".
            why_australia: Why they chose Australia over other countries.
            why_this_course: Why this specific course and university.
        """
        try:
            log.info("tool_call", tool="generate_gs_statement_guide")

            sections = [
                {
                    "section_number": 1,
                    "title": "Personal Introduction & Background",
                    "what_to_include": [
                        "Your full name, age, and nationality",
                        "Current education level and institution",
                        "Brief work experience summary (if any)",
                        "Family background — parents' occupations, siblings",
                        "What motivated you to pursue further education abroad",
                    ],
                    "example_opening": f"I am [Name], a {student_background}. I am applying for {course_name} at {university_name}.",
                    "tips": [
                        "Keep it concise — 2-3 paragraphs maximum",
                        "Show you are grounded in Nepal with strong ties",
                        "Mention family responsibilities and connections",
                    ],
                },
                {
                    "section_number": 2,
                    "title": "Why This Course?",
                    "what_to_include": [
                        f"Specific reasons for choosing {course_name}",
                        "How it connects to your previous education",
                        "Specific subjects/modules that interest you and why",
                        "Skills gap this course fills",
                        "Research you've done about the curriculum",
                    ],
                    "why_this_course_input": why_this_course if why_this_course else "Student should explain specific course features that align with their career goals",
                    "tips": [
                        "Name specific subjects from the course structure",
                        "Show logical progression from your current qualification",
                        "Explain why this course is not available (at same quality) in Nepal",
                        "Reference course accreditations or industry partnerships",
                    ],
                },
                {
                    "section_number": 3,
                    "title": f"Why {university_name}?",
                    "what_to_include": [
                        f"Specific features of {university_name} that attracted you",
                        "Rankings, research output, industry connections",
                        "Campus facilities, student support services",
                        "Location advantages (city, networking opportunities)",
                        "Alumni success stories if known",
                    ],
                    "tips": [
                        "Be specific — generic reasons like 'good ranking' are weak",
                        "Mention specific research groups, labs, or professors",
                        "Reference the university's industry partnership or internship programs",
                        "Show you've genuinely researched this university",
                    ],
                },
                {
                    "section_number": 4,
                    "title": "Why Australia?",
                    "what_to_include": [
                        "Quality of education system (CRICOS, ESOS Act protections)",
                        "Post-study work rights (485 visa)",
                        "Safety, multicultural environment",
                        "Comparison with other countries you considered",
                        "Why Australia is better for your specific field",
                    ],
                    "why_australia_input": why_australia if why_australia else "Student should explain why Australia specifically over UK, USA, Canada, etc.",
                    "tips": [
                        "Don't just say 'Australia has good universities' — everyone says that",
                        "Compare with at least one other destination and explain why AU wins",
                        "Mention specific AU industry strengths relevant to your course",
                        "Reference ESOS Act and CRICOS framework as quality assurance",
                    ],
                },
                {
                    "section_number": 5,
                    "title": "Career Plans & Return to Nepal",
                    "what_to_include": [
                        f"Specific career goal: {career_goal or 'Must specify concrete job/role in Nepal'}",
                        "Name specific Nepali companies or sectors you'd work in",
                        "How this course prepares you for that specific career",
                        "Nepal's market demand for your skills (cite specific examples)",
                        "Long-term career progression in Nepal",
                        "Why return to Nepal is beneficial (family, opportunities, patriotism)",
                    ],
                    "tips": [
                        "THIS IS THE MOST CRITICAL SECTION — DHA cares most about intent to return",
                        "Name 2-3 specific Nepali employers (e.g., 'F1Soft, Leapfrog Technology, Deerhold')",
                        "Reference Nepal's growing sectors (IT, hydropower, tourism, banking)",
                        "Show concrete knowledge of Nepal's job market in your field",
                        "Mention salary expectations and career growth trajectory in Nepal",
                        "If family has business — explain how your skills apply to the business",
                    ],
                },
                {
                    "section_number": 6,
                    "title": "Financial Capacity",
                    "what_to_include": [
                        "Summary of financial arrangements (savings, loans, sponsors)",
                        "How funds have been accumulated (timeline)",
                        "Who is sponsoring and their income source",
                        "Proof that funds are genuine and sufficient",
                    ],
                    "tips": [
                        "Mirror what your financial documents show — don't contradict",
                        "Explain the source of funds clearly (e.g., 'father's 20-year salary savings')",
                        "If education loan — mention the bank, amount, and repayment plan",
                        "Show funds have been building over time, not sudden deposits",
                    ],
                },
                {
                    "section_number": 7,
                    "title": "Study Gap Explanation (if applicable)",
                    "what_to_include": [
                        "What you did during the gap (work, preparation, family)",
                        "How the gap prepared you for this course",
                        "Why you're applying now specifically",
                        "Continuous professional development during the gap",
                    ],
                    "tips": [
                        "Only include this section if you have a gap of 2+ years",
                        "Frame the gap positively — work experience, skill building, career clarity",
                        "Never leave the gap unexplained — that's a red flag",
                    ],
                },
            ]

            red_flags = [
                "Generic statements that could apply to any course or university",
                "No mention of specific career plans in home country",
                "Emphasizing post-study work rights or PR pathway — screams migration intent",
                "Mentioning family or friends already in Australia too prominently",
                "Contradictions between SOP and financial documents",
                "Copy-pasted templates — DHA officers can spot these instantly",
                "Choosing a low-cost regional provider for a course available at a metro university",
                "Course downgrade — e.g., Masters holder applying for a Diploma",
                "No research about the specific course curriculum",
                "Mentioning multiple previous visa refusals without adequate explanation",
            ]

            common_refusal_reasons = [
                "Weak or generic GTE/GS statement — most common reason for Nepali students",
                "Fabricated or recently deposited financial evidence — DHA cross-checks",
                "No clear reason to return to Nepal after studies",
                "Unexplained study gap of 5+ years",
                "Course misaligned with background (e.g., IT graduate applying for hospitality diploma)",
                "Choosing the cheapest possible provider — migration intent signal",
                "Previous overstay or visa breach not adequately addressed",
                "Insufficient financial documentation — partial evidence raises suspicion",
            ]

            return {
                "guide": {
                    "course": course_name,
                    "university": university_name,
                    "sections": sections,
                },
                "red_flags_to_avoid": red_flags,
                "common_refusal_reasons": common_refusal_reasons,
                "formatting_guidelines": {
                    "word_count": "800-1200 words (concise but comprehensive)",
                    "format": "Clear paragraphs with section headings",
                    "tone": "Professional, specific, genuine — not salesy or emotional",
                    "language": "Clear English, grammatically correct, avoid flowery language",
                    "structure": "Follow the 7 sections above in order",
                },
                "expert_tips": [
                    "Write it yourself — DHA can tell if an agent wrote it for you",
                    "Be specific — generic statements are the #1 reason for refusal",
                    "Show GENUINE intent — why you actually want this education, not just talk about Australia's greatness",
                    "Your GS must align perfectly with your documents — contradictions are fatal",
                    "Have someone proofread for grammar and clarity",
                    "Update it for each application — don't reuse the same statement",
                    "Research the actual course curriculum and mention specific units/subjects",
                    "If you have a previous refusal, address it head-on in a separate section",
                ],
                "gyco_advice": "GYCO Consultants recommends having your GS statement reviewed by a qualified counsellor before submission. "
                               "Our team has helped thousands of Nepali students craft successful applications. "
                               "Contact us at 01-4545747 or hello@gyconepal.com for a free review.",
                "source": "FindUni.online GS Cheatsheet — powered by GYCO Consultants",
                "contact": {
                    "phone": "01-4545747",
                    "email": "hello@gyconepal.com",
                    "whatsapp": "https://wa.link/68wkmn",
                },
                "data_freshness": datetime.now().isoformat(),
            }
        except Exception as e:
            log.error("tool_error", tool="generate_gs_statement_guide", error=str(e))
            return {"error": "Failed to generate GS guide.", "error_type": "tool_error"}
