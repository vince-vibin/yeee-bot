from discord.ext import commands, tasks
import aiohttp
import discord
from discord import app_commands

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

class Animals(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot


    @app_commands.command(name="cat") #sending a random cat pic from random.cat
    async def cat(interaction: discord.interactions.Interaction) -> None:
        async with interaction.channel.typing():

            async with aiohttp.ClientSession() as cs: #making the http-Request
                async with cs.get("https://api.thecatapi.com/v1/images/search") as r:

                    data = await r.json(content_type="application/json")
                    url=data[0]
                    
                    #sending calledNUM Metric to influxdb.py
                    global calledKitty, calledKittyH
                    calledKitty += 1
                    com = "kitty"
                    calledKittyH[0] += 1
                    sendingCom(cog, com, calledKitty)

                    embed = discord.Embed(colour=colorEmbed, title=":heart_eyes_cat:") #sending the message
                    embed.set_image(url=url["url"])

                    embed.set_footer(text="Powered by: http://random.cat")
                    
                    await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @app_commands.command(name="doggo") # sending a random dog pic from random.dog
    async def doggo(interaction: discord.interactions.Interaction) -> None:
        async with interaction.channel.typing():
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
                            await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="fox") # sending a random  fox pic from randomfox.ca
    async def fox(interaction: discord.interactions.Interaction) -> None:
        async with interaction.channel.typing():
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

                    await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="duccy") # sending a random duck pic from random-d.uk
    async def duccy(interaction: discord.interactions.Interaction) -> None:
        async with interaction.channel.typing():
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

                    await interaction.response.send_message(embed=embed, ephemeral=True)

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

    bot.tree.add_command(cat, override=True)
    bot.tree.add_command(doggo, override=True)
    bot.tree.add_command(fox, override=True)
    bot.tree.add_command(duccy, override=True)

    exporterH.start()

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Animals(bot))