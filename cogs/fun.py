import discord
from discord.ext import commands, tasks
import random
import json
from discord_slash import cog_ext, SlashContext

import qrcode
import os

# setting global var for Embed-Color
global colorEmbed 
colorEmbed = 0x60C14E

#vars for calling sending func
from influx.influxdbExport import sendingCom, sendingH
global cog

cog = "fun"
calledYoomum = 0
calledKanye = 0
calledMagicball = 0
calledQrcode = 0

calledYoomumH = [0, "yoomum", cog] 
calledKanyeH = [0, "kanye", cog]
calledMagicballH = [0, "magicball", cog]
calledQrcodeH = [0, "qrcode", cog]

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="yoomum", description="be nice to moms") # getting a random yoomum joke from data/yoomum.json
    async def yoomum(self, ctx: SlashContext, member: discord.Member = None):
        #sending calledNUM Metric to influxdb.py
        global calledYoomum, calledYoomumH
        com = "yoomum"
        calledYoomum += 1
        calledYoomumH[0] += 1

        sendingCom(cog, com, calledYoomum)

        with open("data/yoomum.json", encoding='utf-8') as yoomum_file:
            yoomum = json.load(yoomum_file)
            random_category = random.choice(list(yoomum.keys()))
            yoomum = random.choice(list(yoomum[random_category]))

        if member is not None:
            author = ctx.author
            embed = discord.Embed(colour=colorEmbed)
            embed.add_field(name=yoomum, value="{} got owned by {}".format(member.mention, author.mention), inline=False)
            await ctx.send(embed=embed)
        else:
            author = ctx.author
            embed = discord.Embed(colour=colorEmbed)
            embed.add_field(name=yoomum, value="{} got owned by himself".format(author.mention), inline=False)
            embed.set_footer(text="what a loser")
            await ctx.send(embed=embed)
    
    @cog_ext.cog_slash(name="kanye", description="get a random Kanye West quote") # getting a random wisdom from data/weisheiten.json
    async def kanye(self, ctx: SlashContext):
        with open("data/kanyerest.json", encoding='utf-8') as wisdom_file:
            wisdom = json.load(wisdom_file)
            wisdom = random.choice(list(wisdom))

        #sending calledNUM Metric to influxdb.py
        global calledKanye, calledKanyeH
        com = "kanye"
        calledKanye += 1
        calledKanyeH[0] += 1

        sendingCom(cog, com, calledKanye)

        embed = discord.Embed(colour=colorEmbed)
        embed.add_field(name=wisdom, value="This is a random quote by Kanye West", inline=False)
        embed.set_footer(text="Check out the Kanye Rest API here: https://github.com/ajzbc/kanye.rest")
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="8ball", description="Ask the magic 8ball a question") # getting a random answer from data/8ball.json
    async def magicball(self, ctx: SlashContext, question):

        #sending calledNUM Metric to influxdb.py
        global calledMagicball, calledMagicballH
        com = "magicball"
        calledMagicball += 1
        calledMagicballH[0] += 1

        sendingCom(cog, com, calledMagicball)

        with open("data/8ball.json", encoding='utf-8') as answers_file:
            answers = json.load(answers_file)
            random_category = random.choice(list(answers.keys()))
            answers = random.choice(list(answers[random_category]))

        embed = discord.Embed(colour=colorEmbed)
        embed.add_field(name=answers, value="The ball has spoken", inline=False)
        embed.set_footer(text="Just like my balls if you know what i mean")
        await ctx.send(embed=embed)
    
    @cog_ext.cog_slash(name="qr", description="Create a qrcode to a link") #generating a qr code based on the profided link=data
    async def qrcode(self, ctx: SlashContext, arg):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        data = arg

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")
        img.save("data/qr_code.png")

        await ctx.send(file=discord.File('data/qr_code.png')) # files can not be send in an Embed :(

        #sending calledNUM Metric to influxdb.py
        global calledQrcode, calledQrcodeH
        com = "qrcode"
        calledQrcode += 1

        calledQrcodeH[0] += 1

        sendingCom(cog, com, calledQrcode)

        os.remove("data/qr_code.png")

    @tasks.loop(hours=1)
    async def exporterH():
        global calledYoomumH, calledKanyeH, calledMagicballH, calledQrcodeH
        send = [calledYoomumH, calledKanyeH, calledMagicballH, calledQrcodeH]
        i = 0

        while i < len(send): #looping throught send array
            sendingH(send[i])
            i = i + 1

        calledYoomumH[0] = 0 #reseting all values 
        calledKanyeH[0] = 0
        calledMagicballH[0] = 0
        calledQrcodeH[0] = 0

    exporterH.start()

def setup(bot):
    bot.add_cog(fun(bot))