from discord import colour, Embed, Member

import random
from discord.ext.commands import context
from discord.ext import commands

from discord.commands import permissions

class Winter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.user_command(name="Throw snowball")
    async def snowball(self, ctx: context, member: Member):  # user commands return the member
        
        throw = random.randint(0,1)
        if throw == 0:
            targets = ["It barely grazes the shoulder.", "It hits straight in the face! ", "It hits the kneecap.", "It splatters all over the chest."]
            result = random.choice(targets)
        else:
            result = "It misses."
        
        
        snowball = Embed(title="Snowball fight!", colour=colour.Color.lighter_grey() )
        snowball.set_footer(text=f"{ctx.author.name} throws a snowball at {member.name}. {result}",icon_url="https://icons.iconarchive.com/icons/arrioch/christmas/128/snowball-icon.png")
        await ctx.respond(embed=snowball)


def setup(bot: commands.Bot):
    bot.add_cog(Winter(bot))