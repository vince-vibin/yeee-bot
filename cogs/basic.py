from discord.ext import commands, tasks
import discord
from discord import app_commands

from .influxdbMetrix import InfluxMetrix
from influx.influxdbExport import sendingCom, sendingH

# setting global var for Embed-Color
global colorEmbed 
colorEmbed = 0x94FFB4

#vars for calling sending func
global cog

cog = "basic"
calledPing = 0
calledBotinfo = 0
calledServerinfo = 0

calledPingH = [0, "ping", cog] 
calledBotinfoH = [0, "serverinfo", cog]
calledServerinfoH = [0, "botinfo", cog]


class Basic(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

    @app_commands.command(name="ping", description="get the ping of the bot") # getting the ping of the bot
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
        await interaction.response.send_message(embed=embed, ephemeral=False)

    @app_commands.command(name="botinfo", description="stalk me") # get info about the bot
    async def botinfo(interaction: discord.Interaction) -> None:
        com = "botinfo"

        #sending Monitoring Info
        global calledBotinfo, calledBotinfoH
        calledBotinfo += 1
        calledBotinfoH[0] += 1
        sendingCom(cog, com, calledBotinfo)

        uptime = InfluxMetrix.uptime
        embed = discord.Embed(colour=colorEmbed, title="About YeeeeeBot")
        embed.add_field(name="Servers active:", value=len(self.bot.guilds), inline=False)
        embed.add_field(name="Uptime:", value=uptime, inline=False)
        embed.add_field(name="Invitelink:", value="https://bit.ly/3wVcOia", inline=False)
        embed.add_field(name="Sourcecode:", value="https://github.com/vince-vibin/yeee-bot", inline=False)
        embed.add_field(name="Feel free to upvote at:", value="https://discordbotlist.com/bots/yeeeebot", inline=False)
        embed.add_field(name="Developer/Dad :desktop:", value="vince_vibin#7429", inline=False)
         
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="serverinfo", description="stalk the sever") # get info about the server
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
        num_voicechannels = len(guild.voice_channels)
        num_textchannels = len(guild.text_channels)
        num_members = guild.member_count
        owner =  guild.get_member(guild.owner_id)
        server_icon = interaction.guild.icon.url
        description = (guild.description)

        embed.set_thumbnail(url=server_icon)
        embed.add_field(name="Server Name", value=guild.name, inline=False)
        embed.add_field(name="Description", value=description)
        embed.add_field(name="Owner", value=owner, inline=False)
        embed.add_field(name="Member Count", value=num_members, inline=False)
        embed.add_field(name="Voice Channels", value=num_voicechannels, inline=True)
        embed.add_field(name="Text Channels", value=num_textchannels, inline=True)
            
        emoji_string = ""
        for e in guild.emojis:
            if e.is_usable():
                emoji_string += str(e)
                if len(emoji_string) > 900:
                    emoji_string = emoji_string + " and more..." # cant send embed fields with > 1024 chars
                    print(len(emoji_string))
                    break

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