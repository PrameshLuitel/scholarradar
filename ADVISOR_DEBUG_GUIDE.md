# FindUni AI Advisor - Debugging Guide

## What Was Fixed

### Issue 1: Advisor shows "loading" but no results appear
**Root Cause:** The complex AgentRunner system was failing silently without producing output.

**Solution:** Simplified to direct LLM streaming with pre-queried database results.

### Issue 2: Improved prompt for worldwide students
**Solution:** Complete rewrite of system prompt to be more personalized, honest, and actionable.

## Architecture (SIMPLIFIED)

```
Frontend (FindUni.jsx)
    ↓ POST /api/advisor/analyze
Backend (advisor.py)
    ↓ 1. Parse profile + CV
    ↓ 2. Query database (courses, scholarships, unis, visa, costs)
    ↓ 3. Send metadata/courses/scholarships events to frontend
    ↓ 4. Build comprehensive prompt with all data
    ↓ 5. Stream LLM response via Groq cascade
Frontend receives:
    - metadata event → shows course/scholarship counts
    - courses event → displays course cards
    - scholarships event → displays scholarship cards
    - chunk events → streams AI analysis text
    - done event → shows completion stats
```

## How to Test

### Step 1: Start the Backend
```bash
cd /Users/prameshluitel/Documents/ScholarRadar
python -m src.mcp_server.server
```

Look for these log messages:
- `advisor_request_received` - Request arrived
- `profile_parsed` - Profile JSON parsed successfully
- `querying_database` - Starting database queries
- `database_query_complete` - Found X courses, Y scholarships
- `sending_metadata` - Sending events to frontend
- `starting_llm_stream` - Starting LLM streaming
- `stream_complete` - LLM finished streaming
- `advisor_stream_finished` - All done!

### Step 2: Test with Script
```bash
cd /Users/prameshluitel/Documents/ScholarRadar
python test_advisor.py
```

This will:
- Send a test profile to the advisor
- Show all events received
- Report if any events are missing
- Display the AI response

### Step 3: Test via Frontend
```bash
cd frontend
npm run dev
```

Visit: http://localhost:5173/finduni

Fill in the form and click "Find My Path"

## What You Should See

### Frontend Loading Sequence:
1. ✅ "Parsing your profile..." (0.5s)
2. ✅ "Querying courses database..." (1-2s)
3. ✅ "Matching scholarships..." (1-2s)
4. ✅ Course cards appear (if matches found)
5. ✅ Scholarship cards appear (if matches found)
6. ✅ "AI is writing your plan..." (10-20s)
7. ✅ AI analysis streams in with markdown formatting
8. ✅ Completion stats appear (model, time, cost)

### Backend Log Sequence:
```
INFO advisor_request_received
INFO profile_parsed keys=['nationality', 'current_qualification', ...]
INFO advisor_analyze nationality=Nepalese subject=Computer Science countries=['Australia']
INFO querying_database countries=['Australia']
INFO database_query_complete courses=15 scholarships=10 universities=10
INFO sending_metadata courses=15 scholarships=10
INFO sending_courses count=15
INFO sending_scholarships count=10
INFO starting_llm_stream prompt_length=12345
INFO groq_cascade_trying model=groq/compound
INFO groq_cascade_success model=groq/compound input_tokens=5000 output_tokens=3000
INFO stream_complete total_time=15.5
INFO advisor_stream_finished
```

## Common Issues & Solutions

### Issue: No events received at all
**Check:**
1. Is backend running? `curl http://localhost:8000/health`
2. Check backend logs for errors
3. Check browser console for network errors
4. Verify GROQ_API_KEY is set in .env

**Solution:**
```bash
# Check if API key is set
cat .env | grep GROQ_API_KEY

# Check backend health
curl http://localhost:8000/health

# Check backend logs (should see structlog output)
```

### Issue: Metadata received but no AI text
**Check:**
1. Backend logs - look for `starting_llm_stream`
2. Check if Groq API is responding
3. Check for timeout errors

**Solution:**
- The LLM might be slow - wait up to 60 seconds
- Check if GROQ_API_KEY has credits remaining
- Try the test script to isolate the issue

### Issue: Error event received
**Check:**
1. What does the error message say?
2. Check backend logs for `stream_error` or `advisor_stream_failed`
3. Look for full traceback with `exc_info=True`

