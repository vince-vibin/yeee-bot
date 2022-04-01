import asyncpraw
from discord.ext import commands, tasks
import discord
import random
import os
from discord_slash import cog_ext, SlashContext

# setting global var for Embed-Color
global colorEmbed 
colorEmbed = 0xFF6800

#vars for calling sending func
from influx.influxdbExport import sendingCom, sendingH
global cog

cog = "reddit"
calledMeme = 0
calledHmm = 0
calledDeep = 0
calledWholesome = 0
calledStock = 0
calledTehc = 0
calledStoopid = 0

calledMemeH = [0, "meme", cog] 
calledHmmH = [0, "hmm", cog]
calledDeepH = [0, "deep", cog]
calledWholesomeH = [0, "wholesome", cog]
calledStockH = [0, "stock", cog]
calledTehcH = [0, "tehc", cog]
calledStoopidH = [0, "stoopid", cog]

class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # setting secrets from .env
    clientID = os.getenv("REDDIT_client_id")
    clientSecret = os.getenv("REDDIT_client_secret")
    username = os.getenv("REDDIT_username")
    password = os.getenv("REDDIT_password")
    userAgent = os.getenv("REDDIT_user_agent")

    global reddit
    reddit = asyncpraw.Reddit(client_id = clientID, client_secret = clientSecret, username = username, password = password, user_agent = userAgent)


    @cog_ext.cog_slash(name="meme", description="Get a random piece of content from r/memes")
    async def meme(self, ctx: SlashContext):
        async with ctx.channel.typing():
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
            embed.add_field(name=name, value="...", inline=False)
            embed.set_image(url=url)
            embed.set_footer(text="A random piece of content from r/memes")
            
            await ctx.send(embed=embed)
        return

    @cog_ext.cog_slash(name="wholesome", description="Get a random piece of content from r/wholesomememes")
    async def wholesome(self, ctx: SlashContext):
        async with ctx.channel.typing():
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
            embed.add_field(name=name, value="...", inline=False)
            embed.set_image(url=url)
            embed.set_footer(text="A random piece of content from r/wholesomememes")

            await ctx.send(embed=embed)
        return

    @cog_ext.cog_slash(name="stock", description="Get a random piece of content from r/stockphotos")
    async def stock(self, ctx: SlashContext):
        async with ctx.channel.typing():
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
            embed.add_field(name=name, value="...", inline=False)
            embed.set_image(url=url)
            embed.set_footer(text="A random piece of content from r/stockphotos")

            await ctx.send(embed=embed)
        return
        
    @tasks.loop(hours=1)
    async def exporterH():
        global calledMemeH, calledHmmH, calledDeepH, calledWholesomeH, calledStockH, calledTehcH, calledStoopidH
        send = [calledMemeH, calledHmmH, calledDeepH, calledWholesomeH, calledStockH, calledTehcH, calledStoopidH]
        i = 0

        while i < len(send): #looping throught send array
            sendingH(send[i])
            i = i + 1

        calledMemeH[0] = 0 #reseting all values 
        calledHmmH[0] = 0
        calledDeepH[0] = 0
        calledWholesomeH[0] = 0
        calledStockH[0] = 0
        calledTehcH[0] = 0
        calledStoopidH[0] = 0
        
    exporterH.start()
    
def setup(bot):
    bot.add_cog(Reddit(bot))