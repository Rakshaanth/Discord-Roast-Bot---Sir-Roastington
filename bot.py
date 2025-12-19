import discord
from discord import app_commands

import config
from config import DISCORD_TOKEN

from Prompts.personality import build_roast_prompt
from LLM.gemini import GeminiLLM

# Intents
intents = discord.Intents.default()

# Client
class DiscordRoastBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # Sync slash commands
        await self.tree.sync()

    async def on_ready(self):
        print(f'Logged in as {self.user}')
        print('------')

# Create bot instance
client = DiscordRoastBot()

# Initialize LLM (Gemini)
llm = GeminiLLM()

''' LLM Test Code (in case you want to test the LLM independently)
from LLM.gemini import GeminiLLM
llm = GeminiLLM()
prompt = "Say something witty about the weather."
print(llm.generate(prompt))
'''

# /ping command
@client.tree.command(name="ping", description="Test Command")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🥁Pong!")

# /roast command
@client.tree.command(
    name="roast",
    description="Get roasted by Sir Roastington"
)
@app_commands.describe(
    username="Who shall be roasted?",
    about="Optional bio/about text"
)
async def roast(
    interaction: discord.Interaction,
    username: str,
    about: str | None = None
):
    # Defer the response immediately (prevents 404 for slow LLM)
    await interaction.response.defer()

    # Build prompt with persona
    prompt = build_roast_prompt(username, about)

    # Generate roast via LLM
    try:
        roast_text = llm.generate(prompt)
    except Exception:
        # Fallback if API fails
        roast_text = "Sir Roastington declines to speak. How tragic."

    # Send response
    await interaction.followup.send(roast_text)

# Run the bot
client.run(DISCORD_TOKEN)
