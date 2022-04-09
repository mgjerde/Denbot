import fnmatch
import os
from dotenv import load_dotenv
from os import getenv
import discord
from discord.ext import commands
# from discord.ext.commands import context


load_dotenv()
DEBUG_GUILD = list()
DEBUG_GUILD.append(int(getenv('DEBUG_GUILD')))
TOKEN = getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
denbot = commands.Bot(intents=intents, debug_guilds=DEBUG_GUILD)

with os.scandir("src/cogs") as fileList:
    for file in fileList:
        if fnmatch.fnmatch(file,"*.py"):
            denbot.load_extension(f"cogs.{os.path.splitext(file.name)[0]}")
            print(f"Cog: {os.path.splitext(file.name)[0]} added.")

@denbot.event
async def on_ready():
    print(f"{denbot.user} has successfully connected! (ID: {denbot.user.id})")
    for guild in denbot.guilds:
        print(f"{guild.name} (ID: {guild.id})")


denbot.run(TOKEN) 