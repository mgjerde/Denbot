import discord
import database
from discord.ext import commands
class CurrentlyStreaming(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        streaming_id = database.get_setting(before.guild.id, 'streaming_role')
        streaming_role = discord.utils.get( before.guild.roles, id=streaming_id )
        isstreaming = False
        for activity in after.activities:
            if isinstance(activity, discord.Streaming): 
                isstreaming = True
        await after.add_roles(streaming_role) if isstreaming else await after.remove_roles(streaming_role)
        # TODO: Should add a check for if streaming role is not set yet

def setup(bot: commands.Bot):
    bot.add_cog(CurrentlyStreaming(bot))