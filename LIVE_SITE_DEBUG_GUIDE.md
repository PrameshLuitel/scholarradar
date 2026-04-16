# Live Site Debugging Guide - FindUni AI Advisor

## 🐛 Issue Fixed: Results Page Going Back to Form

### Problem:
- Student submits form
- Sees "Loading..." animation
- 2 scholarships appear briefly
- Page goes back to form instead of showing results

### Root Cause:
1. Streaming starts successfully (metadata + scholarships sent)
2. An error occurs mid-stream (could be network, LLM, or parsing error)
3. Error is caught and `setError()` is called
4. `setIsAnalyzing(false)` is called in finally block
5. `showResults` evaluates to `false` because:
   - `responseText` might be empty or short
   - `isAnalyzing` is now `false`
   - `courses.length` might be 0
6. Form shows again instead of results

### Solution Applied:

**1. Enhanced `showResults` Logic:**
```javascript
// BEFORE (Broken):
const showResults = responseText || isAnalyzing || courses.length > 0;

// AFTER (Fixed):
const showResults = responseText || isAnalyzing || courses.length > 0 || scholarships.length > 0 || error;
```

Now results page shows if:
- ✅ There's any response text
- ✅ Still analyzing
- ✅ Has courses
- ✅ **Has scholarships** (NEW!)
- ✅ **Has error** (NEW!)

**2. Added Comprehensive Console Logging:**
```javascript
console.log('Received metadata:', ev);
console.log('Received courses:', ev.data?.length);
console.log('Received scholarships:', ev.data?.length);
console.log('Status:', ev.content);
console.log('Done:', ev);
console.error('Stream error:', ev.message);
console.error('Failed to parse event:', parseError, 'Raw data:', d);
console.error('Submit error:', e);
```

**3. Better Error Display:**
```javascript
// Shows error even if there's partial content
{error && (
  <div>
    <p>{responseText ? 'Partial Analysis - Error Occurred' : 'Analysis Failed'}</p>
    <p>{error}</p>
    {responseText && <p>Analysis below is incomplete...</p>}
  </div>
)}
```

---

## 🔍 How to Debug on Live Site

### Step 1: Open Browser DevTools
```
Chrome/Edge: F12 or Ctrl+Shift+I (Cmd+Option+I on Mac)
Firefox: F12
Safari: Cmd+Option+I (enable DevTools in Preferences first)
```

### Step 2: Go to Console Tab
Look for these log messages:

**Successful Flow:**
```
Received metadata: {courses_found: 15, scholarships_found: 10}
Received courses: 15
Received scholarships: 10
Status: Generating your personalized analysis...
Received model: {model: 'groq/compound', display_name: 'Groq Compound AI'}
[Multiple chunk events...]
Done: {model: '...', total_time_seconds: 15.2}
Request completed, isAnalyzing set to false
```

**Error Flow:**
```
Received metadata: {courses_found: 15, scholarships_found: 10}
Received courses: 15
Received scholarships: 10
Status: Generating your personalized analysis...
Stream error: All AI models are currently unavailable...
Submit error: Error: All AI models...
Request completed, isAnalyzing set to false
```

**Parse Error:**
```
Received metadata: {courses_found: 15, scholarships_found: 10}
Failed to parse event: SyntaxError: Unexpected token... Raw data: {invalid json}
```

### Step 3: Check Network Tab

1. Filter by "Fetch/XHR"
2. Look for `analyze` request
3. Check:
   - **Status Code**: Should be 200
   - **Response**: Click and preview
   - **Timing**: How long did it take?

**Expected Response (SSE Stream):**
```
data: {"type":"metadata","courses_found":15,"scholarships_found":10}

data: {"type":"courses","data":[...]}

data: {"type":"scholarships","data":[...]}

data: {"type":"status","content":"Generating your personalized analysis..."}

data: {"type":"model","model":"groq/compound","display_name":"Groq Compound AI"}

data: {"type":"chunk","content":"### 🎯 Your Profile Analysis\n..."}

data: {"type":"done","model":"groq/compound",...}

data: [DONE]
```

**Error Response:**
```
data: {"type":"error","message":"All AI models are currently unavailable..."}

data: [DONE]
```

### Step 4: Check Backend Logs

If you have access to server logs, look for:

**Successful Flow:**
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

**Error Flow:**
```
INFO advisor_request_received
INFO profile_parsed keys=[...]
INFO querying_database countries=['Australia']
INFO database_query_complete courses=15 scholarships=10
INFO sending_metadata courses=15 scholarships=10
INFO sending_courses count=15
INFO sending_scholarships count=10
INFO starting_llm_stream prompt_length=12345
ERROR groq_cascade_all_failed last_error=groq/compound: HTTP 429
ERROR advisor_stream_failed error="All AI models are currently unavailable..."
```

---

## 🛠️ Common Issues & Fixes

### Issue 1: "All AI models are currently unavailable"

**Cause:** Groq API rate limit or outage

**Check:**
```bash
# Test Groq API directly
curl -X POST https://api.groq.com/openai/v1/chat/completions \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"groq/compound","messages":[{"role":"user","content":"test"}]}'
```

**Fix:**
- Wait a few minutes and retry
- Check Groq status page: https://status.groq.com
- Verify API key has credits remaining

---

### Issue 2: Courses/Scholarships appear but no AI text

**Cause:** LLM streaming failed after database queries succeeded

**Console shows:**
```
Received metadata: {courses_found: 15, scholarships_found: 10}
Received courses: 15
Received scholarships: 10
Stream error: All AI models are currently unavailable...
```

**Fix:**
- This is now handled properly - shows error with partial data
- Student can see courses/scholarships even if AI analysis fails
- Click "Try again" to retry

---

