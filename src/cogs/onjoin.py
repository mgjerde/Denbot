import discord
import database
from discord.ext import commands


class Onjoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        db = database.DB
        role_id = db.get_setting(member.guild.id, "autorole")
        role = discord.utils.get(member.guild.roles, id=role_id)

        if role:
            await member.add_roles(role)
        else:
            pass
        # Should get a better test probably?


def setup(bot: commands.Bot):
    bot.add_cog(Onjoin(bot))
