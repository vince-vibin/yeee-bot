import asyncpraw
from discord.ext import commands, tasks
import discord
import random
import os
from discord import app_commands
from dotenv import load_dotenv

# setting global var for Embed-Color
global colorEmbed 
colorEmbed = 0xFF6800

#vars for calling sending func
from influx.influxdbExport import sendingCom, sendingH
global cog

cog = "reddit"
calledMeme = 0
calledWholesome = 0
calledStock = 0

calledMemeH = [0, "meme", cog] 
calledWholesomeH = [0, "wholesome", cog]
calledStockH = [0, "stock", cog]

load_dotenv()

class Reddit(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

    # setting secrets from .env
    clientID = os.getenv("REDDIT_CLIENTID")
    clientSecret = os.getenv("REDDIT_CLIENTSECRET")
    userAgent = os.getenv("REDDIT_USERAGENT")

    global reddit
    reddit = asyncpraw.Reddit(
        client_id=clientID, 
        client_secret=clientSecret, 
        user_agent=userAgent
    )


    @app_commands.command(name="meme", description="get a random piece of content from r/meme")
    async def meme(interaction: discord.Interaction) -> None:
        async with interaction.channel.typing():
            
            global reddit
            subreddit = await reddit.subreddit("memes")
            hot = subreddit.hot(limit = 20)
            all_subs = []

            async for submission in hot: # putting posts together
                all_subs.append(submission)

            random_sub = random.choice(all_subs) # getting random post
            name = random_sub.title
            url = random_sub.url

            #sending calledNUM Metric to influxdb.py
            global calledMeme, calledMemeH
            com = "meme"
            calledMeme += 1
            calledMemeH[0] += 1

            sendingCom(cog, com, calledMeme)
            
            embed = discord.Embed(colour=colorEmbed) # sendign message
            embed.add_field(name=name, value="-----", inline=False)
            embed.set_image(url=url)
            embed.set_footer(text="A random piece of content from r/memes")
            
            await interaction.response.send_message(embed=embed, ephemeral=False)
        return

    @app_commands.command(name="wholesome", description="get a random piece of content from r/wholesomememes")
    async def wholesome(interaction: discord.Interaction) -> None:
        async with interaction.channel.typing():
            global reddit
            subreddit = await reddit.subreddit("wholesomememes")
            hot = subreddit.hot(limit = 20)
            all_subs = []

            async for submission in hot:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url

            #sending calledNUM Metric to influxdb.py
            global calledWholesome, calledWholesomeH
            com = "wholesome"
            calledWholesome += 1
            calledWholesomeH[0] += 1

            sendingCom(cog, com, calledWholesome)
            
            embed = discord.Embed(colour=colorEmbed)
            embed.add_field(name=name, value="-----", inline=False)
            embed.set_image(url=url)
            embed.set_footer(text="A random piece of content from r/wholesomememes")

            await interaction.response.send_message(embed=embed, ephemeral=False)
        return

    @app_commands.command(name="stock", description="get a random piece of content from r/stockphotos")
    async def stock(interaction: discord.Interaction) -> None:
        async with interaction.channel.typing():
            global reddit
            subreddit = await reddit.subreddit("stockphotos")
            hot = subreddit.hot(limit = 20)
            all_subs = []

            async for submission in hot:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url

            #sending calledNUM Metric to influxdb.py
            global calledStock, calledStockH
            com = "stock"
            calledStock += 1
            calledStockH[0] += 1

            sendingCom(cog, com, calledStock)
            
            embed = discord.Embed(colour=colorEmbed)
            embed.add_field(name=name, value="-----", inline=False)
            embed.set_image(url=url)
            embed.set_footer(text="A random piece of content from r/stockphotos")

            await interaction.response.send_message(embed=embed, ephemeral=False)
        return
        
    @tasks.loop(hours=1)
    async def exporterH():
        global calledMemeH, calledWholesomeH, calledStockH
        send = [calledMemeH, calledWholesomeH, calledStockH]
        i = 0

        while i < len(send): #looping throught send array
            sendingH(send[i])
            i = i + 1

        calledMemeH[0] = 0 #reseting all values 
        calledWholesomeH[0] = 0
        calledStockH[0] = 0
        
    exporterH.start()

    bot.tree.add_command(meme, override=True)
    bot.tree.add_command(wholesome, override=True)
    bot.tree.add_command(stock, override=True)

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Reddit(bot))