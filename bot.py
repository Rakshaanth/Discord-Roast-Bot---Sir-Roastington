import discord
from discord import app_commands

import config
from config import DISCORD_TOKEN

from Prompts.personality import build_roast_prompt

# Intents
intents = discord.Intents.default()

# Client
class DiscordRoastBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f'Logged in as {self.user}')
        print('------')

client = DiscordRoastBot()

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
    # Build prompt (LLM not used yet)
    prompt = build_roast_prompt(username, about)

    # Dummy response
    dummy_roast = (
        f"Ah yes, {username}. "
        "One observes thee and immediately understands why silence was invented."
    )

    await interaction.response.send_message(dummy_roast)

# Run the bot (must be last)
client.run(DISCORD_TOKEN)
