"""
Public-facing analytics dashboard — no API key required.
Shows IDP leadership the live usage data from ScholarRadar MCP.
"""

import os
from collections import Counter
from datetime import datetime, timedelta
from typing import Any

from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from structlog import get_logger

from src.database.client import get_db

log = get_logger("api.dashboard")

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


# ── JSON Data Endpoint ─────────────────────────────────────────────────────

@router.get("/data")
async def dashboard_data() -> dict[str, Any]:
    """Public JSON endpoint with aggregated analytics — no auth required."""
    db = get_db()
    now = datetime.utcnow()

    try:
        today_iso = (now - timedelta(days=1)).isoformat()
        week_iso = (now - timedelta(days=7)).isoformat()
        month_iso = (now - timedelta(days=30)).isoformat()

        today_res = db.table("tool_call_logs").select("id", count="exact").gte("called_at", today_iso).execute()
        week_res = db.table("tool_call_logs").select("id", count="exact").gte("called_at", week_iso).execute()
        month_res = db.table("tool_call_logs").select("id", count="exact").gte("called_at", month_iso).execute()
        total_res = db.table("tool_call_logs").select("id", count="exact").execute()

        # Fetch recent 2000 rows for aggregation
        recent = db.table("tool_call_logs").select("*").order("called_at", desc=True).limit(2000).execute()
        rows = recent.data if recent and recent.data else []

        # Tool usage breakdown
        tools = Counter([r.get("tool_name") for r in rows if r.get("tool_name")])
        tool_breakdown = [{"tool": k, "calls": v} for k, v in tools.most_common()]

        # Top nationalities
        nats = Counter([r.get("nationality") for r in rows if r.get("nationality")])
        top_nationalities = [{"name": k, "count": v} for k, v in nats.most_common(10)]

        # Top destinations
        dests = Counter([r.get("destination_country") for r in rows if r.get("destination_country")])
        top_destinations = [{"name": k, "count": v} for k, v in dests.most_common(10)]

        # Top subjects
        subjects = Counter([r.get("subject") for r in rows if r.get("subject")])
        top_subjects = [{"name": k, "count": v} for k, v in subjects.most_common(10)]

        # Top universities searched
        unis = Counter([r.get("university_name") for r in rows if r.get("university_name")])
        top_universities = [{"name": k, "count": v} for k, v in unis.most_common(10)]

        # Zero result rate
        zero_count = sum(1 for r in rows if r.get("zero_results") is True)
        zero_rate = round((zero_count / len(rows) * 100), 1) if rows else 0

        # Average response time
        response_times = [r.get("response_time_ms") for r in rows if r.get("response_time_ms")]
        avg_response = round(sum(response_times) / len(response_times)) if response_times else 0

        # Recent 15 calls (for live feed)
        recent_calls = []
        for r in rows[:15]:
            recent_calls.append({
                "tool": r.get("tool_name"),
                "nationality": r.get("nationality"),
                "destination": r.get("destination_country"),
                "subject": r.get("subject"),
                "results": r.get("results_count", 0),
                "time_ms": r.get("response_time_ms"),
                "when": r.get("called_at"),
            })

        # Gap searches — top combos with zero results
        gap_rows = [r for r in rows if r.get("zero_results") is True]
        gap_combos = Counter()
        for r in gap_rows:
            nat = r.get("nationality") or "Any"
            dest = r.get("destination_country") or "Any"
            subj = r.get("subject") or "Any"
            if nat == "Any" and dest == "Any" and subj == "Any":
                continue
            gap_combos[f"{nat} → {dest} → {subj}"] += 1
        top_gaps = [{"query": k, "count": v} for k, v in gap_combos.most_common(10)]

        return {
            "generated_at": now.isoformat(),
            "total_calls": {
                "today": today_res.count if today_res else 0,
                "week": week_res.count if week_res else 0,
                "month": month_res.count if month_res else 0,
                "all_time": total_res.count if total_res else 0,
            },
            "tool_breakdown": tool_breakdown,
            "top_nationalities": top_nationalities,
            "top_destinations": top_destinations,
            "top_subjects": top_subjects,
            "top_universities": top_universities,
            "zero_result_rate": zero_rate,
            "avg_response_ms": avg_response,
            "recent_calls": recent_calls,
            "demand_gaps": top_gaps,
        }

    except Exception as e:
        log.error("dashboard_data_error", error=str(e))
        return {"error": "Failed to load dashboard data", "detail": str(e)}


