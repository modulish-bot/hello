import discord
from discord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot, config_dir: str):
        self.bot = bot

    @discord.slash_command(name="hello")
    async def hello(self, ctx):
        await ctx.respond("Hello, world!")

def setup(bot: commands.Bot, config_dir: str = None):
    if config_dir is None:
        config_dir = globals().get('PLUGIN_CONFIG_DIR', '<unknown>')
    bot.add_cog(Hello(bot, config_dir))