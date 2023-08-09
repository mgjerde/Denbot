from discord.ui import View, Select
from discord import command, Interaction, Embed, Color
from discord.commands import Option, slash_command
from discord.ext import commands
import urllib.request
import json


class GameSelect(Select):
    def __init__(self):
        super().__init__(
            placeholder="Search results, select your game",
            min_values=1,
            max_values=1,
            options=[],
        )

    async def callback(self, interaction: Interaction):
        gameid = self.values[0]
        apicall = urllib.request.urlopen(
            f"https://api.rawg.io/api/games/{gameid}?key=4c63ca18e8234c849fdc082eb88b6925"
        )
        gameinfo = json.load(apicall)

        embed = Embed(
            title=gameinfo["name"],
            url="https://rawg.io/games/" + gameinfo["slug"],
            description=gameinfo["description_raw"].replace("\n", ""),
            color=Color.random(),
        )
        embed.set_thumbnail(url=gameinfo["background_image_additional"])
        embed.add_field(name="Release date:", value=gameinfo["released"], inline=True)
        embed.add_field(
            name="Average playtime:",
            value=str(gameinfo["playtime"]) + " hours",
            inline=True,
        )
        embed.add_field(
            name="Metacritic score:", value=gameinfo["metacritic"], inline=True
        )
        await interaction.response.send_message(embeds=[embed])


class GameView(View):
    def __init__(self):
        super().__init__()


class Lookup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        default_permission=True, name="lookup", description="Denbot lookup utility"
    )
    async def addgame(
        self,
        ctx: commands.context,
        type: Option(str, "What do you want to lookup?", choices=["Game"]),
        title: Option(str, "What is the title you are trying to look up"),
    ):
        query = title.replace(" ", "%20")
        apicall = urllib.request.urlopen(
            f"https://api.rawg.io/api/games?key=4c63ca18e8234c849fdc082eb88b6925&search={query}&page_size=10"
        )
        rawglist = json.load(apicall)

        if rawglist["results"]:
            gameselector = GameSelect()
            searchview = GameView()
            searchview.add_item(gameselector)

            for game in rawglist["results"]:
                gameselector.add_option(
                    label=f"{game['name']}", value=game["id"], emoji="🎮"
                )

            await ctx.respond("Game lookup", ephemeral=True, view=searchview)
        else:
            await ctx.respond("No games found...", ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(Lookup(bot))
