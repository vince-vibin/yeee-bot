from wsgiref.simple_server import sys_version
from discord.ext import commands
import os
import discord
from discord import *
from dotenv import load_dotenv
import cogs.basic
import cogs.animals

# Invite link:
#   https://discord.com/api/oauth2/authorize?client_id=728319090510528602&permissions=277025516544&scope=bot%20applications.commands

# Github Repository 
#   https://github.com/vince-vibin/yeee-bot 

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

TOKEN = os.getenv("DISCORD_TOKEN")

async def syncFunc():
    print(bot.cogs)
    await bot.tree.sync()
        
@bot.event
async def on_ready():
    print("Python Version: ", sys_version)
    await bot.add_cog(cogs.basic.Basic(bot))
    await bot.add_cog(cogs.animals.Animals(bot))
    activity = discord.Game(name="sleeping")
    await syncFunc()
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("YeeeeeBot online")

""" for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}') """
  




bot.run(TOKEN)