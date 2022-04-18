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
            if member.activity:
                channame = F"🎮 {member.activity.name}"
            else:
                channame = F"💬 {member.name}"
            overwrite = discord.PermissionOverwrite()
            overwrite.manage_channels = True
            overwrite.mute_members = True
            overwrite.move_members = True
            newchan = await member.guild.create_voice_channel(channame,category=after.channel.category,position=(len(after.channel.category.voice_channels)+1),overwrites={member:overwrite})
            await member.move_to(channel=newchan)

            def emptycheck(m, b, a):
                return len(newchan.members) == 0

            await self.bot.wait_for('voice_state_update',check=emptycheck)
            await newchan.delete()

            
      
    # create channel when joining specific channel and move user ✔
        # Change name based on Game Played ✔
        # Give access to change name etc ✔
    # Delete channel when leaving empty channel ✔



def setup(bot: discord.ext.commands.Bot):
    bot.add_cog(Autochannel(bot))