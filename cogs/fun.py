import discord
from discord.ext import commands, tasks
import random
import json
from discord import app_commands

import image   
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

class Fun(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

    @app_commands.command(name="yoomum", description="be nice to moms (you can tag people her)") # getting a random yoomum joke from data/yoomum.json
    async def yoomum(interaction: discord.Interaction, member: discord.Member = None) -> None:
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
            author = interaction.user
            embed = discord.Embed(colour=colorEmbed)
            embed.add_field(name=yoomum, value="{} got owned by {}".format(member.mention, author.mention), inline=False)
            await interaction.response.send_message(embed=embed, ephemeral=False)
        else:
            author = interaction.user
            embed = discord.Embed(colour=colorEmbed)
            embed.add_field(name=yoomum, value="{} got owned by himself".format(author.mention), inline=False)
            embed.set_footer(text="what a loser")
            await interaction.response.send_message(embed=embed, ephemeral=False)
    
    @app_commands.command(name="kanye", description="get a quote of kanye west") # getting a random wisdom from data/weisheiten.json
    async def kanye(interaction: discord.Interaction) -> None:
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
        await interaction.response.send_message(embed=embed, ephemeral=False)

    @app_commands.command(name="8ball", description="ask me a question") # getting a random answer from data/8ball.json
    async def magicball(interaction: discord.Interaction, question: str):

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
        await interaction.response.send_message(embed=embed, ephemeral=False)
    
    @app_commands.command(name="qr", description="get a qr code of anything") #generating a qr code based on the profided link=data
    async def qr(interaction: discord.Interaction, arg: str):
        global calledQrcode, calledQrcodeH
        com = "qrcode"
        calledQrcode += 1
        calledQrcodeH[0] += 1

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(arg)
        qr.make(arg)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("./data/qrcode.png")

        await interaction.response.send_message("Here is your QR-Code:", file=discord.File('./data/qrcode.png'), ephemeral=False) # files can not be send in an Embed :(   

        sendingCom(cog, com, calledQrcode)

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

    bot.tree.add_command(yoomum, override=True)
    bot.tree.add_command(kanye, override=True)
    bot.tree.add_command(magicball, override=True)
    bot.tree.add_command(qr, override=True)

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Fun(bot))