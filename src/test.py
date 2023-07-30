import discord
client = discord.Client()
@client.event
async def on_ready() :
    guilds = [guild.id for guild in client.guilds]
    print(f"The {client.user.name} bot is in {len(guilds)} Guilds.\nThe guilds ids list : {guilds}")

client.run("OTUyMzY4Mzc3OTg3NDY5Mzcy.GmuLs4._6SIrUIql4uMIQ8qmyFOxCGX5zRkR8aN77bOrU")