# ── HTML Dashboard ─────────────────────────────────────────────────────────

@router.get("", response_class=HTMLResponse)
async def dashboard_page():
    """Render a beautiful, self-contained analytics dashboard — no auth."""
    return HTMLResponse(content=DASHBOARD_HTML)


DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ScholarRadar — Live Analytics Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#0f172a;--card:#1e293b;--border:#334155;
  --text:#f8fafc;--muted:#94a3b8;--accent:#0072bc;
  --accent2:#f7941e;--green:#00a651;--amber:#f59e0b;
  --red:#ef4444;--cyan:#0ea5e9;
}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;padding:0}
.header{background:linear-gradient(135deg,#003152 0%,#0072bc 50%,#0f172a 100%);
  padding:2.5rem 2rem;border-bottom:1px solid var(--border);text-align:center;position:relative;overflow:hidden}
.header::before{content:'';position:absolute;top:-50%;left:-50%;width:200%;height:200%;
  background:radial-gradient(circle at 30% 50%,rgba(0,114,188,0.1) 0%,transparent 50%);pointer-events:none}
.header h1{font-size:2rem;font-weight:800;
  background:linear-gradient(135deg,#ffffff,#cbd5e1);-webkit-background-clip:text;-webkit-text-fill-color:transparent;
  letter-spacing:-0.5px;margin-bottom:0.25rem;position:relative}
.header p{color:var(--muted);font-size:0.95rem;position:relative}
.header .badge{display:inline-flex;align-items:center;gap:6px;margin-top:0.75rem;padding:4px 12px;
  border-radius:20px;background:rgba(16,185,129,0.15);color:var(--green);font-size:0.75rem;font-weight:600;position:relative}
.header .badge::before{content:'';width:6px;height:6px;border-radius:50%;background:var(--green);
  animation:pulse 2s ease-in-out infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.3}}
.container{max-width:1280px;margin:0 auto;padding:1.5rem}
.stats-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1rem;margin-bottom:1.5rem}
.stat-card{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:1.25rem;
  text-align:center;transition:transform 0.2s,border-color 0.2s}
.stat-card:hover{transform:translateY(-2px);border-color:var(--accent)}
.stat-card .label{font-size:0.7rem;text-transform:uppercase;letter-spacing:1.5px;color:var(--muted);margin-bottom:0.5rem}
.stat-card .value{font-size:2rem;font-weight:800;
  background:linear-gradient(135deg,#818cf8,#c084fc);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.stat-card .sub{font-size:0.75rem;color:var(--muted);margin-top:0.25rem}
.charts-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(380px,1fr));gap:1rem;margin-bottom:1.5rem}
.chart-card{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:1.5rem}
.chart-card h3{font-size:0.85rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;
  color:var(--muted);margin-bottom:1rem;display:flex;align-items:center;gap:8px}
