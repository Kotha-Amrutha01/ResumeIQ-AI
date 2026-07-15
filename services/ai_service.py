import os
import time
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# Create Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(prompt):

    for _ in range(3):

        try:
            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt
            )

            return response.text

        except Exception as e:

            if "503" in str(e):
                time.sleep(5)
                continue

            return f"Error: {e}"

    return "Gemini is currently busy. Please try again later."