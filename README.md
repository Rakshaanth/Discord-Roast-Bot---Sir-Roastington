# Sir Roastington — Discord Roast Bot

Sir Roastington is an AI-powered Discord bot that delivers **witty, old-English, 18+ roasts** and intelligent replies using modern LLMs.  
He judges usernames, bios, and conversations with aristocratic disappointment.

---

## Features

- `/roast` — Roast a user by name (and optional bio)
- `/decode` — Translate the previous roast into simple modern English
- `/sir` — Ask Sir Roastington any question  
  - Supports contextual questions like:
    - `Is @jack correct?`
    - `@sarim thinks Elon is dumb`
    - General knowledge questions
- LLM-backed responses (Gemini by default)
- Stateless design (no message storage)
- Slash-command based (Discord-native UX)

---

## Tech Stack

Python 3.11

discord.py API

Google Gemini API

Flask (optional keep-alive)

Replit 

---
## Personality

**Sir Roastington**
- Old-English aristocrat tone
- Sharp, witty, and offensive (18+)
- Never vulgar, always condescending
- Explains himself only when commanded

---

## Project Structure

├── bot.py # Main Discord bot entry point

├── config.py # Environment variable loader & validation

├── requirements.txt # Python dependencies

├── LLM/

│ ├── init.py

│ ├── base.py # Abstract LLM interface

│ └── gemini.py # Gemini LLM implementation

├── Prompts/

│ ├── init.py

│ └── personality.py # Sir Roastington prompt builders

└── .gitignore


---

## 🔐 Environment Variables

Set these as environment variables (**do NOT commit `.env`**):

DISCORD_TOKEN=your_discord_bot_token
GEMINI_API_KEY=your_gemini_api_key
LLM_PROVIDER=gemini
