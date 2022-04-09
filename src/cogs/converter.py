from discord import ApplicationContext, AutocompleteContext, Embed, Color, utils
# from discord.commands import Option, slash_command
# from discord.ext import commands
# import discord
from discord.ui import View, Select
from discord import command, Interaction, Embed, Color
from discord.commands import Option, slash_command
from discord.ext import commands
import urllib.request
import json
import discord
import math

def temp_c2f(celsius):
    return round(1.8 * celsius + 32,2)
def temp_c2k(celsius):
    return celsius + 10
def temp_f2c(fahrenheit):
    return round((fahrenheit-32)/1.8,2)
def temp_f2k(fahrenheit):
    return round((fahrenheit-32)/1.8+273.15,2)

def cm2feetinches(cm):
    totalinches = cm * 0.393700787
    return f"{int(totalinches // 12)}' {round(totalinches % 12,3)}\""
    

units = {
    
        "Gram (g)": { "Ounce (oz)": 0.03527396198, "Pound (lb)": 0.00220462262  },
        "Kilogram (kg)": { "Ounce (oz)": 35.2739619, "Pound (lb)": 2.20462262  },
        "Ounce (oz)": { "Gram (g)": 28.3495231, "Pound (lb)": 0.0625  },
        "Pound (lb)": { "Gram (g)": 453.59237, "Kilogram (kg)": 0.45359237, "Ounce (oz)": 16  },
        "Centimeters (cm)": {"Feet and inches": cm2feetinches  },
        "Meters (m)":{ "Feet (ft)": 3.2808399, "Inches (in)": 39.3700787, "Yard (yd)": 1.0936133},
        "Kilometers (km)":{"Yard (yd)": 1093.6133, "Mile (mi)": 0.621371192},
        "Feet (ft)":{"Meters (m)": 0.3048, "Inches (in)": 12, "Yard (yd)": 0.333333333},
        "Inches (in)":{"Meters (m)": 0.0254, "Feet (ft)": 0.0833333333, "Yard (yd)": 0.0277777778, "Mile (mi)": 0.000015782828},
        "Yard (yd)":{"Meters (m)": 0.9144, "Feet (ft)": 3, "Inches (in)": 36, "Mile (mi)": 0.000568181818},
        "Mile (mi)":{ "Kilometers (km)":1.609344, "Feet (ft)": 5280 , "Yard (yd)": 1760},
   
        "Celsius (°C)": {"Fahrenheit (°F)": temp_c2f, "Kelvin (K)": temp_c2k},
        "Fahrenheit (°F)": {"Celsius (°C)": temp_f2c, "Kelvin (K)": temp_f2k}
}


async def unit_from(ctx: AutocompleteContext):
    return [unit for unit in units.keys() if ctx.value.lower() in unit.lower()]

class Converter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="convert", description="Conceptual converter")
    async def convert_command(
        self,
        ctx: ApplicationContext,
        unit: Option(str, "Pick an unit", autocomplete=unit_from),
        amount: Option(float,"What amount?"),
        ):
        embed = Embed(title=f"{amount} {unit} is:",  color=Color.random())
        for convertedunit in units[unit].keys():
            if callable(units[unit][convertedunit]):
                embed.add_field(name=f"{convertedunit}", value=units[unit][convertedunit](amount) , inline=True)
            else:
                embed.add_field(name=f"{convertedunit}", value=round(units[unit][convertedunit]*amount,3) , inline=True)
        await ctx.response.send_message(embeds=[embed])

def setup(bot: commands.Bot):
    bot.add_cog(Converter(bot))