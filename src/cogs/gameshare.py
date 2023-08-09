import discord

from discord.ext import commands
from discord.commands import Option

# from discord import context
import json
import urllib.request

# from discord import SlashCommandGroup


class GameSelect(discord.ui.Select):
    def __init__(self):
        super().__init__(
            placeholder="Search results, select your game",
            min_values=1,
            max_values=1,
            options=[],
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(content=self.values[0])


class GameView(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Share", style=discord.ButtonStyle.gray)
    async def share(self, button: discord.ui.Button, interaction: discord.Interaction):
        pass

    @discord.ui.button(label="Donate", style=discord.ButtonStyle.gray, emoji="🎁")
    async def donate(self, button: discord.ui.Button, interaction: discord.Interaction):
        pass


class GameButton(discord.ui.Button):
    def __init__(self, buttonname: str, emoji: str):
        """
        A button for one role. `custom_id` is needed for persistent views.
        """
        super().__init__(
            label=buttonname, style=discord.enums.ButtonStyle.grey, emoji=emoji
        )

    async def callback(self, interaction: discord.Interaction):
        pass


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        default_permission=True,
        name="addgame",
        description="Donate a game to the community",
    )
    async def addgame(
        self, ctx: commands.context, game: Option(str, "What game do you want to add?")
    ):
        # This will crash if non-basic letters like æøå is being used, library bug or server settings? halp
        query = game.replace(" ", "%20")
        url = urllib.request.urlopen(
            f"https://api.rawg.io/api/games?key=4c63ca18e8234c849fdc082eb88b6925&search={query}&page_size=5"
        )
        rawglist = json.load(url)

        selectlist = []
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

    async def callback(self, interaction: discord.Interaction):
        pass


def setup(bot: commands.Bot):
    bot.add_cog(Games(bot))
