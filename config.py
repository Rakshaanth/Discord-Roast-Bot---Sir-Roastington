import os
from dotenv import load_dotenv

load_dotenv()

#Discord Configuration
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_TOKEN is not set in environment variables.")

#LLM Provider 
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini").lower()

#API Key
API_KEY = os.getenv("GEMINI_API_KEY")
if LLM_PROVIDER == "gemini" and not API_KEY:
    raise ValueError("GEMINI_API_KEY is required for Gemini LLM provider.") 

