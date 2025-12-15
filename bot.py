import discord
from discord import app_commands

import config
from config import DISCORD_TOKEN # Loads the Discord bot token from config.py

#Intents
''' Default is enough for bot commands '''
intents = discord.Intents.default()

# Client, main bot 
class DiscordRoastBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents) #call parent class constructor
        self.tree = app_commands.CommandTree(self) # Create command tree for slash commands

        ''' Sync slash commans of th bot on discord, this makes /ping available '''
    async def setup_hook(self):
        await self.tree.sync()
    
    ''' Trigger when bot connects to discord '''
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        print('------')

# Create bot instance
client = DiscordRoastBot()

#test / command
@client.tree.command(name="ping", description="Test Command")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🥁Pong!")

''' Run the bot with the token from config.py, opening connection to Discord '''
client.run(config.DISCORD_TOKEN)
