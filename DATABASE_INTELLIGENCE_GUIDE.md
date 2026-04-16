# FindUni AI - Database Intelligence Guide

## 🎯 What We Fixed

The advisor now leverages **ALL available database fields** to provide genuinely helpful, location-specific, data-rich guidance for students.

## 📊 Complete Database Schema Usage

### 1. **COURSES TABLE** - Full Intelligence

**Fields Now Used:**
```javascript
{
  name: "Master of Computer Science",
  university: "University of Melbourne",
  country: "Australia",
  city: "Melbourne",
  state: "VIC",  // ✅ NOW USED - Critical for location filtering
  location: "Melbourne, VIC",  // ✅ NEW - Combined for display
  level: "postgraduate",
  tuition_fee: 45000,
  currency: "AUD",
  tuition_display: "AUD 45,000/yr",
  duration_months: 24,
  duration_years: 2.0,  // ✅ NEW - Easier to understand
  ielts_required: 6.5,
  ielts_breakdown: {  // ✅ NEW - Full IELTS details
    overall: 6.5,
    reading: 6.0,
    writing: 6.0,
    speaking: 6.0,
    listening: 6.0
  },
  ielts_met: true,
  gpa_requirement: "65%",
  entry_qualification: "Bachelor degree",
  start_dates: ["February", "July"],  // ✅ NOW USED - When can they start?
  apply_url: "https://apply.unimelb.edu.au/...",
  cricos_code: "012345A",  // ✅ CRITICAL - Official gov registration
  provider_code: "00116K",  // ✅ CRITICAL - University code
  relevance: 0.95,
  match_reason: "Perfect subject match • Meets English requirements"
}
```

**Why This Matters:**
- **State data** → Students can filter by NSW/VIC/QLD/etc.
- **CRICOS code** → Proves course is government-approved for international students
- **IELTS breakdown** → Shows if student meets EACH section requirement
- **Start dates** → Helps students plan timeline
- **Duration years** → Easier to calculate total cost

### 2. **SCHOLARSHIPS TABLE** - Complete Data

**Fields Now Used:**
```javascript
{
  title: "Melbourne International Scholarship",
  university: "University of Melbourne",
  country: "Australia",
  city: "Melbourne",  // ✅ NOW USED
  funding_type: "partial",
  value: "AUD 10,000",
  value_numeric: 10000,
  award_min: 5000,  // ✅ NEW - Range info
  award_max: 10000,  // ✅ NEW - Range info
  currency: "AUD",  // ✅ NEW
  deadline: "2026-03-15",
  eligibility: "Open to all international students",
  description: "Merit-based scholarship for...",  // ✅ NOW USED
  match_score: 0.85,
  why_matched: ["Subject match: 85%", "Open to all international students"],
  apply_url: "https://scholarships.unimelb.edu.au/...",
  source: "university_direct",  // ✅ NOW USED
  source_url: "https://finduni.online/..."
}
```

**Why This Matters:**
- **City data** → Students know WHERE the scholarship is
- **Award range** → Shows min-max possible value
- **Description** → Helps students understand what it's for
- **Source** → Shows if it's university, government, etc.

### 3. **UNIVERSITIES TABLE** - Full Profile

**Fields Now Used:**
```javascript
{
  name: "University of Melbourne",
  country: "Australia",
  city: "Melbourne",
  state: "VIC",  // ✅ NOW USED
  world_ranking: 14,
  subject_rankings: {  // ✅ NOW USED - Field-specific rankings
    "computer science": 8,
    "engineering": 12
  },
  acceptance_rate: 70.5,
  total_students: 51000,
  international_students: 18000,
  tuition_min: 35000,
  tuition_max: 55000,
  currency: "AUD",  // ✅ NOW USED
  ielts_minimum: 6.5,
  popular_subjects: ["Computer Science", "Engineering", "Business"],  // ✅ NOW USED
  facilities: ["Library", "Lab", "Gym"],  // ✅ NOW USED
  accommodation_cost_min: 200,  // ✅ NOW USED - Weekly
  accommodation_cost_max: 400,  // ✅ NOW USED - Weekly
  website: "https://unimelb.edu.au",
  provider_code: "00116K"  // ✅ NOW USED
}
```

**Why This Matters:**
- **State** → Location filtering
- **Subject rankings** → Better than world ranking for specific fields
- **Popular subjects** → Shows university's strengths
- **Accommodation costs** → Realistic budget planning
- **International students** → Shows diversity

### 4. **VISA REQUIREMENTS TABLE** - Complete Info

