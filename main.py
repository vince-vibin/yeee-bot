from wsgiref.simple_server import sys_version
from discord.ext.commands import Bot
import os
import discord
from dotenv import load_dotenv
from discord_slash import SlashCommand

# Invite link:
#   https://discord.com/api/oauth2/authorize?client_id=728319090510528602&permissions=277025516544&scope=bot%20applications.commands

# Github Repository 
#   https://github.com/vince-vibin/yeee-bot 

intents = discord.Intents.default()
intents.members = True

bot = Bot(command_prefix="$", intents=intents)
slash = SlashCommand(bot, sync_commands=True)
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