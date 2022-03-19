from discord.ext import commands, tasks
import discord

#vars for calling sending func
from influxdbExport import sendingCom, sendingH
global cog

cog = "help"
calledHelp = 0
calledHelpAnimals = 0
calledHelpBasic = 0
calledHelpFun = 0
calledHelpGames = 0
calledHelpReddit = 0

calledHelpH = [0, "help", cog] 
calledHelpAnimalsH = [0, "helpAnimals", cog]
calledHelpBasicH = [0, "helpBasic", cog]
calledHelpFunH = [0, "helpFun", cog]
calledHelpGamesH = [0, "helpGames", cog]
calledHelpRedditH = [0, "helpReddit", cog]

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.group(name="help", invoke_without_command=True) # help command with no or unkown argument
    async def help(self, ctx):

        #sending calledNUM Metric to influxdb.py
        global calledHelp, calledHelpH
        com = "helpGeneral"
        calledHelp += 1
        calledHelpH[0] += 1

        sendingCom(cog, com, calledHelp)

        embed = discord.Embed(colour=discord.Colour.green(), title="Help commands")
        embed.add_field(name="animals :duck:", value="```$help animals```", inline=True)
        embed.add_field(name="basic :teddy_bear:", value="```$help basic```", inline=True)
        embed.add_field(name="fun :microbe:", value="```$help fun```", inline=True)
        embed.add_field(name="games :video_game:", value="```$help games```", inline=True)
        embed.add_field(name="reddit :camera_with_flash:", value="```$help reddit```", inline=True)
        await ctx.send(embed=embed)

    @help.command(name="animals") # help command for animals.py
    async def animals(self, ctx):
        
        #sending calledNUM Metric to influxdb.py
        global calledHelpAnimals, calledHelpAnimalsH
        com = "helpAnimlas"
        calledHelpAnimals += 1
        calledHelpAnimalsH[0] += 1

        sendingCom(cog, com, calledHelpAnimals)

        embed = discord.Embed(colour=0xE6A8FF, title="Help for animal commands :duck:")
        embed.add_field(name="kitty", value="get a cute picture of a kitty ```$kitty```", inline=True)
        embed.add_field(name="doggo", value="get a cute picture of a doggo ```$doggo```", inline=True)
        embed.add_field(name="foxxy", value="get a cute picture of a foxxy ```$foxxy```", inline=False)
        embed.add_field(name="duccy", value="get a cute picture of a duccy ```$duccy```", inline=True)
        embed.set_footer(text="For help send me an e-mail yeeeeebot@gmail.com or check out my socials.")
        await ctx.send(embed=embed)

    @help.command(name="basic") # help command for basic.py
    async def basic(self, ctx):

        #sending calledNUM Metric to influxdb.py
        global calledHelpBasic, calledHelpBasicH
        com = "helpBasic"
        calledHelpBasic += 1
        calledHelpBasicH[0] += 1

        sendingCom(cog, com, calledHelpBasic)

        embed = discord.Embed(colour=0x94FFB4, title="Help for basic commands :teddy_bear:")
        embed.add_field(name="ping", value="*Happy Table-Tennis noises* ```$ping```", inline=True)
        embed.add_field(name="say", value="Something you want the bot to say. ```$say <words>```", inline=True)
        embed.add_field(name="botinfo", value="Get ifo about my life you stalker.```$botinfo```", inline=True)
        embed.set_footer(text="For help send me an e-mail yeeeeebot@gmail.com or check out my socials.")
        await ctx.send(embed=embed)

    @help.command(name="fun") # help command for fun.py
    async def fun(self, ctx):

        #sending calledNUM Metric to influxdb.py
        global calledHelpFun, calledHelpFunH
        com = "helpFun"
        calledHelpFun += 1
        calledHelpFunH[0] += 1

        sendingCom(cog, com, calledHelpFun)

        embed = discord.Embed(colour=0x60C14E, title="Help for fun commands :microbe:")
        embed.add_field(name="wisdom", value="Smort ```$wisdom/smort```", inline=True)
        embed.add_field(name="yoomum", value="Yoo Mum is! ```$yoomum <member>```", inline=True)
        embed.add_field(name="Magic 8Ball", value="Ask the Ball a question ```$8ball <question>```", inline=True)
        embed.add_field(name="QR-Code", value="Generate a QR-Code to a link ```$qr <link>```", inline=True)
        embed.set_footer(text="For help send me an e-mail yeeeeebot@gmail.com or check out my socials.")
        await ctx.send(embed=embed)

    @help.command(name="games") # help for games.py
    async def games(self, ctx):

        #sending calledNUM Metric to influxdb.py
        global calledHelpGames, calledHelpGamesH
        com = "helpGames"
        calledHelpGames += 1
        calledHelpGamesH[0] += 1

        sendingCom(cog, com, calledHelpGames)
        
        embed = discord.Embed(colour=0x00FFEC, title="Help for game commands :video_game:")
        embed.add_field(name="Rock, Paper, Scissors", value="Play Rock, Paper, Scissors against your friend replacement. ```$rps <rock/paper/scissor>```", inline=True)
        embed.add_field(name="hangman", value="Play Hangman against your friend replacement. ```$hm <guess>```", inline=True)
        embed.set_footer(text="For help send me an e-mail yeeeeebot@gmail.com or check out my socials.")
        embed.add_field(name="roll", value="Get a random number from 1-100. But Whuay?? ```$roll```", inline=True)
        embed.add_field(name="dice", value="Roll a dice cause you dont have any hobbys. ```$dice```", inline=True)
        embed.add_field(name="coinflip", value="Just flip a coin (i dont know whuay you would). ```$coinflip/coin```", inline=True)
        embed.set_footer(text="For help send me an e-mail yeeeeebot@gmail.com or check out my socials.")
        await ctx.send(embed=embed)

    @help.command(name="reddit") # help for reddit.py
    async def reddit(self, ctx):

        #sending calledNUM Metric to influxdb.py
        global calledHelpReddit, calledHelpRedditH
        com = "helpReddit"
        calledHelpReddit += 1
        calledHelpRedditH[0] += 1

        sendingCom(cog, com, calledHelpReddit)

        embed = discord.Embed(colour=0xA8FFD5, title="Help for reddit commands :art:")
        embed.add_field(name="meme", value="Get a random piece of content from r/memes ```$meme```", inline=True)
        embed.add_field(name="sell", value="Get a random piece of content from r/CrackheadCraigslist```$sell```", inline=True)
        embed.add_field(name="hmm", value="Get a random piece of content from r/mhh```$hmm```", inline=True)
        embed.add_field(name="deep", value="Get a random piece of content from r/im14andthisisdeep```$deep```", inline=True)
        embed.add_field(name="wholesome", value="Get a random piece of content from r/wholesomememes```$wholesome```", inline=True)
        embed.add_field(name="truth", value="Get a random piece of content from r/technicallythetruth```$truth```", inline=True)
        embed.add_field(name="facepalm", value="Get a random piece of content from r/facepalm```$facepalm```", inline=True)
        embed.set_footer(text="For help send me an e-mail yeeeeebot@gmail.com or check out my socials.")
        await ctx.send(embed=embed)

    @tasks.loop(minutes=1)
    async def exporterH():
        global calledHelpH, calledHelpAnimalsH, calledHelpBasicH, calledHelpFunH, calledHelpGamesH, calledHelpRedditH
        send = [calledHelpH, calledHelpAnimalsH, calledHelpBasicH, calledHelpFunH, calledHelpGamesH, calledHelpRedditH]
        i = 0

        while i < len(send): #looping throught send array
            sendingH(send[i])
            i = i + 1

        calledHelpH[0] = 0 #reseting all values 
        calledHelpAnimalsH[0] = 0
        calledHelpBasicH[0] = 0
        calledHelpFunH[0] = 0
        calledHelpGamesH[0] = 0
        calledHelpRedditH[0] = 0
        
    exporterH.start()

def setup(bot):
    bot.add_cog(Help(bot))