import discord
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

class Onjoin(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @discord.ext.commands.Cog.listener()
    async def on_member_join(self, member):
        await member.add_roles(discord.utils.get( member.guild.roles, id=int(config[str(member.guild.id)]['AUTO_ROLE']) ))
        # Needs a check if role is set


def setup(bot: discord.ext.commands.Bot):
    bot.add_cog(Onjoin(bot))