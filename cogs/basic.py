from discord.ext import commands, tasks
import discord
from discord import app_commands

from .influxdbMetrix import InfluxMetrix
from influx.influxdbExport import sendingCom, sendingH, sendingErrors

# setting global var for Embed-Color
global colorEmbed 
colorEmbed = 0x94FFB4

#vars for calling sending func
global cog

cog = "basic"
calledPing = 0
calledBotinfo = 0
calledServerinfo = 0
threwError = 0

calledPingH = [0, "ping", cog] 
calledBotinfoH = [0, "serverinfo", cog]
calledServerinfoH = [0, "botinfo", cog]


class Basic(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

    @commands.Cog.listener() # defining the error message
    async def on_command_error(self, ctx, ex):
        print(ex)
        colour=0xFF0000 # color for the error message

        global threwError
        threwError += 1

        send = ["exHandler", threwError, ex]

        sendingErrors(send)

        embed = discord.Embed(colour=colour)
        embed.add_field(name="Bruh", value="It seems like you are to dumb to use this command so please leave me alone.", inline=False)
        embed.set_footer(text=ex)
        await ctx.send(embed=embed)

    @app_commands.command(name="ping") # getting the ping of the bot
    async def ping(interaction: discord.Interaction) -> None:
        com = "ping"
        #sending calledNUM Metric to influxdb.py
        global calledPing, calledPingH
        calledPing += 1

        #setting for called per hour
        calledPingH[0] += 1

        sendingCom(cog, com, calledPing)
        ping = format(round(self.bot.latency * 1000))

        embed = discord.Embed(colour=colorEmbed)
        embed.add_field(name="Pong you Dumb!", value="{} ms".format(ping), inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="botinfo") # get info about the bot
    async def botinfo(interaction: discord.Interaction) -> None:
        com = "botinfo"

        #sending Monitoring Info
        global calledBotinfo, calledBotinfoH
        calledBotinfo += 1
        calledBotinfoH[0] += 1
        sendingCom(cog, com, calledBotinfo)

        uptime = await InfluxMetrix.getUptime(InfluxMetrix)
        embed = discord.Embed(colour=colorEmbed, title="About YeeeeeBot")
        embed.add_field(name="Servers active:", value=len(self.bot.guilds), inline=False)
        embed.add_field(name="Uptime:", value=uptime, inline=False)
        embed.add_field(name="Invitelink:", value="https://bit.ly/3wVcOia", inline=False)
        embed.add_field(name="Sourcecode:", value="https://github.com/vince-vibin/yeee-bot", inline=False)
        embed.add_field(name="Feel free to upvote at:", value="https://discordbotlist.com/bots/yeeeebot", inline=False)
        embed.add_field(name="Developer/Dad :desktop:", value="vince_vibin#7429", inline=True)
         
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="serverinfo") # get info about the server
    async def serverinfo(interaction: discord.interactions.Interaction) -> None:
        com = "serverinfo"

        #sending calledNUM Metric to influxdb.py
        global calledServerinfo, calledServerinfoH
        calledServerinfo += 1

        #setting for called per hour
        calledServerinfoH[0] += 1

        sendingCom(cog, com, calledServerinfo)

        guild = interaction.guild
        embed = discord.Embed(colour=colorEmbed)
        numb_voicechannels = len(guild.voice_channels)
        numb_textchannels = len(guild.text_channels)
        numb_member = (guild.member_count)
        owner = interaction.guild.owner
        server_icon = interaction.guild.icon.url
        description = (guild.description)

        embed.set_thumbnail(url=server_icon)
        embed.add_field(name="Server Name", value=guild.name, inline=False)
        embed.add_field(name="Description", value=description)
        embed.add_field(name="Owner", value=owner, inline=False)
        embed.add_field(name="Member Count", value=numb_member, inline=False)
        embed.add_field(name="Voice Channels", value=numb_voicechannels, inline=True)
        embed.add_field(name="Text Channels", value=numb_textchannels, inline=True)
            
        emoji_string = ""
        for e in guild.emojis:
            if e.is_usable():
                emoji_string += str(e)
        embed.add_field(name="Emojies",
                        value=emoji_string or "No emojis setup", inline=False)

        await interaction.response.send_message(embed=embed, ephemeral=True)

    @tasks.loop(hours=1)
    async def exporterH():
        global calledPingH, calledBotinfoH, calledServerinfoH
        send = [calledPingH, calledBotinfoH, calledServerinfoH]
        i = 0

        while i < len(send): #looping throught send array
            sendingH(send[i])
            i = i + 1

        calledPingH[0] = 0 #reseting all values 
        calledBotinfoH[0] = 0
        calledServerinfoH[0] = 0

    bot.tree.add_command(ping, override=True)
    bot.tree.add_command(serverinfo, override=True)
    bot.tree.add_command(botinfo, override=True) 
    
    exporterH.start()

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Basic(bot))