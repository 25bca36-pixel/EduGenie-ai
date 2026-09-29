from google import genai

from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    MAX_OUTPUT_TOKENS,
    TEMPERATURE,
)


def generate_text(prompt: str) -> str:
    """
    Generate text using Google Gemini.

    If no API key is configured, return a useful local message
    instead of crashing the application.
    """

    if not GEMINI_API_KEY:
        return (
            "Gemini API key is not configured. "
            "Please add GEMINI_API_KEY to your .env file."
        )

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config={
                "temperature": TEMPERATURE,
                "max_output_tokens": MAX_OUTPUT_TOKENS,
            },
        )

        if response.text:
            return response.text.strip()

        return "Gemini returned an empty response."

    except Exception as exc:
        return f"Gemini request failed: {exc}"