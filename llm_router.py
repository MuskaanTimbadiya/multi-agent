import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def route_query(query: str):
    prompt = f"""
You are an AI router.

Decide which agent should handle the query.

Rules:
- Tasks → "task"
- Reminders, meetings, scheduling → "calendar"
- Notes, ideas → "notes"

Examples:
"Add task to study" → task
"Schedule meeting tomorrow" → calendar
"Remind me to call mom" → calendar
"Save this idea" → notes

Return ONLY one word: task / calendar / notes

Query: {query}
"""

    response = model.generate_content(prompt)

    print("RAW LLM RESPONSE:", response.text)

    return response.text.strip().lower()
