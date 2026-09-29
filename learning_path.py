from gemini_client import generate_text


def create_learning_path(goal: str) -> str:
    if not goal.strip():
        return "Please enter a learning goal."

    prompt = f"""
Create a practical learning path for this goal:

{goal}

Include:

1. Beginner level
2. Intermediate level
3. Advanced level
4. Topics to study at each level
5. Suggested practice activities
6. Approximate timeline

Keep the plan clear and realistic.
"""

    return generate_text(prompt)