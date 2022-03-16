from turtle import color
from discord.ext import commands
import aiohttp
import discord

# setting global var for Embed-Color
global colorEmbed 
colorEmbed = 0xE6A8FF

#vars for calling sending func
from influx.influxdb import sendingCom, sendingH
global cog

cog = "animals"
calledKitty = 0
calledDoggo = 0
calledFoxxy = 0
calledDuccy = 0


class images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=["pussy", "cat"], description="Meow :heart_eyes_cat:",brief="Meow :heart_eyes_cat:") #sending a random cat pic from random.cat
    async def kitty(self, ctx):
        async with ctx.channel.typing():

            async with aiohttp.ClientSession() as cs: #making the http-Request
                async with cs.get("http://aws.random.cat/meow") as r:
                    data = await r.json()

                    #sending calledNUM Metric to influxdb.py
                    global calledKitty
                    calledKitty += 1
                    com = "kitty"
                    sendingCom(cog, com, calledKitty)

                    embed = discord.Embed(colour=colorEmbed, title=":heart_eyes_cat: Meow :heart_eyes_cat: ") #sending the message
                    embed.set_image(url=data['file'])
                    embed.set_footer(text="Powered by: http://random.cat")
                    await ctx.send(embed=embed)
    
    @commands.command(aliases=["dog"], description="Woof :dog:",brief="Woof :dog:") # sending a random dog pic from random.dog
    async def doggo(self, ctx):
        async with ctx.channel.typing():
            gotPic = False
            while not gotPic:
                async with aiohttp.ClientSession() as cs: #making the http-Request
                    async with cs.get("https://random.dog/woof.json") as r:
                        data = await r.json()
                        url = data['url']
                        url = url.lower()


                        if url.endswith("jpg") or url.endswith("jpeg"):
                            gotPic = True

                            global calledDoggo
                            calledDoggo += 1
                            com = "doggo"
                            sendingCom(cog, com, calledDoggo)

                            embed = discord.Embed(colour=colorEmbed, title=":dog: Woof Woof :dog:") #sending the message
                            embed.set_image(url=data['url'])
                            embed.set_footer(text="Powered by: http://random.dog")
                            await ctx.send(embed=embed)

    @commands.command(aliases=["fox"],description="What does the fox say? :fox:",brief="What does the fox say? :fox:") # sending a random  fox pic from randomfox.ca
    async def foxxy(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs: #making the http-Request
                async with cs.get("https://randomfox.ca/floof/") as r:
                    data = await r.json()

                    global calledFoxxy
                    calledFoxxy += 1
                    com = "foxxy"
                    sendingCom(cog, com, calledFoxxy)

                    embed = discord.Embed(colour=colorEmbed, title="Seriosly, what does the fox say?? :fox:") #sending the message
                    embed.set_image(url=data['image'])
                    embed.set_footer(text="Powered by: https://randomfox.ca/")

                    await ctx.send(embed=embed)

    @commands.command(aliases=["duck"],description="Quack quack! :duck:",brief="Quack quack! :duck:") # sending a random duck pic from random-d.uk
    async def duccy(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs: #making the http-Request
                async with cs.get("https://random-d.uk/api/random") as r:
                    data = await r.json()

                    global calledDuccy
                    calledDuccy += 1
                    com = "duccy"
                    sendingCom(cog, com, calledDuccy)

                    embed = discord.Embed(colour=colorEmbed, title="Quickidi quackidi your love is now my property!") #sending the message
                    embed.set_image(url=data['url'])
                    embed.set_footer(text="Powered by: https://random-d.uk")

                    await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(images(bot))