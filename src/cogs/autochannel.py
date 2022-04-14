import discord
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

class Autochannel(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @discord.ext.commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        
        if after.channel and after.channel.id == int(config[str(member.guild.id)]['AC_CHANNEL']):
            print(f"{member.name} went from {before.channel} to {after.channel} -- {member.guild.id}")

        
    # create channel when joining specific channel and move user
        # Change name based on Game Played
        # Give access to change name etc
    # Delete channel when leaving empty channel



def setup(bot: discord.ext.commands.Bot):
    bot.add_cog(Autochannel(bot))