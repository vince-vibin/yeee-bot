from discord.ext import commands, tasks
import aiohttp
import discord
from discord_slash import cog_ext, SlashContext

# setting global var for Embed-Color
global colorEmbed 
colorEmbed = 0xE6A8FF

#vars for calling sending func
from influx.influxdbExport import sendingCom, sendingH
global cog

cog = "animals"
calledKitty = 0
calledDoggo = 0
calledFoxxy = 0
calledDuccy = 0

calledKittyH = [0, "kitty", cog] 
calledDoggoH = [0, "doggo", cog]
calledFoxxyH = [0, "foxxy", cog]
calledDuccyH = [0, "duccy", cog]

class images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @cog_ext.cog_slash(name="cat", description="get a random pic of a cat") #sending a random cat pic from random.cat
    async def cat(self, ctx: SlashContext):
        async with ctx.channel.typing():

            async with aiohttp.ClientSession() as cs: #making the http-Request
                async with cs.get("http://aws.random.cat/meow") as r:
                    
                    data = await r.json(content_type=None)

                    #sending calledNUM Metric to influxdb.py
                    global calledKitty, calledKittyH
                    calledKitty += 1
                    com = "kitty"
                    calledKittyH[0] += 1
                    sendingCom(cog, com, calledKitty)

                    embed = discord.Embed(colour=colorEmbed, title=":heart_eyes_cat:") #sending the message
                    embed.set_image(url=data['file'])
                    embed.set_footer(text="Powered by: http://random.cat")
                    await ctx.send(embed=embed)
    
    @cog_ext.cog_slash(name="doggo", description="get a random pic of a dog") # sending a random dog pic from random.dog
    async def doggo(self, ctx: SlashContext):
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

                            global calledDoggo, calledDoggoH
                            calledDoggo += 1
                            com = "doggo"
                            calledDoggoH[0] += 1
                            sendingCom(cog, com, calledDoggo)

                            embed = discord.Embed(colour=colorEmbed, title=":dog:") #sending the message
                            embed.set_image(url=data['url'])
                            embed.set_footer(text="Powered by: http://random.dog")
                            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="fox",description="get a random pic of a fox") # sending a random  fox pic from randomfox.ca
    async def fox(self, ctx: SlashContext):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs: #making the http-Request
                async with cs.get("https://randomfox.ca/floof/") as r:
                    data = await r.json()

                    global calledFoxxy, calledFoxxyH
                    calledFoxxy += 1
                    com = "foxxy"
                    calledFoxxyH[0] += 1
                    sendingCom(cog, com, calledFoxxy)

                    embed = discord.Embed(colour=colorEmbed, title=":fox:") #sending the message
                    embed.set_image(url=data['image'])
                    embed.set_footer(text="Powered by: https://randomfox.ca/")

                    await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="duck",description="get a random pic of a duck") # sending a random duck pic from random-d.uk
    async def duccy(self, ctx: SlashContext):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs: #making the http-Request
                async with cs.get("https://random-d.uk/api/random") as r:
                    data = await r.json()

                    global calledDuccy, calledDuccyH
                    calledDuccy += 1
                    com = "duccy"
                    calledDuccyH[0] += 1
                    sendingCom(cog, com, calledDuccy)

                    embed = discord.Embed(colour=colorEmbed, title=":duck:") #sending the message
                    embed.set_image(url=data['url'])
                    embed.set_footer(text="Powered by: https://random-d.uk")

                    await ctx.send(embed=embed)

    @tasks.loop(hours=1)
    async def exporterH():
        global calledKittyH, calledDoggoH, calledFoxxyH, calledDuccyH
        send = [calledKittyH, calledDoggoH, calledFoxxyH, calledDuccyH]
        i = 0

        while i < len(send): #looping throught send array
            sendingH(send[i])
            i = i + 1

        calledKittyH[0] = 0 #reseting all values 
        calledDoggoH[0] = 0
        calledFoxxyH[0] = 0
        calledDuccyH[0] = 0
        
    exporterH.start()

def setup(bot):
    bot.add_cog(images(bot))