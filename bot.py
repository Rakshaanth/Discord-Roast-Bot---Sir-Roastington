import discord
from discord import app_commands

import config
from config import DISCORD_TOKEN

from Prompts.personality import build_roast_prompt
from LLM.gemini import GeminiLLM

from Prompts.sir import build_sir_prompt

import re

# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

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
    await interaction.response.defer()

    prompt = build_roast_prompt(username, about)

    try:
        roast_text = llm.generate(prompt)
    except Exception:
        roast_text = "Sir Roastington declines to speak. How tragic."

    await interaction.followup.send(roast_text)

# /decode command
@client.tree.command(
    name="decode",
    description="Explain the previous roast in simple modern English"
)
async def decode(interaction: discord.Interaction):
    await interaction.response.defer()

    channel = interaction.channel
    roast_message = None

    async for msg in channel.history(limit=10):
        if msg.author == client.user and msg.content:
            roast_message = msg.content
            break

    if not roast_message:
        await interaction.followup.send(
            "Sir Roastington finds no recent roast worthy of explanation."
        )
        return

    prompt = f"""
Translate the following roast into ONE simple modern English sentence.
Remove old-English language.

Roast:
{roast_message}
"""

    try:
        decoded = llm.generate(prompt)
    except Exception as e:
        print("LLM error:", e)
        decoded = "Sir Roastington refuses to simplify such eloquence."

    await interaction.followup.send(decoded)

@client.tree.command(
    name="sir",
    description="Ask Sir Roastington any question"
)
@app_commands.describe(
    question="Your question for Sir Roastington"
)
async def sir(interaction: discord.Interaction, question: str):
    await interaction.response.defer()
    channel = interaction.channel
    quoted_message = None

    # Detect first mention in the text
    mention_match = re.search(r"<@!?(\d+)>", question)
    if mention_match:
        user_id = int(mention_match.group(1))
        try:
            target = await interaction.guild.fetch_member(user_id)
            # Fetch last message from that user
            async for msg in channel.history(limit=50):
                if msg.author.id == target.id and msg.content:
                    quoted_message = msg.content
                    break
        except discord.Forbidden:
            await interaction.followup.send(
                "I cannot read message history here. Check my permissions!"
            )
            return

    # Build prompt with optional quoted_message
    prompt = build_sir_prompt(question, quoted_message)

    try:
        reply = llm.generate(prompt)
    except Exception as e:
        print("LLM error:", e)
        reply = "Sir Roastington is indisposed and declines to answer."

    # Show the original question and the answer
    await interaction.followup.send(f"*{question}*\n{reply}")


'''
------------Postscript------------
Just for deployment keep-alive purposes.
'''
from flask import Flask
from threading import Thread
import os

app = Flask("")

@app.route("/")
def home():
    return "Alive"

def run():
    app.run(host="0.0.0.0", port=3000)

Thread(target=run).start()
''' ------------End of Postscript------------'''


# Run the bot 
client.run(DISCORD_TOKEN)
