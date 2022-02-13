from discord.ext import commands
import os
from settings import *
import discord


bot = commands.Bot(command_prefix="$")
bot.remove_command("help")

@bot.event
async def on_ready():
    activity = discord.Game(name="sleeping")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("YeeeeeBot online")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(TOKEN)