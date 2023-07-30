import fnmatch
import os
import discord
import sqlite3
import database
from discord.ext import commands

DEBUG_GUILDS = os.environ.get("DEBUG_GUILDS")
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN") 

denbot = commands.Bot(intents=discord.Intents.all(), debug_guilds=[DEBUG_GUILDS])

enabled = ["settings", "autochannel", "converter", "onjoin" ] #  "lfg" "currentlystreaming" 
with os.scandir("/app/src/cogs") as fileList:
    for file in fileList:
        if fnmatch.fnmatch(file,"*.py"):
            if os.path.splitext(file.name)[0] in enabled:
                # denbot.add_cog(f"{os.path.splitext(file.name)[0]}")
                denbot.load_extension(f"cogs.{os.path.splitext(file.name)[0]}")
                print(f"Cog: {os.path.splitext(file.name)[0]} added.")

@denbot.event
async def on_ready():
    print(f"{denbot.user} has successfully connected! (ID: {denbot.user.id})")
    database.create_table()
    for guild in denbot.guilds:
        database.add_guild(guild.id)


denbot.run(DISCORD_TOKEN) 