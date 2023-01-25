from wsgiref.simple_server import sys_version
from discord.ext import commands
import os
import discord
from discord.app_commands import AppCommandError
from dotenv import load_dotenv
from influx.influxdbExport import sendingErrors
import pyfiglet

import cogs

# Invite link:
#   https://discord.com/api/oauth2/authorize?client_id=728319090510528602&permissions=277025516544&scope=bot%20applications.commands

# Github Repository 
#   https://github.com/vince-vibin/yeee-bot 

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)
tree = bot.tree
TOKEN = os.getenv("DISCORD_TOKEN")

threwError = 0

async def syncFunc():
    await bot.tree.sync()

@bot.event
async def on_ready():
    await bot.add_cog(cogs.Basic(bot)) # not the best solution but at this point im to tired
    await bot.add_cog(cogs.Animals(bot))
    await bot.add_cog(cogs.Fun(bot))
    await bot.add_cog(cogs.Games(bot))
    await bot.add_cog(cogs.Help(bot))
    await bot.add_cog(cogs.Reddit(bot))
    await bot.add_cog(cogs.InfluxMetrix(bot))

    activity = discord.Game(name="sleeping")
    await syncFunc()
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    
    ascii_banner = pyfiglet.figlet_format("YeeeeBot online!")
    print(ascii_banner)
    print("running on Python ", sys_version)

@tree.error
async def on_app_command_error(interaction : discord.Interaction, error : AppCommandError):
    print(error)
    colour=0xFF0000 # color for the error message

    global threwError
    threwError += 1

    send = ["exHandler", threwError, error]

    sendingErrors(send)

    embed = discord.Embed(colour=colour)
    embed.add_field(name="Bruh :face_with_raised_eyebrow:", value="It seems like you are to stupid to use this command", inline=False)
    embed.add_field(name="maybe try /help", value="or send the errormessage in the footer to my dad: https://discord.gg/5WfYJje")
    embed.set_footer(text=error)
    await interaction.response.send_message(embed=embed, ephemeral=True)


  




bot.run(TOKEN)