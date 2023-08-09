import fnmatch
import os
import discord
import database
from discord.ext import commands
import logging
import sys

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='/app/data/discord.log', encoding='utf-8', mode='w')
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

DEBUG_GUILDS = os.environ.get("DEBUG_GUILDS")
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN") 

denbot = commands.Bot(intents=discord.Intents.all()) #  debug_guilds=[DEBUG_GUILDS]

enabled = ["settings", "autochannel", "converter", "onjoin" ] #  "lfg" "currentlystreaming" 
with os.scandir("cogs") as fileList:
    for file in fileList:
        if fnmatch.fnmatch(file,"*.py"):
            if os.path.splitext(file.name)[0] in enabled:
                denbot.load_extension(f"cogs.{os.path.splitext(file.name)[0]}")
                logger.warning(f"Cog: {os.path.splitext(file.name)[0]} added.")

@denbot.event
async def on_ready():
    logger.info(f"{denbot.user} has successfully connected! (ID: {denbot.user.id})")
    for guild in denbot.guilds:
        database.add_guild(guild.id)

@denbot.event
async def on_guild_join(guild):
    database.add_guild(guild.id)



denbot.run(DISCORD_TOKEN) 