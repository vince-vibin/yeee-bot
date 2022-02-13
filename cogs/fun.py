import discord
from discord.ext import commands

from utils import get_yoomum_joke
from utils import get_wisdom
from utils import get_answers

import qrcode
import image
import os

class insults(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Yoo Mum is!")
    async def yoomum(self, ctx, member: discord.Member = None):
        yoomum = await get_yoomum_joke()
        if member is not None:
            embed = discord.Embed(colour=0x60C14E)
            embed.add_field(name=member.name, value=yoomum, inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(colour=0x60C14E)
            embed.add_field(name="To make you fell better", value=yoomum, inline=False)
            await ctx.send(embed=embed)
    
    @commands.command(aliases=['wisdom'], brief="Smort")
    async def smort(self, ctx,):
        wisdom = await get_wisdom()
        colour = 0x60C14E
        
        embed = discord.Embed(colour=colour)
        embed.add_field(name=wisdom, value="This wisdom i learned from my dad/developer YeeeeeBoi", inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=['ball', 'mb', '8ball'], brief="Magic 8Ball")
    async def magicball(self, ctx, *question):
        answers = await get_answers()
        colour = 0x60C14E
        
        embed = discord.Embed(colour=colour)
        embed.add_field(name=answers, value="The ball has spoken", inline=False)
        embed.set_footer(text="Just like my balls if you know what i mean")
        await ctx.send(embed=embed)
    
    @commands.command(aliases=['qr'], brief="Create a qrcode")
    async def qrcode(self, ctx, *link):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        data = link

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")
        img.save("data/qr_code.png")

        await ctx.send(file=discord.File('data/qr_code.png'))

        os.remove("data/qr_code.png")

def setup(bot):
    bot.add_cog(insults(bot))