**Fields Now Used:**
```javascript
{
  country: "Australia",
  visa_type: "Student Visa",
  visa_subclass: "500",  // ✅ NOW USED - Official name
  financial_requirement_aud: 29710,  // ✅ CRITICAL - DHA requirement
  processing_weeks: "4-6",
  processing_weeks_min: 4,  // ✅ NEW - For calculations
  processing_weeks_max: 6,  // ✅ NEW - For calculations
  work_rights_hours: 48,  // ✅ NOW USED - Hours per fortnight
  required_documents: [  // ✅ NOW USED - Checklist!
    "CoE",
    "Genuine Student statement",
    "Financial evidence",
    "English test results",
    "Health insurance"
  ],
  health_requirements: "OSHC required",  // ✅ NOW USED
  notes: "Apply at least 6-8 weeks before course start",  // ✅ NOW USED
  source_url: "https://immi.homeaffairs.gov.au/..."  // ✅ NOW USED - Official source
}
```

**Why This Matters:**
- **Visa subclass** → Official government terminology
- **Financial requirement** → EXACT amount students need to show
- **Processing weeks** → When to apply
- **Required documents** → Complete checklist for students
- **Health requirements** → OSHC info for Australia
- **Notes** → Critical tips from official sources

### 5. **COST OF LIVING TABLE** - Detailed Budget

**Fields Now Used:**
```javascript
{
  city: "Melbourne",
  country: "Australia",
  rent_shared_min: 150,  // ✅ NOW USED - Weekly
  rent_shared_max: 250,  // ✅ NOW USED - Weekly
  rent_private_min: 300,  // ✅ NOW USED - Weekly
  rent_private_max: 500,  // ✅ NOW USED - Weekly
  food_monthly: 400,  // ✅ NOW USED
  transport_monthly: 150,  // ✅ NOW USED
  utilities_monthly: 100,  // ✅ NOW USED
  internet_monthly: 60,  // ✅ NOW USED
  total_monthly_min: 1200,  // ✅ NOW USED
  total_monthly_max: 2000,  // ✅ NOW USED
  part_time_wage_hourly: 24.10,  // ✅ CRITICAL - Students can earn this
  currency: "AUD",
  weekly_budget: {  // ✅ NEW - Easier to understand
    shared_rent_min: 34.64,
    shared_rent_max: 57.74,
    food: 92.38,
    transport: 34.64
  }
}
```

**Why This Matters:**
- **Rent ranges** → Shared vs private options
- **All expenses** → Complete budget picture
- **Part-time wage** → REALISTIC earnings potential
- **Weekly budget** → Students think in weeks, not months
- **Total monthly** → Min-max for planning

## 🌍 Location Intelligence

### Australia (CRICOS Data)

**States Available:**
- NSW (New South Wales) - Sydney
- VIC (Victoria) - Melbourne
- QLD (Queensland) - Brisbane
- WA (Western Australia) - Perth
- SA (South Australia) - Adelaide
- TAS (Tasmania) - Hobart
- ACT (Australian Capital Territory) - Canberra
- NT (Northern Territory) - Darwin

**Why State Matters:**
1. **Visa points** - Regional areas give additional PR points
2. **Cost of living** - Sydney/Melbourne expensive, Adelaide/Perth cheaper
3. **Job opportunities** - Tech in Sydney/Melbourne, Mining in Perth
4. **Lifestyle** - Different climates, cultures, pace of life
5. **Post-study work** - Regional areas get longer visas

**Industry Hubs:**
- **Sydney (NSW)**: Finance, Tech, Consulting
- **Melbourne (VIC)**: Tech, Education, Healthcare, Arts
- **Brisbane (QLD)**: Mining, Tourism, Agriculture
- **Perth (WA)**: Mining, Engineering, Resources
- **Adelaide (SA)**: Defense, Manufacturing, Wine
- **Canberra (ACT)**: Government, Research, Education

### UK Cities

**Major Cities:**
- London - Expensive but most opportunities
- Manchester - Tech hub, cheaper than London
- Birmingham - Growing tech scene
- Edinburgh - Finance, Tourism
- Glasgow - Engineering, Healthcare
- Bristol - Tech, Creative industries

### Other Countries

Use city data from database to provide:
- Cost of living comparisons
- Job market info
- Lifestyle differences
- Industry presence

## 🎯 How Advisor Uses This Data

### 1. **Course Recommendations**
```
"Master of Computer Science at University of Melbourne
📍 Melbourne, VIC, Australia
🎓 CRICOS: 012345A (Government-approved)
💰 AUD 45,000/yr × 2 years = AUD 90,000 total
📝 IELTS 6.5 overall (You have 7.0 ✓)
📅 Start: February or July 2026
🔗 Apply: https://apply.unimelb.edu.au/..."
```

