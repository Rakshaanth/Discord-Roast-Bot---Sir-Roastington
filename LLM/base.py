from abc import ABC, abstractmethod

class RoastLLM(ABC):
    """
    Base interface for all LLM providers.

    Contract:
    - Input: prompt (str)
    - Output: plain text roast (str)
    - Tone: witty, sarcastic, light roast (no slurs, no hate)
    - Length: must not exceed MAX_CHARS
    """
    MAX_CHARS = 280 # Limit appropriate for a discord message (change as needed)

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a roast based on the given prompt.

        Rules:
        - Return plain text only
        - No markdown
        - No code blocks
        - No emojis unless explicitly instructed
        - Must be <= MAX_CHARS characters
        """
        pass

    def _enforce_length(self, text: str) -> str:
        """
        Enforce maximum output length.
        Truncates safely if exceeded.
        """
        if len(text) > self.MAX_CHARS:
            return text[: self.MAX_CHARS].rstrip()
        return text
