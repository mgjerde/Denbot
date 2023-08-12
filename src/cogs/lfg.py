import discord
import database
from discord.ext import commands



class Lfg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        db = database.DB()
        lfg_id = db.get_setting(before.guild.id, 'lfg_role')
        lfg_role = discord.utils.get( before.guild.roles, id=lfg_id )
        print(lfg_role, before.status, after.status, after.roles)
        if str(before.status) in ("online", "idle", "dnd") and str(after.status) == "offline" and lfg_role in after.roles:
            await after.remove_roles(lfg_role)

    @commands.slash_command(default_permission=True, name="lfg", description="Looking for peeps to play with")
    async def lfg(self, ctx: discord.ApplicationContext): 
        lfg_id = database.get_setting(ctx.guild_id, 'lfg_role')

        lfg_role = discord.utils.get( ctx.author.guild.roles, id=lfg_id )
        await ctx.author.add_roles(lfg_role)
        await ctx.respond("LFG role given!", ephemeral=True)


def setup(bot: discord.ext.commands.Bot):
    bot.add_cog(Lfg(bot))