### Issue 3: Page goes back to form immediately

**Cause:** 
- Network error (CORS, connection refused)
- Backend not running
- Wrong API URL

**Console shows:**
```
Submit error: Failed to fetch
```

**Fix:**
```bash
# Check if backend is running
curl http://localhost:8000/health

# Check CORS settings
# Backend should allow your frontend domain
```

**Verify API URL:**
```javascript
// In FindUni.jsx line 636
const res = await fetch('/api/advisor/analyze', { method: 'POST', body: fd });

// For local dev, should be:
// http://localhost:8000/api/advisor/analyze

// For production, should be:
// https://your-domain.com/api/advisor/analyze
```

---

### Issue 4: JSON Parse Errors

**Console shows:**
```
Failed to parse event: SyntaxError: Unexpected token 'I', "Invalid profile JSON" is not valid JSON
Raw data: {"type":"error","message":"Invalid profile JSON"}
```

**Cause:** Backend returning error as JSON instead of SSE format

**Fix:**
- Check backend logs for validation errors
- Ensure profile data is valid JSON
- Verify all required fields are present

---

### Issue 5: Loading Forever

**Console shows:**
```
Received metadata: {courses_found: 15, scholarships_found: 10}
Received courses: 15
Received scholarships: 10
Status: Generating your personalized analysis...
[Nothing else...]
```

**Cause:** LLM streaming started but never completes

**Check:**
1. Network tab - is connection still open?
2. Backend logs - is LLM call stuck?
3. Groq API - is it responding?

**Fix:**
- Add timeout to fetch request
- Check Groq API status
- Increase backend timeout

---

## 📊 What to Look For in Console

### ✅ Success Indicators:
```
✓ Received metadata: {courses_found: X, scholarships_found: Y}
✓ Received courses: X
✓ Received scholarships: Y
✓ Received model: {display_name: '...'}
✓ [Multiple chunk events]
✓ Done: {total_time_seconds: X}
```

### ❌ Error Indicators:
```
✗ Stream error: [message]
✗ Submit error: [message]
✗ Failed to parse event: [error]
✗ Network error: Failed to fetch
```

### ⚠️ Warning Indicators:
```
⚠ No courses found (database query returned 0)
⚠ No scholarships found
⚠ Long response time (>30 seconds)
```

---

## 🧪 Testing Checklist

### Local Testing:
```bash
# 1. Start backend
python -m src.mcp_server.server

# 2. Start frontend
cd frontend
npm run dev

# 3. Open browser with DevTools
# 4. Submit form
# 5. Check console for logs
# 6. Check network tab for requests
# 7. Verify results display
```

### Production Testing:
```bash
# 1. Open live site with DevTools
# 2. Submit form
# 3. Check console for errors
# 4. Check network tab
# 5. Check backend logs (if accessible)
# 6. Verify results or proper error display
```

---

## 🎯 Expected Behavior After Fix

### Scenario 1: Complete Success
```
Form → Loading (2s) → Courses + Scholarships appear → AI text streams (15s) → Done
✅ Results page shows everything
✅ No errors
✅ Can click "New analysis" to restart
```

### Scenario 2: Partial Success (Courses/Scholarships found, AI fails)
```
Form → Loading (2s) → Courses + Scholarships appear → Error occurs
✅ Results page shows courses + scholarships
✅ Error message displayed at bottom
✅ "Try again" button available
✅ Does NOT go back to form
```

### Scenario 3: Complete Failure (Network error)
```
Form → Loading → Error immediately
✅ Results page shows error
✅ "Try again" button available
✅ Does NOT go back to form
```

### Scenario 4: No Matches Found
```
Form → Loading (2s) → No courses/scholarships → AI text streams
✅ Results page shows "No courses found" message
✅ AI still provides guidance
✅ Can try different criteria
```

---

## 📞 Quick Debug Commands

### Check Backend Health:
```bash
curl http://localhost:8000/health
# Should return: {"status":"healthy",...}
```

### Test Advisor Endpoint:
```bash
python test_advisor.py
# Should show all events received
```

### Check Environment Variables:
```bash
# Backend .env file should have:
GROQ_API_KEY=your_key_here
SUPABASE_URL=your_url
SUPABASE_SERVICE_ROLE_KEY=your_key
```

### Verify Database Connection:
```bash
python -c "
from src.database.client import get_db
db = get_db()
result = db.table('courses').select('*').limit(1).execute()
print(f'Courses found: {len(result.data)}')
"
```

---

## 🚀 Deployment Checklist

Before deploying to production:

- [ ] Console logs added (for debugging)
- [ ] Error handling improved
- [ ] `showResults` logic fixed
- [ ] Error display shows even with partial content
- [ ] Tested locally with DevTools open
- [ ] Verified all event types are logged
- [ ] Checked network requests in browser
- [ ] Tested error scenarios (network failure, LLM failure)
- [ ] Verified mobile responsive
- [ ] Checked CORS settings for production domain

---

## 📝 Summary of Changes

### Files Modified:
1. `/frontend/src/pages/FindUni.jsx`
   - Line 706: Enhanced `showResults` logic
   - Lines 653-711: Added comprehensive console logging
   - Lines 716-722: Better error handling in catch block
   - Lines 1115-1129: Improved error display

### What Changed:
- ✅ Results page no longer disappears on error
- ✅ Shows courses/scholarships even if AI fails
- ✅ Console logs help debug issues
- ✅ Error messages are clear and actionable
- ✅ "Try again" button always available

### What Students See Now:
- **Success**: Complete analysis with courses, scholarships, and AI guidance
- **Partial**: Courses + scholarships visible, error message explains what went wrong
- **Failure**: Clear error message with "Try again" option

**No more going back to form unexpectedly!**