.chart-card h3 span{font-size:1rem}
.bar-row{display:flex;align-items:center;gap:10px;margin-bottom:8px}
.bar-label{font-size:0.8rem;color:var(--text);width:140px;text-align:right;flex-shrink:0;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.bar-track{flex:1;height:24px;background:#1e293b;border-radius:6px;overflow:hidden;position:relative}
.bar-fill{height:100%;border-radius:6px;transition:width 1s ease;position:relative;min-width:2px}
.bar-fill.purple{background:linear-gradient(90deg,var(--accent),#3b82f6)}
.bar-fill.cyan{background:linear-gradient(90deg,var(--accent2),#fb923c)}
.bar-fill.green{background:linear-gradient(90deg,var(--green),#22c55e)}
.bar-fill.amber{background:linear-gradient(90deg,var(--amber),#fbbf24)}
.bar-fill.rose{background:linear-gradient(90deg,var(--red),#f87171)}
.bar-count{font-size:0.75rem;color:var(--muted);width:40px;text-align:right;flex-shrink:0}
.feed-table{width:100%;border-collapse:collapse}
.feed-table th{font-size:0.65rem;text-transform:uppercase;letter-spacing:1px;color:var(--muted);
  text-align:left;padding:8px 10px;border-bottom:1px solid var(--border)}
.feed-table td{font-size:0.8rem;padding:8px 10px;border-bottom:1px solid rgba(30,41,59,0.5);color:var(--text)}
.feed-table tr:hover td{background:rgba(99,102,241,0.05)}
.tag{display:inline-block;padding:2px 8px;border-radius:4px;font-size:0.7rem;font-weight:600}
.tag-tool{background:rgba(99,102,241,0.15);color:#818cf8}
.tag-zero{background:rgba(239,68,68,0.15);color:var(--red)}
.tag-ok{background:rgba(16,185,129,0.15);color:var(--green)}
.gap-item{display:flex;justify-content:space-between;align-items:center;padding:8px 0;
  border-bottom:1px solid rgba(30,41,59,0.5);font-size:0.8rem}
.gap-item:last-child{border-bottom:none}
.gap-item .q{color:var(--text)}
.gap-item .c{color:var(--amber);font-weight:700}
.footer{text-align:center;padding:2rem;color:var(--muted);font-size:0.75rem}
.footer a{color:var(--accent);text-decoration:none}
.loading{display:flex;justify-content:center;align-items:center;min-height:60vh;font-size:1.2rem;color:var(--muted)}
.loading .spinner{width:32px;height:32px;border:3px solid var(--border);border-top-color:var(--accent);
  border-radius:50%;animation:spin 0.8s linear infinite;margin-right:12px}
@keyframes spin{to{transform:rotate(360deg)}}
.idp-callout{background:linear-gradient(135deg,rgba(99,102,241,0.1),rgba(139,92,246,0.1));
  border:1px solid rgba(99,102,241,0.3);border-radius:12px;padding:1.25rem;text-align:center;margin-bottom:1.5rem}
.idp-callout p{font-size:0.85rem;color:var(--text);line-height:1.6}
.idp-callout strong{color:#a5b4fc}
</style>
</head>
<body>

<div class="header">
  <h1>📡 ScholarRadar — Live Analytics</h1>
  <p>Real-time MCP tool usage data from AI-powered student queries</p>
  <div class="badge">● LIVE — Connected to Production</div>
</div>

<div class="container" id="app">
  <div class="loading" id="loader">
    <div class="spinner"></div>
    Loading live data from ScholarRadar MCP...
  </div>
</div>

<div class="footer">
  <p>Built by <strong>Pramesh Luitel</strong> · ScholarRadar MCP · <a href="/mcp">Connect via MCP</a></p>
  <p style="margin-top:4px">Data sourced live from <strong>Supabase tool_call_logs</strong> via MCP instrumentation</p>
  <p style="margin-top:4px; opacity: 0.8; font-size: 0.65rem">All student leads are routed directly to <strong>idp.com</strong> domains</p>
</div>

<script>
async function loadDashboard() {
  try {
    const res = await fetch('/dashboard/data');
    const d = await res.json();
    if (d.error) { document.getElementById('loader').innerHTML = '<p>'+d.error+'</p>'; return; }
    render(d);
  } catch(e) {
    document.getElementById('loader').innerHTML = '<p>Failed to connect. Server may be starting up.</p>';
  }
}

function render(d) {
  const app = document.getElementById('app');
  const tc = d.total_calls || {};
  const maxTool = d.tool_breakdown && d.tool_breakdown.length ? d.tool_breakdown[0].calls : 1;
  const maxNat = d.top_nationalities && d.top_nationalities.length ? d.top_nationalities[0].count : 1;
  const maxDest = d.top_destinations && d.top_destinations.length ? d.top_destinations[0].count : 1;
  const maxSubj = d.top_subjects && d.top_subjects.length ? d.top_subjects[0].count : 1;

  app.innerHTML = `
    <div class="idp-callout">
      <p>This dashboard tracks <strong>every AI query</strong> processed by ScholarRadar MCP.
      Each query represents a student using AI to search for courses, scholarships, and study-abroad plans — 
      <strong>all routing directly to IDP.</strong></p>
    </div>

    <div class="stats-grid">
      <div class="stat-card">
        <div class="label">Total Calls (All Time)</div>
        <div class="value">${(tc.all_time||0).toLocaleString()}</div>
        <div class="sub">MCP tool invocations</div>
      </div>
      <div class="stat-card">
        <div class="label">Last 30 Days</div>
        <div class="value">${(tc.month||0).toLocaleString()}</div>
        <div class="sub">monthly active queries</div>
      </div>
      <div class="stat-card">
        <div class="label">Last 7 Days</div>
        <div class="value">${(tc.week||0).toLocaleString()}</div>
        <div class="sub">weekly queries</div>
      </div>
      <div class="stat-card">
        <div class="label">Last 24 Hours</div>
        <div class="value">${(tc.today||0).toLocaleString()}</div>
        <div class="sub">daily queries</div>
      </div>
      <div class="stat-card">
        <div class="label">Avg Response</div>
        <div class="value">${d.avg_response_ms||0}ms</div>
        <div class="sub">tool execution time</div>
      </div>
      <div class="stat-card">
        <div class="label">Zero-Result Rate</div>
        <div class="value">${d.zero_result_rate||0}%</div>
        <div class="sub">demand gap indicator</div>
      </div>
    </div>

    <div class="charts-grid">
      <div class="chart-card">
        <h3><span>🛠️</span> Tool Usage Breakdown</h3>
        ${(d.tool_breakdown||[]).map(t => `
          <div class="bar-row">
            <div class="bar-label">${formatToolName(t.tool)}</div>
            <div class="bar-track"><div class="bar-fill purple" style="width:${(t.calls/maxTool*100)}%"></div></div>
            <div class="bar-count">${t.calls}</div>
          </div>
        `).join('')}
      </div>

      <div class="chart-card">
        <h3><span>🌍</span> Top Student Nationalities</h3>
        ${(d.top_nationalities||[]).map(n => `
          <div class="bar-row">
            <div class="bar-label">${capitalize(n.name)}</div>
            <div class="bar-track"><div class="bar-fill cyan" style="width:${(n.count/maxNat*100)}%"></div></div>
            <div class="bar-count">${n.count}</div>
          </div>
        `).join('')}
      </div>

      <div class="chart-card">
        <h3><span>✈️</span> Top Destination Countries</h3>
        ${(d.top_destinations||[]).map(n => `
          <div class="bar-row">
            <div class="bar-label">${capitalize(n.name)}</div>
            <div class="bar-track"><div class="bar-fill green" style="width:${(n.count/maxDest*100)}%"></div></div>
            <div class="bar-count">${n.count}</div>
          </div>
        `).join('')}
      </div>

      <div class="chart-card">
        <h3><span>📚</span> Most Searched Subjects</h3>
        ${(d.top_subjects||[]).map(n => `
          <div class="bar-row">
            <div class="bar-label">${capitalize(n.name)}</div>
            <div class="bar-track"><div class="bar-fill amber" style="width:${(n.count/maxSubj*100)}%"></div></div>
            <div class="bar-count">${n.count}</div>
          </div>
        `).join('')}
      </div>
    </div>

    <div class="charts-grid">
      <div class="chart-card">
        <h3><span>📡</span> Live Feed — Recent Queries</h3>
        <div style="overflow-x:auto">
        <table class="feed-table">
          <thead><tr><th>Tool</th><th>Nationality</th><th>Destination</th><th>Subject</th><th>Results</th><th>Speed</th></tr></thead>
          <tbody>
            ${(d.recent_calls||[]).map(r => `
              <tr>
                <td><span class="tag tag-tool">${(r.tool||'—').replace(/_/g,' ')}</span></td>
                <td>${capitalize(r.nationality||'—')}</td>
                <td>${capitalize(r.destination||'—')}</td>
                <td>${r.subject||'—'}</td>
                <td><span class="tag ${r.results===0?'tag-zero':'tag-ok'}">${r.results}</span></td>
                <td>${r.time_ms?r.time_ms+'ms':'—'}</td>
              </tr>
            `).join('')}
          </tbody>
        </table>
        </div>
      </div>

      <div class="chart-card">
        <h3><span>🔴</span> Demand Gaps — Students Searched, Nothing Found</h3>
        <p style="font-size:0.75rem;color:#94a3b8;margin-bottom:12px">
          These represent unmet student demand — real searches with zero results.
          This is where IDP can expand coverage to capture more students.
        </p>
        ${(d.demand_gaps||[]).length === 0 ? '<p style="color:#94a3b8;font-size:0.85rem">No gap searches recorded yet.</p>' : ''}
        ${(d.demand_gaps||[]).map(g => `
          <div class="gap-item">
            <span class="q">${g.query}</span>
            <span class="c">${g.count}×</span>
          </div>
        `).join('')}
      </div>
    </div>
  `;
}

function formatToolName(name) {
  if (!name) return '—';
  return name.replace(/_/g, ' ').replace(/\\b\\w/g, l => l.toUpperCase());
}
function capitalize(s) {
  if (!s || s === '—') return s || '—';
  return s.charAt(0).toUpperCase() + s.slice(1);
}

loadDashboard();
// Auto-refresh every 60 seconds
setInterval(loadDashboard, 60000);
</script>
</body>
</html>"""