### 2. **Financial Breakdown**
```
Total Cost for 2 Years in Melbourne:
┌─────────────────┬──────────────┐
│ Tuition         │ AUD 90,000   │
│ Living (2 yrs)  │ AUD 57,600   │
│ ─────────────────────────────── │
│ TOTAL           │ AUD 147,600  │
│ Scholarship     │ -AUD 20,000  │
│ ─────────────────────────────── │
│ NET COST        │ AUD 127,600  │
└─────────────────┴──────────────┘

Part-time Work Potential:
- Wage: AUD 24.10/hour
- Max: 48 hrs/fortnight during study
- Monthly: ~AUD 2,315 (20 hrs/week)
- Can cover: Rent + Food
```

### 3. **Visa Guidance**
```
Student Visa (Subclass 500):
✅ Financial proof: AUD 29,710/year
✅ Processing: 4-6 weeks
✅ Work rights: 48 hrs/fortnight
✅ Post-study work: 2-4 years

Required Documents:
□ Confirmation of Enrolment (CoE)
□ Genuine Student statement
□ Financial evidence (bank statements)
□ English test results (IELTS)
□ Overseas Student Health Cover (OSHC)

Apply by: January 2026 for February intake
```

### 4. **Location Advice**
```
Why Melbourne, VIC?
✅ Tech hub - 15,000+ IT jobs
✅ Lower cost than Sydney (20% cheaper rent)
✅ Post-study work: 3 years (VIC is regional-eligible)
✅ Strong Nepalese community
✅ Direct flights to Kathmandu

Alternative: Adelaide, SA
✅ Even cheaper (30% less than Melbourne)
✅ Additional 5 PR points for regional study
✅ Post-study work: 4-5 years
✅ Growing tech scene
```

## 🔍 Frontend Features

### Location Filter
```javascript
// Students can filter courses by state/city
filteredCourses = courses.filter(c => {
  if (!locationFilter) return true;
  const search = locationFilter.toLowerCase();
  return (c.city?.toLowerCase() || '').includes(search) || 
         (c.state?.toLowerCase() || '').includes(search);
});

// Available locations auto-generated from data
availableLocations = ["NSW", "VIC", "QLD", "WA", "SA", "Melbourne", "Sydney", ...]
```

### Course Card Display
```
┌─────────────────────────────────────┐
│ 🎓 Elite Insight                    │
│ Perfect subject match • IELTS ✓     │
│                                     │
│ Master of Computer Science     95%  │
│ University of Melbourne             │
│ 📍 Melbourne, VIC                   │
│ CRICOS: 012345A  PROV: 00116K      │
│                                     │
│ [Australia] [Postgraduate] [24 mo]  │
│ [IELTS ✓ (6.5)]                     │
│                                     │
│ AUD 45,000/yr        [Apply →]     │
└─────────────────────────────────────┘
```

## 📋 Quality Checklist

Every recommendation MUST include:

- [ ] **Exact course name** from database
- [ ] **University name** from database
- [ ] **City AND State** (not just country)
- [ ] **CRICOS code** (if Australia)
- [ ] **Annual tuition** AND **total course cost**
- [ ] **IELTS requirements** (full breakdown)
- [ ] **Duration** (in years for clarity)
- [ ] **Start dates** (when can they apply)
- [ ] **Direct apply URL** from database
- [ ] **Location benefits** (why this city?)
- [ ] **Cost of living** for that specific city
- [ ] **Part-time wage** in that city
- [ ] **Scholarship eligibility** (specific to their profile)
- [ ] **Visa requirements** (with exact amounts)
- [ ] **Required documents** (complete checklist)
- [ ] **Timeline** (when to apply, when to start)

## 🎓 Student Benefits

### What Students Get:
1. **Location-specific guidance** - Not just "Australia" but "Melbourne, VIC"
2. **Real costs** - Exact tuition + living for their chosen city
3. **Official data** - CRICOS codes, visa subclasses, financial requirements
4. **Complete checklists** - Documents, timelines, deadlines
5. **Honest advice** - Budget reality, score requirements, alternatives
6. **Career insights** - Which cities have jobs for their field
7. **PR pathways** - Regional vs metro, points, visa durations
8. **Financial planning** - Weekly budgets, part-time earnings, scholarships

### What Students DON'T Get:
- ❌ Generic "study in Australia" advice
- ❌ Fake or hallucinated fees/requirements
- ❌ Vague "check website" responses
- ❌ Ignoring their budget constraints
- ❌ Recommending countries they didn't select
- ❌ Sugarcoating challenges
- ❌ Missing critical deadlines or requirements

## 🚀 Impact

This level of detail means:
- **Students make informed decisions** - Not blind choices
- **No surprises** - They know exact costs, requirements, timelines
- **Better planning** - Complete checklists and timelines
- **Realistic expectations** - Honest about budget, scores, chances
- **Location-aware choices** - Understand city/state implications
- **Career-focused** - Know which locations have job opportunities
- **PR-ready** - Understand visa pathways from day one

**This is what separates ScholarRadar from random consultancies - we provide DATA, not fluff.**
