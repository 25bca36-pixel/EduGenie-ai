import json
import re

from gemini_client import generate_text


def generate_quiz(topic: str, number_of_questions: int = 5):
    if not topic.strip():
        return []

    number_of_questions = max(1, min(number_of_questions, 10))

    prompt = f"""
Create {number_of_questions} educational multiple-choice questions
about:

{topic}

Return ONLY valid JSON.

Use exactly this format:

[
  {{
    "question": "Question text",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer": "Option A",
    "explanation": "Short explanation"
  }}
]
"""

    result = generate_text(prompt)

    try:
        cleaned = result.strip()

        if cleaned.startswith("```"):
            cleaned = re.sub(r"^```(?:json)?", "", cleaned)
            cleaned = re.sub(r"```$", "", cleaned).strip()

        data = json.loads(cleaned)

        if not isinstance(data, list):
            return []

        return data

    except (json.JSONDecodeError, TypeError):
        return [
            {
                "question": "Quiz generation returned an invalid response.",
                "options": [],
                "answer": "",
                "explanation": result,
            }
        ]