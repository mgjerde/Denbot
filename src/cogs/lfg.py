import configparser
import discord



class Lfg(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.ext.commands.Cog.listener()
    async def on_presence_update(self, before, after):
        config = configparser.ConfigParser()
        config.read('settings.ini')

        lfg_role = discord.utils.get( before.guild.roles, id=int(config[str(before.guild.id)]['LFG_ROLE']) )
        if str(before.status) in ("online", "idle", "dnd") and str(after.status) == "offline" and lfg_role in after.roles:
            await after.remove_roles(lfg_role)

    @discord.ext.commands.slash_command(default_permission=True, name="lfg", description="Looking for peeps to play with")
    async def lfg(self, ctx: discord.ApplicationContext): 
        config = configparser.ConfigParser()
        config.read('settings.ini')

        lfg_role = discord.utils.get( ctx.author.guild.roles, id=int(config[str(ctx.guild.id)]['LFG_ROLE']) )
        await ctx.author.add_roles(lfg_role)
        await ctx.respond("LFG role given!", ephemeral=True)


def setup(bot: discord.ext.commands.Bot):
    bot.add_cog(Lfg(bot))