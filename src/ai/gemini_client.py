import os

from dotenv import load_dotenv
from google import genai

# ----------------------------------------
# Load Environment Variables
# ----------------------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)


# ----------------------------------------
# AI Chat Function
# ----------------------------------------

def ask_ai(prompt):
    """
    Sends a prompt to Gemini and returns the response.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text.strip()

    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Sorry, the AI service is currently unavailable."