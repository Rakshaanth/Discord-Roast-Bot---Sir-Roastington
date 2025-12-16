import google.generativeai as genai

import config
from LLM.base import RoastLLM



class GeminiLLM(RoastLLM):
    def __init__(self):
        # Initialize Gemini client with API key
        genai.configure(api_key=config.API_KEY)

        # Use a fast, text-only model
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)

            # Safety / empty response handling
            if not response or not response.text:
                return "Sir Roastington declines to speak. How tragic."

            # Normalize output
            text = response.text.strip()

            # Enforce max length from base class
            return self._enforce_length(text)

        except Exception:
            # Fallback for safety blocks, rate limits, etc.
            return "Sir Roastington was censored by lesser minds."
