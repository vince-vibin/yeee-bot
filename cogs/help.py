from discord.ext import commands, tasks
import discord
from discord_slash import cog_ext, SlashContext

#vars for calling sending func
from influx.influxdbExport import sendingCom, sendingH
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


    @cog_ext.cog_slash(name="help", description="get help") # help command with no or unkown argument
    async def help(self, ctx: SlashContext, arg = None):

        if arg != None and arg.lower() == "animals":
            #sending calledNUM Metric to influxdb.py
            global calledHelpAnimals, calledHelpAnimalsH
            com = "helpAnimlas"
            calledHelpAnimals += 1
            calledHelpAnimalsH[0] += 1

            sendingCom(cog, com, calledHelpAnimals)

            embed = discord.Embed(colour=0xE6A8FF, title="Help for animal commands :duck:")
            embed.add_field(name="kitty", value="get a cute picture of a kitty ```/cat```", inline=True)
            embed.add_field(name="doggo", value="get a cute picture of a doggo ```/doggo```", inline=True)
            embed.add_field(name="foxxy", value="get a cute picture of a foxxy ```/fox```", inline=False)
            embed.add_field(name="duccy", value="get a cute picture of a duccy ```/duck```", inline=True)
            embed.set_footer(text="For help feel free to join this discord server: https://discord.gg/5WfYJje")
            await ctx.send(embed=embed)
        
        elif arg != None and arg.lower() == "basic":
            #sending calledNUM Metric to influxdb.py
            global calledHelpBasic, calledHelpBasicH
            com = "helpBasic"
            calledHelpBasic += 1
            calledHelpBasicH[0] += 1

            sendingCom(cog, com, calledHelpBasic)

            embed = discord.Embed(colour=0x94FFB4, title="Help for basic commands :teddy_bear:")
            embed.add_field(name="ping", value="*Happy Table-Tennis noises* ```/ping```", inline=True)
            embed.add_field(name="botinfo", value="Get info about my life you stalker.```/botinfo```", inline=False)
            embed.add_field(name="serverinfo", value="Get info about my the server you stalker.```/serverinfo```", inline=True)
            embed.set_footer(text="For help feel free to join this discord server: https://discord.gg/5WfYJje")
            await ctx.send(embed=embed)

        elif arg != None and  arg.lower() == "fun":
            #sending calledNUM Metric to influxdb.py
            global calledHelpFun, calledHelpFunH
            com = "helpFun"
            calledHelpFun += 1
            calledHelpFunH[0] += 1

            sendingCom(cog, com, calledHelpFun)

            embed = discord.Embed(colour=0x60C14E, title="Help for fun commands :microbe:")
            embed.add_field(name="Kanye", value="a random Kanye West quote ```/kanye```", inline=True)
            embed.add_field(name="Yoo Mum", value="Yoo Mum is! ```/yoomum <member>```", inline=True)
            embed.add_field(name="Magic 8Ball", value="Ask the Ball a question ```/8ball <question>```", inline=True)
            embed.add_field(name="QR-Code", value="Generate a QR-Code to anything ```/qr <link>```", inline=True)
            embed.set_footer(text="For help feel free to join this discord server: https://discord.gg/5WfYJje")
            await ctx.send(embed=embed)

        elif arg != None and arg.lower() == "games":
            #sending calledNUM Metric to influxdb.py
            global calledHelpGames, calledHelpGamesH
            com = "helpGames"
            calledHelpGames += 1
            calledHelpGamesH[0] += 1

            sendingCom(cog, com, calledHelpGames)
            
            embed = discord.Embed(colour=0x00FFEC, title="Help for game commands :video_game:")
            embed.add_field(name="Rock, Paper, Scissors", value="Play Rock, Paper, Scissors ```$rps <rock/paper/scissor>```", inline=True)
            embed.add_field(name="hangman", value="Play Hangman ```/hm <guess>```", inline=True)
            embed.add_field(name="roll", value="Get a random number from any range you want. But Whuay?? ```/roll <max-number> <bet (OPTIONAl)>```", inline=True)
            embed.add_field(name="dice", value="Roll a dice cause you dont have any hobbys. ```/dice <bet (OPTIONAl)>```", inline=True)
            embed.add_field(name="coinflip", value="Just flip a coin (i dont know whuay you would). ```/coinflip/coin <bet (OPTIONAl)>```", inline=True)
            embed.set_footer(text="For help feel free to join this discord server: https://discord.gg/5WfYJje")
            await ctx.send(embed=embed)

        elif arg != None and arg.lower() == "reddit":
            #sending calledNUM Metric to influxdb.py
            global calledHelpReddit, calledHelpRedditH
            com = "helpReddit"
            calledHelpReddit += 1
            calledHelpRedditH[0] += 1

            sendingCom(cog, com, calledHelpReddit)

            embed = discord.Embed(colour=0xA8FFD5, title="Help for reddit commands :art:")
            embed.add_field(name="meme", value="Get a random piece of content from r/memes ```/meme```", inline=True)
            embed.add_field(name="wholesome", value="Get a random piece of content from r/wholesomememes```/wholesome```", inline=True)
            embed.add_field(name="wholesome", value="Get a random piece of content from r/wtfstock```/stock```", inline=True)
            embed.set_footer(text="For help feel free to join this discord server: https://discord.gg/5WfYJje")
            await ctx.send(embed=embed)

        else:
            #sending calledNUM Metric to influxdb.py
            global calledHelp, calledHelpH
            com = "helpGeneral"
            calledHelp += 1
            calledHelpH[0] += 1

            sendingCom(cog, com, calledHelp)

            embed = discord.Embed(colour=discord.Colour.green(), title="Help commands")
            embed.add_field(name="animals :duck:", value="```/help animals```", inline=True)
            embed.add_field(name="basic :teddy_bear:", value="```/help basic```", inline=True)
            embed.add_field(name="fun :microbe:", value="```/help fun```", inline=True)
            embed.add_field(name="games :video_game:", value="```/help games```", inline=True)
            embed.add_field(name="reddit :camera_with_flash:", value="```/help reddit```", inline=True)
            embed.set_footer(text="For help feel free to join this discord server: https://discord.gg/5WfYJje")
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