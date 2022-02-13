import random
from discord.ext import commands
import discord


class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(description="Get a random number from 1-100. But Whuay??",brief="Get a random number from 1-100. But Whuay??")
    async def roll(self, ctx):
        n = random.randrange(1,101)

        colour=0xC14EB2
        embed = discord.Embed(colour=colour)
        embed.add_field(name="Congratulations you got a:", value=n, inline=False)
        embed.set_footer(text="Now move on with your live and get hobbys.")
        await ctx.send(embed=embed)

    @commands.command(description="Roll a dice cause you dont have any hobbys.",brief="Roll a dice cause you dont have any hobbys.")
    async def dice(self, ctx):
        n = random.randrange(1, 6)
        
        colour=0xC14EB2
        embed = discord.Embed(colour=colour)
        embed.add_field(name="You rolled a:", value=n, inline=False)
        embed.set_footer(text="Now move on with your live and get hobbys.")
        await ctx.send(embed=embed)

    @commands.command(aliases=['coin'], description="Just flip a coin (i dont know whuay you would).",brief="Just flip a coin (i dont know whuay you would).")
    async def coinflip(self, ctx):
        n = random.choice(('Heads', 'Tails'))
        
        colour=0xC14EB2
        embed = discord.Embed(colour=colour)
        embed.add_field(name="You got:", value=n, inline=False)
        embed.set_footer(text="Now move on with your live and get hobbys.")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Gamble(bot))