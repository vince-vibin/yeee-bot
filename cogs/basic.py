from discord.ext import commands
import discord

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ex)
        colour=0xFF0000

        embed = discord.Embed(colour=colour)
        embed.add_field(name="Bruh", value="It seems like you are to dumb to use this command so please leave me alone.", inline=False)
        await ctx.send(embed=embed)


    @commands.command(description="*Happy Table-Tennis noises*",brief="*Happy Table-Tennis noises*")
    async def ping(self, ctx):
        colour=0x94FFB4

        embed = discord.Embed(colour=colour)
        embed.add_field(name="Pong you Dumb!", value=format(round(self.bot.latency * 1000)), inline=False)
        await ctx.send(embed=embed)

    @commands.command(description="Something you want the bot to say. Cause youre too afraid to.",brief="Something you want the bot to say. Cause youre to afraid to say it.")
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

    @commands.command(description="Get info about the life of YeeeeeBot",brief="Get info about the life of YeeeeeBot")
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


def setup(bot):
    bot.add_cog(Basic(bot))