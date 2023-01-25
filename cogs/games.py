from discord.ext import commands, tasks
from discord import app_commands
import discord

from rps.converter import RockPaperScissorsConverter
import random
from rps.model import RPS

from hangman.model import Hangman
from hangman.controller import HangmanGame

user_guesses = list()
hangman_games = {}

# setting global var for Embed-Color
global colorEmbed 
colorEmbed = 0xFFFB00

#vars for calling sending func
from influx.influxdbExport import sendingCom, sendingH
global cog

cog = "games"
calledRPS = 0
calledHangman = 0
calledRoll = 0
calledDice = 0
calledCoinflip = 0

calledRPSH = [0, "rps", cog] 
calledHangmanH = [0, "hangman", cog]
calledRollH = [0, "roll", cog]
calledDiceH = [0, "dice", cog]
calledCoinflipH = [0, "coinflip", cog]


class Games(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot

    @app_commands.command(name="rps", description="play rock paper scissors against me") # Rock, Paper, Scissors game
    async def rps(interaction: discord.Interaction, user_choice: str) -> None: # used controller.py and model.py in rps/
        rps_m = RPS()
        bot_choice = random.choice(rps_m.get_choices()) # getting random choice form rps/model.py class RPS
        user_choice = user_choice.lower()

        if user_choice is not None: # just magic
            winner_check = { # compairing choices 
                (RPS.ROCK, RPS.PAPER): False,
                (RPS.ROCK, RPS.SCISSOR): False,
                (RPS.PAPER, RPS.ROCK): True,
                (RPS.PAPER, RPS.SCISSOR): False,
                (RPS.SCISSOR, RPS.ROCK): False,
                (RPS.SCISSOR, RPS.PAPER): True,
            }

            won = None
            if bot_choice == user_choice: # if choices are the same won = None
                won = None
            else:
                won = winner_check[(bot_choice, user_choice)]

            if won is None: # sending if choices are the same
                colour=colorEmbed
                message="Thats a close one, cunt! :cold_face: :cold_face:"
            elif won is True: # bot has won
                colour=colorEmbed
                message="Your a noob go cry to your momma :skull: :skull:"
            elif won is False: # bot has lost
                colour=colorEmbed
                message="I am defeated. :sleepy: :sleepy:"

            #sending calledNUM Metric to influxdb.py
            global calledRPS, calledRPSH
            com = "rps"
            calledRPS += 1
            calledRPSH[0] += 1

            sendingCom(cog, com, calledRPS)

            emoji = {"rock": ":rock:", "paper": ":roll_of_paper:", "scissors": ":scissors:"}

            embed = discord.Embed(colour=colour)
            embed.add_field(name="your choice", value="{} {}".format(user_choice, emoji[user_choice]), inline=True)
            embed.add_field(name="my choice", value="{} {}".format(bot_choice, emoji[bot_choice]), inline=True)
            embed.add_field(name="Conclusion", value=message, inline=False)
            await interaction.response.send_message(embed=embed, ephemeral=False)


    @app_commands.command(name="hangman", description="play hangman") # the hangman game
    async def hangman(interaction: discord.Interaction, guess: str) -> None: # used controller.py and model.py in hangman/ 
        player_id = interaction.user.id
        hangman_instance = HangmanGame()
        game_over, won = hangman_instance.run(player_id, guess)

        #sending calledNUM Metric to influxdb.py
        global calledHangman, calledHangmanH
        com = "hangman"
        calledHangman += 1
        calledHangmanH[0] += 1

        sendingCom(cog, com, calledHangman)

        if game_over:
            titel="Hahahahahahah, you fucking lost"
            game_over_message = "You fucking shit. You wont reach anything in your life."
            if won:
                titel="Hey look at that!"
                game_over_message = "You just reached something in your life congrats."

            game_over_message = game_over_message + \
                " The word was %s" % hangman_instance.get_secret_word()

            await hangman_instance.reset(player_id)
            
            embed = discord.Embed(colour=colorEmbed)
            embed.add_field(name=titel, value=game_over_message, inline=False)
            await interaction.response.send_message(embed=embed, ephemeral=False)

        else:
            embed = discord.Embed(colour=colorEmbed)
            embed.add_field(name="Progress:", value=hangman_instance.get_progress_string(), inline=False)
            embed.add_field(name="Guesses so far:", value=hangman_instance.get_guess_string(), inline=False)
            await interaction.response.send_message(embed=embed, ephemeral=False)
    
    @app_commands.command(name="roll", description="roll a random number from 0 to n (maybe even bet on one)")
    async def roll(interaction: discord.Interaction, range: int, bet: int = None) -> None:

        #sending calledNUM Metric to influxdb.py
        global calledRoll, calledRollH
        com = "roll"
        calledRoll += 1
        calledRollH[0] += 1

        sendingCom(cog, com, calledRoll)

        if range > 1:
            n = random.randrange(1, range)
            if bet != None:
                if bet < range: 
                    if bet == n: 
                        embed = discord.Embed(colour=colorEmbed)
                        embed.add_field(name="You got: ", value=n, inline=True)
                        embed.add_field(name="From a range between 1 and : ", value=range, inline=True)
                        embed.add_field(name="Your bet was: ", value=bet, inline=True)
                        embed.add_field(name="Conclusion: ", value="You fucking did it you finally achieved something in your life", inline=False)
                        embed.set_footer(text="Now move on with your live and get hobbys.")
                        await interaction.response.send_message(embed=embed, ephemeral=False)
                    else: 
                        embed = discord.Embed(colour=colorEmbed)
                        embed.add_field(name="You got: ", value=n, inline=True)
                        embed.add_field(name="From a range from 1 to: ", value=range, inline=True)
                        embed.add_field(name="Your bet was: ", value=bet, inline=True)
                        embed.add_field(name="Conclusion: ", value="You're a loser. And will have gambeling issues in your life", inline=False)
                        embed.set_footer(text="Now move on with your live and get hobbys.")
                        await interaction.response.send_message(embed=embed, ephemeral=False)
                else:
                    embed = discord.Embed(colour=colorEmbed)
                    embed.add_field(name="Idiot", value="Your bet cant be higher then your range. OBVIOSLY ", inline=False)
                    embed.set_footer(text="Try again")
                    await interaction.response.send_message(embed=embed, ephemeral=False)
            else:
                embed = discord.Embed(colour=colorEmbed)
                embed.add_field(name="You got: ", value=n, inline=True)
                embed.add_field(name="From a range from 1 to: ", value=range, inline=True)
                embed.add_field(name="Conclusion: ", value="I dont care", inline=False)
                embed.set_footer(text="Now move on with your live and get hobbys.")
                await interaction.response.send_message(embed=embed, ephemeral=False)
        else:
            embed = discord.Embed(colour=colorEmbed)
            embed.add_field(name="Idiot", value="Range has to be higher then 1. OBVIOSLY ", inline=False)
            embed.set_footer(text="Try again")
            await interaction.response.send_message(embed=embed, ephemeral=False) 

    @app_commands.command(name="dice", description="roll a dice (maybe even bet on a number)")
    async def dice(interaction: discord.Interaction, bet: int = None) -> None:
        n = random.randrange(1, 6)

        #sending calledNUM Metric to influxdb.py
        global calledDice, calledDiceH
        com = "dice"
        calledDice += 1
        calledDiceH[0] += 1

        sendingCom(cog, com, calledDice)

        if bet != None:
            if bet > 6:
                embed = discord.Embed(colour=colorEmbed)
                embed.add_field(name="Idiot", value="Your bet cant be higher then your 6. OBVIOSLY ", inline=False)
                embed.set_footer(text="Try again")
                await interaction.response.send_message(embed=embed, ephemeral=True) 
            else:
                if n == bet:
                    embed = discord.Embed(colour=colorEmbed)
                    embed.add_field(name="You got: ", value=n, inline=True)
                    embed.add_field(name="Your bet was: ", value=bet, inline=True)
                    embed.add_field(name="Conclusion: ", value="You fucking did it you finally achieved something in your life", inline=False)
                    embed.set_footer(text="Now move on with your live and get hobbys.")
                    await interaction.response.send_message(embed=embed, ephemeral=True) 
                else:
                    embed = discord.Embed(colour=colorEmbed)
                    embed.add_field(name="You got: ", value=n, inline=True)
                    embed.add_field(name="Your bet was: ", value=bet, inline=True)
                    embed.add_field(name="Conclusion: ", value="You're a loser. And will have gambeling issues in your life", inline=False)
                    embed.set_footer(text="Now move on with your live and get hobbys.")
                    await interaction.response.send_message(embed=embed, ephemeral=False) 
        else:
            embed = discord.Embed(colour=colorEmbed)
            embed.add_field(name="You rolled a:", value=n, inline=False)
            embed.set_footer(text="Now move on with your live and get hobbys.")
            await interaction.response.send_message(embed=embed, ephemeral=False) 

    @app_commands.command(name="coin", description="flip a coin (maybe even bet on one)")
    async def coin(interaction: discord.Interaction, bet : int = None):

        #sending calledNUM Metric to influxdb.py
        global calledCoinflip, calledCoinflipH
        com = "coinflip"
        calledCoinflip += 1
        calledCoinflipH[0] += 1

        sendingCom(cog, com, calledCoinflip)
        side = random.choice(('heads', 'tails'))

        if bet == None:
            embed = discord.Embed(colour=colorEmbed)
            embed.add_field(name="You flipped: " + side, value="I really dont care why tho", inline=False)
            embed.set_footer(text="Now move on with your live and get hobbys.")
            await interaction.response.send_message(embed=embed, ephemeral=False)
        else:
            if bet.lower() == "heads" or bet.lower() == "tails":
                if side == bet:
                    embed = discord.Embed(colour=colorEmbed)
                    embed.add_field(name="You flipped: " + side, value="You fucking did it you finally achieved something in your life", inline=False)
                    embed.set_footer(text="Now move on with your live and get hobbys.")
                    await interaction.response.send_message(embed=embed, ephemeral=False)
                else:
                    embed = discord.Embed(colour=colorEmbed)
                    embed.add_field(name="You flipped: " + side, value="You're a loser. And will have gambeling issues in your life", inline=False)
                    embed.set_footer(text="Now move on with your live and get hobbys.")
                    await interaction.response.send_message(embed=embed, ephemeral=False)
            else:
                embed = discord.Embed(colour=colorEmbed)
                embed.add_field(name="Idiot", value="You have to bet on heads or tails", inline=False)
                embed.set_footer(text="Try again")
                await interaction.response.send_message(embed=embed, ephemeral=False)
    
    @tasks.loop(hours=1)
    async def exporterH():
        global calledRPSH, calledHangmanH, calledRollH, calledDiceH, calledCoinflipH
        send = [calledRPSH, calledHangmanH, calledRollH, calledDiceH, calledCoinflipH]
        i = 0

        while i < len(send): #looping throught send array
            sendingH(send[i])
            i = i + 1

        calledRPSH[0] = 0 #reseting all values 
        calledHangmanH[0] = 0
        calledRollH[0] = 0
        calledDiceH[0] = 0
        calledCoinflipH[0] = 0
        
    exporterH.start()

    bot.tree.add_command(rps, override=True)
    bot.tree.add_command(hangman, override=True)
    bot.tree.add_command(roll, override=True)
    bot.tree.add_command(dice, override=True)
    bot.tree.add_command(coin, override=True)

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Games(bot))