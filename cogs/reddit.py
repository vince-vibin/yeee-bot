import praw
from discord.ext import commands
import discord
import random

class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # !!!!    
    reddit = praw.Reddit(client_id ="S1vglQgURi0GDQ", client_secret = "lYhIwXcGR8sy2_wYxwJOxluUIxg", username = "YeeeeeBoyy", password = "Gr1zzl1es", user_agent = "YeeeeeBot") # import secrets soon !!!!

    subreddit = reddit.subreddit("memes")
    hot = subreddit.hot(limit = 100) # loading first 100 posts from subreddit

    @commands.command(description="Get a random piece of content from r/memes",brief="Get a random piece of content from r/memes")
    async def meme(self, ctx):
        async with ctx.channel.typing():
            reddit = praw.Reddit(client_id ="S1vglQgURi0GDQ", client_secret = "lYhIwXcGR8sy2_wYxwJOxluUIxg", username = "YeeeeeBoyy", password = "Gr1zzl1es", user_agent = "YeeeeeBot")
            subreddit = reddit.subreddit("memes")
            hot = subreddit.hot(limit = 100)
            all_subs = []

            for submission in hot: # putting posts together
                all_subs.append(submission)

            random_sub = random.choice(all_subs) # getting random post
            name = random_sub.title
            url = random_sub.url
            
            embed = discord.Embed(colour=0xFF6800) # sendign message
            embed.add_field(name=name, value="...", inline=False)
            embed.set_image(url=url)
            embed.set_footer(text="A random piece of content from r/memes")

            await ctx.send(embed=embed)
        return

    @commands.command(aliases=['craiglist','stonks'], description="Get a random piece of content from r/CrackheadCraigslist",brief="Get a random piece of content from r/CrackheadCraigslist")
    async def sell(self, ctx):
        async with ctx.channel.typing():
            reddit = praw.Reddit(client_id ="S1vglQgURi0GDQ", client_secret = "lYhIwXcGR8sy2_wYxwJOxluUIxg", username = "YeeeeeBoyy", password = "Gr1zzl1es", user_agent = "YeeeeeBot")
            subreddit = reddit.subreddit("CrackheadCraigslist")
            hot = subreddit.hot(limit = 100)
            all_subs = []

            for submission in hot:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            
            embed = discord.Embed(colour=0xFF6800)
            embed.add_field(name=name, value="...", inline=False)
            embed.set_image(url=url)
            embed.set_footer(text="A random piece of content from r/CrackheadCraigslist")

            await ctx.send(embed=embed)
        return

    @commands.command(aliases=['think'], description="Get a random piece of content from r/mhh",brief="Get a random piece of content from r/mhh")
    async def hmm(self, ctx):
        async with ctx.channel.typing():
            reddit = praw.Reddit(client_id ="S1vglQgURi0GDQ", client_secret = "lYhIwXcGR8sy2_wYxwJOxluUIxg", username = "YeeeeeBoyy", password = "Gr1zzl1es", user_agent = "YeeeeeBot")
            subreddit = reddit.subreddit("hmm")
            hot = subreddit.hot(limit = 100)
            all_subs = []

            for submission in hot:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            
            embed = discord.Embed(colour=0xFF6800)
            embed.add_field(name=name, value="...", inline=False)
            embed.set_image(url=url)
            embed.set_footer(text="A random piece of content from r/hmm")

            await ctx.send(embed=embed)
        return

    @commands.command(aliases=['depression'], description="Get a random piece of content from r/im14andthisisdeep",brief="Get a random piece of content from r/im14andthisisdeep")
    async def deep(self, ctx):
        async with ctx.channel.typing():
            reddit = praw.Reddit(client_id ="S1vglQgURi0GDQ", client_secret = "lYhIwXcGR8sy2_wYxwJOxluUIxg", username = "YeeeeeBoyy", password = "Gr1zzl1es", user_agent = "YeeeeeBot")
            subreddit = reddit.subreddit("im14andthisisdeep")
            hot = subreddit.hot(limit = 100)
            all_subs = []

            for submission in hot:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            
            embed = discord.Embed(colour=0xFF6800)
            embed.add_field(name=name, value="...", inline=False)
            embed.set_image(url=url)
            embed.set_footer(text="A random piece of content from r/im14andthisisdeep")

            await ctx.send(embed=embed)
        return

    @commands.command(aliases=['wholesomememes'], description="Get a random piece of content from r/wholesomememes",brief="Get a random piece of content from r/wholesomememes")
    async def wholesome(self, ctx):
        async with ctx.channel.typing():
            reddit = praw.Reddit(client_id ="S1vglQgURi0GDQ", client_secret = "lYhIwXcGR8sy2_wYxwJOxluUIxg", username = "YeeeeeBoyy", password = "Gr1zzl1es", user_agent = "YeeeeeBot")
            subreddit = reddit.subreddit("wholesomememes")
            hot = subreddit.hot(limit = 100)
            all_subs = []

            for submission in hot:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            
            embed = discord.Embed(colour=0xFF6800)
            embed.add_field(name=name, value="...", inline=False)
            embed.set_image(url=url)
            embed.set_footer(text="A random piece of content from r/wholesomememes")

            await ctx.send(embed=embed)
        return

    @commands.command(aliases=['true'], description="Get a random piece of content from r/technicallythetruth",brief="Get a random piece of content from r/technicallythetruth")
    async def truth(self, ctx):
        async with ctx.channel.typing():
            reddit = praw.Reddit(client_id ="S1vglQgURi0GDQ", client_secret = "lYhIwXcGR8sy2_wYxwJOxluUIxg", username = "YeeeeeBoyy", password = "Gr1zzl1es", user_agent = "YeeeeeBot")
            subreddit = reddit.subreddit("technicallythetruth")
            hot = subreddit.hot(limit = 100)
            all_subs = []

            for submission in hot:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            
            embed = discord.Embed(colour=0xFF6800)
            embed.add_field(name=name, value="...", inline=False)
            embed.set_image(url=url)
            embed.set_footer(text="A random piece of content from r/technicallythetruth")

            await ctx.send(embed=embed)
        return

    @commands.command(aliases=['stockphotos', 'wtfstockphotos'], description="Get a random piece of content from r/stockphotos",brief="Get a random piece of content from r/stockphotos")
    async def stock(self, ctx):
        async with ctx.channel.typing():
            reddit = praw.Reddit(client_id ="S1vglQgURi0GDQ", client_secret = "lYhIwXcGR8sy2_wYxwJOxluUIxg", username = "YeeeeeBoyy", password = "Gr1zzl1es", user_agent = "YeeeeeBot")
            subreddit = reddit.subreddit("stockphotos")
            hot = subreddit.hot(limit = 100)
            all_subs = []

            for submission in hot:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            
            embed = discord.Embed(colour=0xFF6800)
            embed.add_field(name=name, value="...", inline=False)
            embed.set_image(url=url)
            embed.set_footer(text="A random piece of content from r/stockphotos")

            await ctx.send(embed=embed)
        return

    @commands.command(aliases=['softwaregore', 'techfail'], description="Get a random piece of content from r/softwaregore",brief="Get a random piece of content from r/softwaregore")
    async def tehc(self, ctx):
        async with ctx.channel.typing():
            reddit = praw.Reddit(client_id ="S1vglQgURi0GDQ", client_secret = "lYhIwXcGR8sy2_wYxwJOxluUIxg", username = "YeeeeeBoyy", password = "Gr1zzl1es", user_agent = "YeeeeeBot")
            subreddit = reddit.subreddit("softwaregore")
            hot = subreddit.hot(limit = 100)
            all_subs = []

            for submission in hot:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            
            embed = discord.Embed(colour=0xFF6800)
            embed.add_field(name=name, value="...", inline=False)
            embed.set_image(url=url)
            embed.set_footer(text="A random piece of content from r/softwaregore")

            await ctx.send(embed=embed)
        return

    @commands.command(aliases=['facepalm'], description="Get a random piece of content from r/facepalm",brief="Get a random piece of content from r/facepalm")
    async def stoopid(self, ctx):
        async with ctx.channel.typing():
            reddit = praw.Reddit(client_id ="S1vglQgURi0GDQ", client_secret = "lYhIwXcGR8sy2_wYxwJOxluUIxg", username = "YeeeeeBoyy", password = "Gr1zzl1es", user_agent = "YeeeeeBot")
            subreddit = reddit.subreddit("facepalm")
            hot = subreddit.hot(limit = 100)
            all_subs = []

            for submission in hot:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            
            embed = discord.Embed(colour=0xFF6800)
            embed.add_field(name=name, value="...", inline=False)
            embed.set_image(url=url)
            embed.set_footer(text="A random piece of content from r/facepalm")

            await ctx.send(embed=embed)
        return
def setup(bot):
    bot.add_cog(Reddit(bot))