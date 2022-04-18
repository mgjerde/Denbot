import configparser
import discord

class CurrentlyStreaming(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.ext.commands.Cog.listener()
    async def on_presence_update(self, before, after):
        config = configparser.ConfigParser()
        config.read('settings.ini')

        streaming_role = discord.utils.get( before.guild.roles, id=int(config[str(before.guild.id)]['STREAMING_ROLE']) )
        isstreaming = False
        for activity in after.activities:
            if isinstance(activity, discord.Streaming): 
                isstreaming = True
        await after.add_roles(streaming_role) if isstreaming else await after.remove_roles(streaming_role)
        # TODO: Should add a check for if streaming role is not set yet

def setup(bot: discord.ext.commands.Bot):
    bot.add_cog(CurrentlyStreaming(bot))