from discord.ext.commands import context
from discord.ext import commands
import discord.utils
from dotenv import load_dotenv
from os import getenv
load_dotenv()
ROLE = getenv('STREAMING_ROLE')

class CurrentlyStreaming(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        streaming_role = discord.utils.get( before.guild.roles, name=ROLE )
        isstreaming = False
        for activity in after.activities:
            if isinstance(activity, discord.Streaming): # Making sure it's the correct activity
                isstreaming = True
        await after.add_roles(streaming_role) if isstreaming else await after.remove_roles(streaming_role)
                

def setup(bot: commands.Bot):
    bot.add_cog(CurrentlyStreaming(bot))