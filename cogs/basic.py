from discord.ext import commands
import discord

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() # defining the error message
    async def on_command_error(self, ctx, ex):
        print(ex)
        colour=0xFF0000

        embed = discord.Embed(colour=colour)
        embed.add_field(name="Bruh", value="It seems like you are to dumb to use this command so please leave me alone.", inline=False)
        await ctx.send(embed=embed)


    @commands.command(description="*Happy Table-Tennis noises*",brief="*Happy Table-Tennis noises*") # getting the ping of the bot
    async def ping(self, ctx):
        colour=0x94FFB4

        embed = discord.Embed(colour=colour)
        embed.add_field(name="Pong you Dumb!", value=format(round(self.bot.latency * 1000)), inline=False)
        await ctx.send(embed=embed)

    @commands.command(description="Something you want the bot to say. Cause youre too afraid to.",brief="Something you want the bot to say. Cause youre to afraid to say it.") # the bot is saying a profided string
    async def say(self, ctx, *args):
        if len(args) > 0:
            colour=0x94FFB4

            embed = discord.Embed(colour=colour)
            embed.add_field(name="Quote:", value=" ".join(args), inline=False)
            await ctx.send(embed=embed)
        else:
            colour=0xFF0000

            embed = discord.Embed(colour=colour)
            embed.add_field(name="Bruh", value="You need to add a argument you Dumbass", inline=False)
            await ctx.send(embed=embed)

    @commands.command(description="Get info about the life of YeeeeeBot",brief="Get info about the life of YeeeeeBot") # get info about the bot
    async def botinfo(self, ctx):
        colour=0x94FFB4

        embed = discord.Embed(colour=colour, title="About YeeeeeBot")
        embed.add_field(name="Servers active:", value=len(self.bot.guilds), inline=False)
        embed.add_field(name="Instagram :camera_with_flash:", value="https://www.instagram.com/yeeee.bot", inline=True)
        embed.add_field(name="Twitter :dove:", value="https://twitter.com/bot_yeee", inline=True)
        embed.add_field(name="Buissnes Mail :chart_with_upwards_trend:", value="yeeeeebot@gmail.com", inline=True)
        embed.add_field(name="Developer/Dad :desktop:", value="YeeeeeBoi", inline=True)
        embed.add_field(name="Instagram :camera_with_flash:", value="https://www.instagram.com/einserdnuss", inline=True)
        await ctx.send(embed=embed)

    @commands.command(description="Get server status",brief="Get server status") # get info about the server
    async def serverinfo(self, ctx, *args):
        guild = ctx.guild
        embed = discord.Embed(colour=0xA8FFD5)
        numb_voicechannels = len(guild.voice_channels)
        numb_textchannels = len(guild.text_channels)
        numb_member = len(guild.members)
        owner = (guild.owner)
        server_icon = ctx.guild.icon_url
        server_region = (guild.region)
        description = (guild.description)
        max_members = (guild.max_members)
        system_channel = (guild.system_channel)
        rules_channel = (guild.rules_channel)
        afk_channel = (guild.afk_channel)

        embed.set_thumbnail(url=server_icon)
        embed.add_field(name="Server Name", value=guild.name, inline=False)
        embed.add_field(name="Region", value=server_region)
        embed.add_field(name="Owner", value=owner, inline=False)
        embed.add_field(name="Voice Channels", value=numb_voicechannels, inline=True)
        embed.add_field(name="Text Channels", value=numb_textchannels, inline=False)
        embed.add_field(name="System Channel", value=system_channel)
        embed.add_field(name="Rules Channel", value=rules_channel)
        embed.add_field(name="AFK Channel", value=afk_channel)
        embed.add_field(inline=False, name="Member Count", value=numb_member)
            
        emoji_string = ""
        for e in guild.emojis:
            if e.is_usable():
                emoji_string += str(e)
        embed.add_field(name="Emojies",
                        value=emoji_string or "No emojis setup", inline=False)


        await ctx.send(embed=embed)        


def setup(bot):
    bot.add_cog(Basic(bot))