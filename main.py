from wsgiref.simple_server import sys_version
from discord.ext import commands
import os
import discord
from dotenv import load_dotenv

bot = commands.Bot(command_prefix="$")
bot.remove_command("help")

load_dotenv()
TOKEN = os.getenv("DISCORD_token")

@bot.event
async def on_ready():
    print("Python Version: ", sys_version)
    activity = discord.Game(name="sleeping")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("YeeeeeBot online")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)