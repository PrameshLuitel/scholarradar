# ScholarRadar: AI-Ready Course Data for British Council

**Pramesh Luitel · [skolr.xyz](https://skolr.xyz) · [Video Demo](https://www.loom.com/share/3d4ce784a751464c83592294767f982a)**

---

## Students stopped Googling. British Council has no answer yet.

Students ask ChatGPT and Claude where to study abroad. The AI gives recommendations. None of the links point to British Council. None point to any education provider. They point to Wikipedia, random blogs, outdated forums.

I built a fix. It works today. IDP knows about it and confirmed they have something similar in their pipeline. British Council can ship first.

---

## The fix: an MCP server

MCP (Model Context Protocol) is how AI tools connect to live data. Anthropic created the standard. OpenAI adopted it. Google is adopting it. An MCP server feeds structured data to AI models so their answers contain your links, your courses, your scholarships.

I built one. It runs at [skolr.xyz/mcp](https://skolr.xyz/mcp). Claude can connect to it right now.

A student asks Claude: *"Best masters in data science in the UK under £20k?"*

Without ScholarRadar, Claude guesses from training data. With ScholarRadar, Claude queries a live database of 50,000+ courses, checks scholarship eligibility, calculates costs, and returns an answer where every link routes to the provider.

---

## What the server exposes

Seven tool modules. Each one handles a domain an AI model can call:

| Tool | Data |
|------|------|
| Courses | 50,000+ listings across 6 countries, with IELTS requirements and tuition fees |
| Scholarships | 6,000+ scholarships with eligibility matching by nationality, subject, and deadline |
| Universities | 1,185 institution profiles with rankings and acceptance data |
| Visa | 60 nationality-destination combinations with processing times and financial thresholds |
| Cost of Living | 23 cities with rent, food, transport, and part-time wage data |
| IELTS Prep | Score analysis and improvement impact projections |
| Study Abroad Planner | Combines all tools into a single personalised plan: courses, costs, scholarships, visa, timeline |

The planner tool is the one that matters most. A student gives their nationality, qualification, budget, subject, and preferred countries. The server returns a structured plan covering matched courses, eligible scholarships, a financial breakdown by city, visa risk assessment, and a month-by-month application timeline. One call. Full counselling session.

---

## The data pipeline

Seven scrapers run daily through GitHub Actions. They pull from public education databases, clean the data, and upsert into a Supabase (PostgreSQL) database. Stale records get deactivated. No duplicates. The whole system runs without human input.

A live analytics dashboard at [skolr.xyz/dashboard](https://skolr.xyz/dashboard) tracks every query: which nationalities search most, which subjects trend, which destinations lead, and which searches return zero results. That last metric is the most valuable. It shows you where student demand exists but your catalog has gaps.

Weekly reports generate and deliver via webhook.

---

## IDP is building one. You can ship first.

I pitched this to IDP's Chief Digital Officer and Head of SEO. Neil Pearson directed me to Joel Knight. Joel reviewed my demo and said:

> "Our challenge isn't building an MCP server, that's pretty easy and in our pipeline."

IDP confirmed three things: they see MCP as a channel worth owning, they plan to build one, and they haven't shipped yet.

British Council can move faster. The architecture is built. The data pipeline works. The server is live. Swapping the data source to British Council's catalog is engineering work, not research.

The company that ships an education MCP first sets the default. AI platforms adopt what exists. Students build habits around tools that work. Second place in this race gets significantly less.

---

## Distribution paths

MCP servers gain users through three channels:

1. **Claude Apps** are live now. A published ScholarRadar app would surface to Claude's user base when students ask education questions.
2. **ChatGPT's Apps program** follows the same model. Large education brands can opt in.
3. **Organic social.** British Council already runs education content on Instagram, TikTok, and YouTube. Direct those audiences to AI tools backed by British Council data, and you own both the content layer and the recommendation layer.

---

## What I built, specifically

- Python MCP server (FastMCP + FastAPI), deployed on Render
- 7 async scrapers with rate limiting, checkpointing, and crash recovery
- Supabase database with upsert logic and active/inactive record management
- Analytics instrumentation logging every tool call with nationality, destination, subject, response time, and result count
- React frontend at skolr.xyz with privacy policy, terms, and compliance pages
- Automated daily scraping via GitHub Actions
- Weekly analytics reports via webhook

Live links:
- MCP endpoint: [skolr.xyz/mcp](https://skolr.xyz/mcp)
- Dashboard: [skolr.xyz/dashboard](https://skolr.xyz/dashboard)
- Demo video: [Loom](https://www.loom.com/share/3d4ce784a751464c83592294767f982a)

---

## About me

Pramesh Luitel. Incoming student at Bond University, Gold Coast. I built ScholarRadar from scratch and pitched it to IDP's senior leadership before writing a single line of this document. I build things that work, then find the people who need them.

**Contact:** [LinkedIn](https://www.linkedin.com/in/prameshluitel) · pramesh@skolr.xyz
