import os
from groq import Groq

# Initialize Groq Client with the key provided
client = Groq(api_key="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")

def generate_voiceover(text, output_path):
    print(f"Generating audio for: {text[:50]}...")
    
    # Using the specified Orpheus model for synthesis
    response = client.audio.speech.create(
        model="canopylabs/orpheus-v1-english",
        voice="austin", 
        input=text,
        response_format="wav" # Required by the model
    )

    # Save the binary response to a file
    response.write_to_file(output_path)
    print(f"Saved audio to: {output_path}")

if __name__ == "__main__":
    script_parts = [
        {
            "name": "hook",
            "text": "If you are still paying a study abroad agency thousands of dollars... Stop. You are being scammed."
        },
        {
            "name": "pivot",
            "text": "These agencies only show you universities that pay them commissions. But there's a secret database they’re trying to hide."
        },
        {
            "name": "tool_reveal",
            "text": "It's called Scholar dot X Y Z. It uses a live AI scraper to pull scholarship data directly from official university sites every single day."
        },
        {
            "name": "result",
            "text": "I found a forty-thousand dollar full-ride for CS in Canada in twelve seconds. Stop getting gatekept."
        },
        {
            "name": "cta",
            "text": "Try it for free at Scholar dot X Y Z... before they shut us down."
        }
    ]

    # Create directory if it doesn't exist
    os.makedirs("social-videos/assets", exist_ok=True)

    for part in script_parts:
        filename = f"social-videos/assets/vo_{part['name']}.wav"
        generate_voiceover(part['text'], filename)