**Common Errors:**
- "GROQ_API_KEY not set" → Add to .env file
- "All AI models unavailable" → Groq API rate limit, wait and retry
- "Analysis failed: ..." → Check the specific error in logs

### Issue: Frontend shows loading forever
**Check:**
1. Open browser DevTools → Network tab
2. Look for the `/api/advisor/analyze` request
3. Check if it's still streaming or failed
4. Check response preview for events

**Solution:**
- The stream might have failed - check for error events
- Reload and try again
- Check backend logs for what happened

## Event Protocol (Frontend ↔ Backend)

### Events Backend MUST Send:
```javascript
// 1. Metadata (REQUIRED - sent first)
{ type: 'metadata', courses_found: 15, scholarships_found: 10 }

// 2. Courses (if any found)
{ type: 'courses', data: [/* array of course objects */] }

// 3. Scholarships (if any found)
{ type: 'scholarships', data: [/* array of scholarship objects */] }

// 4. Status updates (optional, for loading messages)
{ type: 'status', content: 'Generating your personalized analysis...' }

// 5. Model info (when LLM starts)
{ type: 'model', model: 'groq/compound', display_name: 'Groq Compound AI' }

// 6. Content chunks (streaming text)
{ type: 'chunk', content: '### 🎯 Your Profile Analysis\n...' }

// 7. Done (when complete)
{ type: 'done', model: '...', display_name: '...', usage: {...}, cost_usd: 0.05, total_time_seconds: 15.5 }

// 8. Error (if something fails)
{ type: 'error', message: 'Detailed error message' }

// 9. Done marker (SSE protocol)
data: [DONE]
```

### Events Frontend Handles:
```javascript
// In FindUni.jsx handleSubmit():
if (ev.type === 'metadata') setMetadata(ev);
else if (ev.type === 'courses') setCourses(ev.data || []);
else if (ev.type === 'scholarships') setScholarships(ev.data || []);
else if (ev.type === 'model') setModelInfo(ev);
else if (ev.type === 'chunk') setResponseText(p => p + ev.content);
else if (ev.type === 'status') { /* updates loading step */ }
else if (ev.type === 'done') setDoneInfo(ev);
else if (ev.type === 'error') setError(ev.message);
```

## System Prompt Design

The new system prompt ensures:

1. **Deep Personalization** - Analyzes CV details, connects past to future
2. **Honest Guidance** - Clear about budget/score limitations
3. **Actionable Advice** - Specific URLs, deadlines, amounts
4. **Country Strict** - Only recommends selected countries
5. **Financial Reality** - Complete cost breakdown
6. **Structured Response** - 9 sections covering all aspects

### Response Sections:
1. 🎯 Your Profile Analysis
2. 🎓 Best-Match Universities & Courses
3. 💰 Scholarships You Can Win
4. 💵 Complete Financial Breakdown
5. 🛂 Your Visa Pathway
6. 📝 Test Score Strategy
7. 📅 Your Month-by-Month Action Plan
8. 🚀 Your Career Pathway After Graduation
9. ⚡ 5 Things to Do THIS WEEK

## Database Queries

The advisor queries these tables:
- `courses` - Matching courses by subject, level, country, IELTS
- `scholarships` - Matching scholarships by subject, level, country, nationality
- `universities` - Top universities in preferred countries
- `visa_requirements` - Visa rules for nationality → destination
- `cost_of_living` - Living costs in destination cities

## Quality Checklist

Before deploying to production:

- [ ] Backend logs show all steps completing
- [ ] Test script receives all event types
- [ ] Frontend displays course cards (if matches)
- [ ] Frontend displays scholarship cards (if matches)
- [ ] AI analysis streams in real-time
- [ ] Completion stats appear
- [ ] No errors in browser console
- [ ] No errors in backend logs
- [ ] Response is personalized to profile
- [ ] Recommendations match selected countries
- [ ] Financial breakdown is accurate
- [ ] Visa information is correct
- [ ] Action items are specific and timely

## Support

If issues persist:
1. Check backend logs with `exc_info=True` for full tracebacks
2. Run test_advisor.py to isolate backend vs frontend issues
3. Verify all environment variables are set
4. Check database connectivity
5. Verify Groq API key has credits

Remember: This feature impacts students' futures - ensure it works flawlessly before deployment!
