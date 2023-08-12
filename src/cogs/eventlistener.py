import discord
import database
from discord.ext import commands


class EventListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_scheduled_event_create(self, event):
        db = database.DB
        channel_id = db.get_setting(event.guild.id, "eventchannel")
        eventembed = discord.Embed(
            title=event.name,
            description=event.description,
            url=event.url,
            timestamp=event.created_at,
        )
        if event.cover:
            eventembed.set_thumbnail(url=event.cover)
        eventembed.set_footer(
            text="Created at",
        )
        eventembed.add_field(
            name="When:", value=f"<t:{int(event.start_time.timestamp())}>", inline=False
        )
        eventembed.add_field(name="Where:", value=f"{event.location}")

        await event.guild.get_channel(channel_id).send(embed=eventembed)


def setup(bot: commands.Bot):
    bot.add_cog(EventListener(bot))
