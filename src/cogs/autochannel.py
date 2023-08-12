import discord
import database
from discord.ext import commands


class Autochannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        db = database.DB
        channel_id = db.get_setting(member.guild.id, "voicechannel")
        if after.channel and after.channel.id == channel_id:
            if member.activity:
                channame = f"🎮 {member.activity.name}"
            else:
                channame = f"💬 {member.name}"
            overwrite = discord.PermissionOverwrite()
            overwrite.manage_channels = True
            overwrite.mute_members = True
            overwrite.move_members = True
            newchan = await member.guild.create_voice_channel(
                channame,
                category=after.channel.category,
                position=(len(after.channel.category.voice_channels) + 1),
                overwrites={member: overwrite},
            )
            await member.move_to(channel=newchan)

            def emptycheck(m, b, a):
                return len(newchan.members) == 0

            await self.bot.wait_for("voice_state_update", check=emptycheck)
            await newchan.delete()


def setup(bot: discord.ext.commands.Bot):
    bot.add_cog(Autochannel(bot))
