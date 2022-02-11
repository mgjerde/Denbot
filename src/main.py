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
denbot.load_extension("moderator_commands")
denbot.load_extension("seasonal_winter")
denbot.load_extension("lfg")
# denbot.load_extension("gameshare")

denbot.run(TOKEN) 