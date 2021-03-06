from discord.ext import commands, tasks
import discord
from discord_slash import cog_ext, SlashContext

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
    def __init__(self, bot):
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


    @cog_ext.cog_slash(name="ping", description="*Happy Table-Tennis noises*") # getting the ping of the bot
    async def ping(self, ctx: SlashContext):
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
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="botinfo", description="Get info about the life of YeeeeeBot") # get info about the bot
    async def botinfo(self, ctx: SlashContext):
        com = "botinfo"
        #sending calledNUM Metric to influxdb.py
        global calledBotinfo, calledBotinfoH
        calledBotinfo += 1
        #setting for called per hour
        calledBotinfoH[0] += 1
        sendingCom(cog, com, calledBotinfo)

        from .influxdbMetrix import timeStamp

        embed = discord.Embed(colour=colorEmbed, title="About YeeeeeBot")
        embed.add_field(name="Servers active:", value=len(self.bot.guilds), inline=False)
        embed.add_field(name="Uptime:", value=timeStamp, inline=False)
        embed.add_field(name="Invitelink:", value="https://bit.ly/3wVcOia", inline=False)
        embed.add_field(name="Sourcecode:", value="https://github.com/vince-vibin/yeee-bot", inline=False)
        embed.add_field(name="Feel free to upvote at:", value="https://discordbotlist.com/bots/yeeeebot", inline=False)
        embed.add_field(name="Developer/Dad :desktop:", value="vince_vibin#7429", inline=True) 
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="serverinfo", description="get information about the Server") # get info about the server
    async def serverinfo(self, ctx: SlashContext):
        com = "serverinfo"

        #sending calledNUM Metric to influxdb.py
        global calledServerinfo, calledServerinfoH
        calledServerinfo += 1

        #setting for called per hour
        calledServerinfoH[0] += 1

        sendingCom(cog, com, calledServerinfo)

        guild = ctx.guild
        embed = discord.Embed(colour=colorEmbed)
        numb_voicechannels = len(guild.voice_channels)
        numb_textchannels = len(guild.text_channels)
        numb_member = (guild.member_count)
        owner = ctx.guild.owner
        server_icon = ctx.guild.icon_url
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

        await ctx.send(embed=embed)

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
        
    exporterH.start()
def setup(bot):
    bot.add_cog(Basic(bot))