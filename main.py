from wsgiref.simple_server import sys_version
from discord.ext import commands, tasks
import os
import discord
from discord.app_commands import AppCommandError
from dotenv import load_dotenv
import pyfiglet

import cogs
from influx.influxdbExport import sendingErrors

# Invite link:
#   https://discord.com/api/oauth2/authorize?client_id=728319090510528602&permissions=277025516544&scope=bot%20applications.commands

# Github Repository 
#   https://github.com/vince-vibin/yeee-bot 

print("Yeeeee Bot called 🫡")
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
    print("    - loading cogs...")
    try: 
        await bot.add_cog(cogs.Basic(bot)) # not the best solution but at this point im to tired
        await bot.add_cog(cogs.Animals(bot))
        await bot.add_cog(cogs.Fun(bot))
        await bot.add_cog(cogs.Games(bot))
        await bot.add_cog(cogs.Help(bot))
        await bot.add_cog(cogs.Reddit(bot))
        await bot.add_cog(cogs.InfluxMetrix(bot))
        print("        OK 👍")
    except:
        print("        FAILED 🥲")

    print("    - starting tasks...")
    try:
        startInfluxMetrix.start()
        print("        OK 👍")
    except:
        print("        FAILED 🥲")

    print("    - loading profile...")
    try:
        activity = discord.Game(name="sleeping")
        await syncFunc()
        await bot.change_presence(status=discord.Status.idle, activity=activity)
        print("        OK 👍")
    except:
        print("        FAILED 🥲")

    print("[INFO] running on ", sys_version)
    
    ascii_banner = pyfiglet.figlet_format("YeeeeBot online!")
    print(ascii_banner)

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

@tasks.loop(minutes=10)
async def startInfluxMetrix():
    await cogs.InfluxMetrix.exportServer(cogs.InfluxMetrix, bot)
    await cogs.InfluxMetrix.getSysData(cogs.InfluxMetrix)
    await cogs.InfluxMetrix.getUptime(cogs.InfluxMetrix)
    return
    


bot.run(TOKEN)