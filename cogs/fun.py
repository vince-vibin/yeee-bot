import discord
from discord.ext import commands

from utils import get_yoomum_joke
from utils import get_wisdom
from utils import get_answers

import qrcode
import os

# setting global var for Embed-Color
global colorEmbed 
colorEmbed = 0x60C14E

class insults(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Yoo Mum is!") # getting a random yoomum joke from data/yoomum.json
    async def yoomum(self, ctx, member: discord.Member = None):
        yoomum = await get_yoomum_joke()
        if member is not None:
            embed = discord.Embed(colour=colorEmbed)
            embed.add_field(name=member.name, value=yoomum, inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(colour=colorEmbed)
            embed.add_field(name="To make you fell better", value=yoomum, inline=False)
            await ctx.send(embed=embed)
    
    @commands.command(aliases=['wisdom'], brief="Smort") # getting a random wisdom from data/weisheiten.json
    async def smort(self, ctx,):
        wisdom = await get_wisdom()

        embed = discord.Embed(colour=colorEmbed)
        embed.add_field(name=wisdom, value="This wisdom i learned from my dad/developer YeeeeeBoi", inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=['ball', 'mb', '8ball'], brief="Magic 8Ball") # getting a random answer from data/8ball.json
    async def magicball(self, ctx, *question):
        answers = await get_answers()
        
        embed = discord.Embed(colour=colorEmbed)
        embed.add_field(name=answers, value="The ball has spoken", inline=False)
        embed.set_footer(text="Just like my balls if you know what i mean")
        await ctx.send(embed=embed)
    
    @commands.command(aliases=['qr'], brief="Create a qrcode") #generating a qr code based on the profided link=data
    async def qrcode(self, ctx, *link):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        data = link

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")
        img.save("data/qr_code.png")

        await ctx.send(file=discord.File('data/qr_code.png')) # files can not be send in an Embed :(

        os.remove("data/qr_code.png")

def setup(bot):
    bot.add_cog(insults(bot))