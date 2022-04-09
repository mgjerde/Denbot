from os import getenv
from discord.ext.commands import context
from discord.ext import commands
from discord.utils import get

LFG_ROLE = getenv('LFG_ROLE')

class Lfg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        lfg_role = get( before.guild.roles, name=LFG_ROLE )
        if str(before.status) in ("online", "idle", "dnd") and str(after.status) == "offline" and lfg_role in after.roles:
            await after.remove_roles(lfg_role)

    @commands.slash_command(default_permission=True, name="lfg", description="Looking for peeps to play with")
    async def lfg(self, ctx: context): 
        lfg_role = get( ctx.author.guild.roles, name=LFG_ROLE )
        await ctx.author.add_roles(lfg_role)
        await ctx.respond("LFG role given!", ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(Lfg(bot))