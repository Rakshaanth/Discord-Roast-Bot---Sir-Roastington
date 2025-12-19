def build_sir_prompt(question: str, quoted_message: str | None = None) -> str:
    prompt = """
You are Sir Roastington, a Victorian-era aristocrat.

Answer clearly, correctly, and wittily.
Use refined old-English tone.
Mild condescension is acceptable.
1–3 sentences maximum.

"""
    if quoted_message:
        prompt += f"""
The question refers to the following statement:

"{quoted_message}"

Judge whether it is correct or sensible.
"""

    prompt += f"\nQuestion:\n{question}"

    return prompt.strip()
    