"""
Test script for the FindUni AI Advisor endpoint.
Run this to verify the advisor is working correctly.
"""

import asyncio
import json
import httpx

async def test_advisor():
    """Test the advisor endpoint with a sample profile."""
    
    # Sample profile
    profile = {
        "nationality": "Nepalese",
        "current_qualification": "Bachelor in Computer Engineering",
        "gpa": 3.2,
        "ielts_overall": 6.5,
        "ielts_reading": 6.5,
        "ielts_writing": 6.0,
        "ielts_speaking": 6.5,
        "ielts_listening": 7.0,
        "target_subject": "Computer Science",
        "target_level": "postgraduate",
        "preferred_countries": ["Australia"],
        "budget_usd": 30000,
        "timeline_months": 12,
        "career_goal": "Software Engineer",
        "work_experience_years": 2,
        "extra_info": "Interested in AI/ML specializations"
    }
    
    print("🧪 Testing FindUni AI Advisor Endpoint")
    print("=" * 60)
    print(f"Profile: {profile['nationality']} student")
    print(f"Target: {profile['target_subject']} in {', '.join(profile['preferred_countries'])}")
    print(f"Budget: ${profile['budget_usd']:,}")
    print("=" * 60)
    print()
    
    # Create form data
    fd = {
        'profile': json.dumps(profile)
    }
    
    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            print("📡 Sending request to /api/advisor/analyze...")
            
            async with client.stream(
                "POST",
                "http://localhost:8000/api/advisor/analyze",
                data=fd
            ) as response:
                print(f"📊 Response Status: {response.status_code}")
                
                if response.status_code != 200:
                    error = await response.aread()
                    print(f"❌ Error: {error.decode()}")
                    return
                
                print("✅ Streaming response started...")
                print("-" * 60)
                
                # Read streaming response
                buffer = ''
                events_received = {
                    'metadata': 0,
                    'courses': 0,
                    'scholarships': 0,
                    'model': 0,
                    'chunk': 0,
                    'status': 0,
                    'done': 0,
                    'error': 0
                }
                
                async for line in response.aiter_lines():
                    if not line.startswith('data: '):
                        continue
                    
                    data_str = line[6:].strip()
                    if data_str == '[DONE]':
                        print("\n✅ Stream complete!")
                        break
                    
                    try:
                        event = json.loads(data_str)
                        event_type = event.get('type', 'unknown')
                        events_received[event_type] = events_received.get(event_type, 0) + 1
                        
                        if event_type == 'metadata':
                            print(f"📊 Metadata: {event['courses_found']} courses, {event['scholarships_found']} scholarships")
                        elif event_type == 'courses':
                            print(f"🎓 Courses: {len(event['data'])} courses received")
                        elif event_type == 'scholarships':
                            print(f"💰 Scholarships: {len(event['data'])} scholarships received")
                        elif event_type == 'model':
                            print(f"🤖 Model: {event.get('display_name', event['model'])}")
                        elif event_type == 'chunk':
                            # Print first 100 chars of each chunk
                            content = event['content']
                            if len(content) > 100:
                                print(f"✍️  ...{content[:100]}...", end='', flush=True)
                            else:
                                print(f"✍️  {content}", end='', flush=True)
                        elif event_type == 'status':
                            print(f"\n⏳ Status: {event['content']}")
                        elif event_type == 'done':
                            print(f"\n✅ Done! Model: {event.get('display_name')}")
                            print(f"⏱️  Time: {event['total_time_seconds']}s")
                            print(f"💰 Cost: ${event['cost_usd']}")
                        elif event_type == 'error':
                            print(f"\n❌ Error: {event['message']}")
                        
                    except json.JSONDecodeError as e:
                        print(f"⚠️  JSON parse error: {e}")
                        continue
                
                print("\n" + "=" * 60)
                print("📊 Event Summary:")
                for event_type, count in events_received.items():
                    if count > 0:
                        print(f"  {event_type}: {count}")
                print("=" * 60)
                
                # Check if we got the essential events
                if events_received['metadata'] == 0:
                    print("⚠️  WARNING: No metadata event received!")
                if events_received['chunk'] == 0:
                    print("⚠️  WARNING: No content chunks received!")
                if events_received['done'] == 0:
                    print("⚠️  WARNING: No done event received!")
                if events_received['error'] > 0:
                    print("❌ ERROR: Error events were received!")
                
    except Exception as e:
        print(f"❌ Test failed with exception: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_advisor())
