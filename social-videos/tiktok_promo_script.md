# Skolr.xyz Viral Promotion Script & Tech Stack Guide

## 🎬 Production Architecture (How this comes together)

Yes, **Remotion** acts as your final programmatic video editor! It will stitch everything together:
1. **Google VEO** generates the raw video file (mp4) for the first 5-8 second "Hook" scene.
2. **ElevenLabs / OpenAI** generates the Voiceover (mp3/wav) audio files.
3. **Remotion** does the following:
   - Imports your VEO video using the `<Video />` component.
   - Layers your voiceover and background music using `<Audio />` tags.
   - Builds the UI animations and screen recordings using raw React components and physics (Springs).
   - Syncs all audio with the visual transitions natively in code so it outputs a final, perfectly timed `mp4`.

---

## 🎥 The Improved Google VEO Prompts (For Scene 1 Hook)
*AI video models like VEO require extremely granular, technical cinematic descriptions to avoid looking cheap. Use these high-fidelity prompts:*

**Prompt Option 1 (The UGC "Handheld" POV - Best for TikTok):**
> "Vertical 9:16 aspect ratio. Shot on iPhone 15 Pro Max, subtle handheld shake. A gorgeous 22-year-old blonde female university student wearing a high-end streetwear oversized hoodie sits in a moody, neon-lit aesthetic cafe at night. Initially, she stares at her laptop looking exhausted and overwhelmed, rubbing her temples. Suddenly, a bright blue light from the laptop screen illuminates her face. Her eyes widen, her jaw drops in genuine disbelief, and she looks directly into the camera lens completely mind-blown. Ultra-realistic skin texture, dynamic hair physics, cinematic shallow depth of field (f/1.4), raw authentic lighting, 60fps, 4k."

**Prompt Option 2 (The Studio-Grade "Cluely" Aesthetic):**
> "Vertical 9:16, 4k resolution. High-end cinematic tracking shot pushing slowly toward an attractive 20-something blonde female student working intensely at a sleek wooden desk. The background is a beautifully blurred, warm-lit library. She looks entirely burnt-out, sighing heavily at her screen. Cut to a near-macro shot: her expression shifts instantly from pure frustration to absolute shock as a glowing reflection from the screen reflects in her eyes. Volumetric lighting, high contrast, photorealistic, intricate facial expressions, cinematic color grading."

---

## 🎬 Master Video Script (45 Seconds)

### Scene 1: The Hook (0:00 - 0:08)
* **Visual:** (The VEO video from the prompt above). The blonde student transitions from extreme frustration to absolute amazement.
* **Remotion Overlay:** Kinetic pop-up text appearing word-by-word: "Stop. Paying. Study-Abroad Agencies. 🛑"
* **Voiceover (via Remotion `<Audio />`):** "Why are international students still paying thousands to agencies just to find a course?"
* **SFX (via Remotion):** Deep bass swell leading to a whoosh.

### Scene 2: The Solution (0:08 - 0:15)
* **Visual:** The VEO video scales out smoothly and gets framed inside a glassmorphic React component in Remotion. We zoom into a beautifully rendered UI of Claude Web. The cursor (animated via Remotion Springs) clicks "Connectors" and pastes the URL: `https://skolr.xyz/mcp`. 
* **Remotion Overlay:** Floating 3D badge: "One URL. 🤯"
* **Voiceover:** "I just found a way to bypass all the gatekeepers. It’s a free database called Skolr dot X-Y-Z."
* **SFX:** Muffled electronic beat drops. Premium mechanical keyboard typing sounds.

### Scene 3: The Proof / "Aha!" Moment (0:15 - 0:30)
* **Visual:** The prompt box in Claude types: *"Find me a Masters in CS in Canada with full scholarships."* Claude instantly streams back real data. The Remotion camera zooms dynamically into the output, highlighting a pill tag that says "Deadline: Updated Today" and a direct "Apply Here" button.
* **Voiceover:** "You just connect it to Claude, and it pulls live, daily-scraped data from over 30 countries. Programs, visas, and hidden government scholarships."
* **SFX:** "Ding" / Success chime synced exactly to the scholarship appearing on screen.

### Scene 4: The Transparency Flex (0:30 - 0:38)
* **Visual:** The cursor clicks the link in Claude. The Remotion composition sweeps seamlessly to show a real university's official `.edu` page loading instantly. A 3D glassmorphic badge pops up reading "100% Free / Unbiased".
* **Voiceover:** "Every link goes straight to the official university page. No agency fees, completely unbiased."
* **SFX:** Smooth, satisfying UI pop sounds (`pop.mp3`). 

### Scene 5: Outro Stinger (0:38 - 0:45)
* **Visual:** The premium Skolr brand animation. A 3D blue dot drops onto the screen, bounces with realistic physics, expands into a clean, Apple-esque white box to reveal the Skolr logo, and slides to reveal `.xyz`. 
* **Remotion Overlay:** Stop guessing. `skolr.xyz`
* **Voiceover:** "The moment your AI stops guessing. Try it for free right now at Skolr dot X-Y-Z."
* **SFX:** Sub-bass drop, followed by a crisp, high-end "click".

---

## 🎙️ Voiceover Generation Script (Copy & Paste)

*Use a premium, authoritative, but youthful AI voice (e.g., 'Bella' or 'Rachel' in ElevenLabs). Set stability to ~40% for more natural emotion.*

### Full Script for Generation:
"Why are international students still paying thousands to agencies just to find a course? Stop getting gatekept. I just found a way to bypass all that. It’s a free database called Skolr dot X-Y-Z. 

Just connect it to Claude, and it pulls live, daily-scraped data from over thirty countries. Programs, visas, and even hidden government scholarships that agencies never tell you about. 

Every link goes straight to the official university page. No agency fees, completely unbiased. The moment your AI stops guessing. Try it for free right now at Skolr dot X-Y-Z."

### Segmented Pitch (For better Remotion syncing):
| Segment | Time | Script Text | Tone |
| :--- | :--- | :--- | :--- |
| **Hook** | 0-8s | "Why are international students still paying thousands to agencies just to find a course? Stop getting gatekept." | Frustrated, questioning, then firm. |
| **Solution** | 8-15s | "I just found a way to bypass all that. It’s a free database called Skolr dot X-Y-Z." | Excited, "sharing a secret" vibe. |
| **Proof** | 15-30s | "Just connect it to Claude, and it pulls live, daily-scraped data from over thirty countries. Programs, visas, and even hidden government scholarships that agencies never tell you about." | Impressive, fast-paced, informative. |
| **Flex** | 30-38s | "Every link goes straight to the official university page. No agency fees, completely unbiased." | Confident, trustworthy. |
| **Outro** | 38-45s | "The moment your AI stops guessing. Try it for free right now at Skolr dot X-Y-Z." | Polished, professional, final. |
