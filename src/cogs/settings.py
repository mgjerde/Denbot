import configparser
import discord

config = configparser.ConfigParser()
config.read('settings.ini')



class SettingsView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
   
    @discord.ui.button(label="Currently playing", style=discord.ButtonStyle.primary, emoji="📽️", custom_id="cp_button")
    async def cp_callback(self, button, interaction):
        cp_dropdown = Dropdown(self)
        for role in interaction.guild.roles:
            if role.name != "@everyone": cp_dropdown.add_option(label=role.name,value=role.id,)
        cp_dropdown.custom_id = "streaming_role"
        cp_dropdown.placeholder = "Set currently streaming role"
        cp_view = discord.ui.View()
        cp_view.add_item(cp_dropdown)
        await interaction.response.edit_message(view=cp_view)

    @discord.ui.button(label="Auto role on join", style=discord.ButtonStyle.primary, emoji="🆕", custom_id="auto_button")
    async def auto_callback(self, button, interaction):
        auto_dropdown = Dropdown(self)
        for role in interaction.guild.roles:
            if role.name != "@everyone": auto_dropdown.add_option(label=role.name,value=role.id,)
        auto_dropdown.custom_id = "auto_role"
        auto_dropdown.placeholder = "Set auto role"       
        auto_view = discord.ui.View()
        auto_view.add_item(auto_dropdown)     
        await interaction.response.edit_message(view=auto_view)

    @discord.ui.button(label="LFG Role", style=discord.ButtonStyle.primary, emoji="🕹️", custom_id="lfg_button")
    async def lfg_callback(self, button, interaction):
        lfg_dropdown = Dropdown(self)
        for role in interaction.guild.roles:
            if role.name != "@everyone": lfg_dropdown.add_option(label=role.name,value=role.id,)
        lfg_dropdown.custom_id = "lfg_role"
        lfg_dropdown.placeholder = "Set LFG role"       
        lfg_view = discord.ui.View()
        lfg_view.add_item(lfg_dropdown)     
        await interaction.response.edit_message(view=lfg_view)
    
    @discord.ui.button(label="Auto Channel", style=discord.ButtonStyle.primary, emoji="🎙️", custom_id="ac_button")
    async def ac_callback(self, button, interaction):
        ac_dropdown = Dropdown(self)
        for channel in interaction.guild.voice_channels:
            ac_dropdown.add_option(label=channel.name,value=channel.id,)
        ac_dropdown.custom_id = "ac_channel"
        ac_dropdown.placeholder = "Set autochannel"       
        ac_view = discord.ui.View()
        ac_view.add_item(ac_dropdown)     
        await interaction.response.edit_message(view=ac_view)

class Dropdown(discord.ui.Select):
    def __init__(self, bot):
        self.bot = bot 
        super().__init__(
            min_values=1,
            max_values=1,
            options=[],
        )

    async def callback(self, interaction: discord.Interaction):
        config[interaction.guild_id] = {self.custom_id: self.values[0]}
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)
        await interaction.response.edit_message(view=SettingsView())
        

class Settings(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(SettingsView())

    @discord.ext.commands.slash_command(name="settings", description="Change the settings on the server")
    async def settings_command(
        self,
        ctx: discord.ApplicationContext,):
        
        await ctx.response.send_message(view=SettingsView(), ephemeral=True) if ctx.author == ctx.guild.owner else await ctx.response.send_message("Only the server administrator can run this command!", ephemeral=True)


def setup(bot: discord.ext.commands.Bot):
    bot.add_cog(Settings(bot))