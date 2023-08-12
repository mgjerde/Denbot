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
        eventembed = discord.Embed(title=event.name, description=event.description, url=event.url, timestamp=event.created_at)
        if event.cover:
            eventembed.set_thumbnail(url=event.cover)
        eventembed.add_field(name="When:", value=f"<t:{int(event.start_time.timestamp())}>")


        await event.guild.get_channel(channel_id).send(embed=eventembed)


def setup(bot: commands.Bot):
    bot.add_cog(EventListener(bot))






# embed = discord.Embed(title=f"{amount} {unit} is:",  color=discord.Color.random())
#         for convertedunit in units[unit].keys():
#             if callable(units[unit][convertedunit]):
#                 embed.add_field(name=f"{convertedunit}", value=units[unit][convertedunit](amount) , inline=True)
#             else: 
#                 embed.add_field(name=f"{convertedunit}", value=round(units[unit][convertedunit]*amount,3) , inline=True)
#         await ctx.response.send_message(embed=embed)

# embed = discord.Embed(title="Title",
#                       url="https://example.com",
#                       colour=0x00b0f4,
#                       timestamp=datetime.now())

# embed.add_field(name="Field Name",
#                 value="This is the field value.")
# embed.add_field(name="The first inline field.",
#                 value="This field is inline.",
#                 inline=True)
# embed.add_field(name="The second inline field.",
#                 value="Inline fields are stacked next to each other.",
#                 inline=True)
# embed.add_field(name="The third inline field.",
#                 value="You can have up to 3 inline fields in a row.",
#                 inline=True)

# embed.set_thumbnail(url="https://dan.onl/images/emptysong.jpg")

# embed.set_footer(text="Example Footer",
#                  icon_url="https://slate.dan.onl/slate.png")

# await ctx.send(embed=embed)