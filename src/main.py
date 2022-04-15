import fnmatch
import os
import discord
from discord.ext import commands
import configparser


config = configparser.ConfigParser()
config.read('settings.ini')


denbot = commands.Bot(intents=discord.Intents.all(), debug_guilds=[(int(config['BASE']['DEBUG_GUILD']))])

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


denbot.run(config['BASE']['DISCORD_TOKEN']) 