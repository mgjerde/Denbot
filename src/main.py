import fnmatch
import os
import discord
from discord.ext import commands

# import configparser
# config = configparser.ConfigParser()
# config.read('settings.ini')

DEBUG_GUILDS = [os.environ.get("DEBUG_GUILDS")]
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")


denbot = commands.Bot(intents=discord.Intents.all(), debug_guilds=DEBUG_GUILDS)
disabled = ["moderator_commands","pages"]
with os.scandir("/app/src/cogs") as fileList:
    for file in fileList:
        if fnmatch.fnmatch(file,"*.py"):
            if not os.path.splitext(file.name)[0] in disabled:
                denbot.load_extension(f"cogs.{os.path.splitext(file.name)[0]}") 
                print(f"Cog: {os.path.splitext(file.name)[0]} added.")

@denbot.event
async def on_ready():
    print(f"{denbot.user} has successfully connected! (ID: {denbot.user.id})")
    for guild in denbot.guilds:
        print(f"{guild.name} (ID: {guild.id})")


denbot.run(DISCORD_TOKEN) 