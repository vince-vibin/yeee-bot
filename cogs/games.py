from discord.ext import commands

import discord

from rps.converter import RockPaperScissorsConverter
import random
from rps.model import RPS

from hangman.model import Hangman
from hangman.controller import HangmanGame

user_guesses = list()
hangman_games = {}

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Play Rock, Paper, Scissors against your friend replacement.",brief="Play Rock, Paper, Scissors against your friend replacement.") # Rock, Paper, Scissors game
    async def rps(self, ctx, user_choice:RockPaperScissorsConverter): # used controller.py and model.py in rps/
        rps_m = RPS()
        bot_choice = random.choice(rps_m.get_choices()) # getting random choice form rps/model.py closs RPS
        user_choice = user_choice.choice

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
                colour=0xFFFB00
                titel="Oof"
                message="Thats a close one, cunt!"
            elif won is True: # bot has won
                colour=0xFF0000
                titel="Hahahaha"
                message="Your sutch a Noob go cry to your momma"
            elif won is False: # bot has lost
                colour=0x13FF00
                titel="F A C K"
                message="I am defeated. Now I'm going to cry over there"

            embed = discord.Embed(colour=colour)
            embed.add_field(name=bot_choice, value=message, inline=False)
            await ctx.send(embed=embed)

        # send error when user_choice = None

    @commands.command(aliases=['hm'], description="Play Hangman against your friend replacement.", brief="Play Hangman against your friend replacement.") # the hangman game
    async def hangman(self, ctx, guess: str): # used controller.py and model.py in hangman/ 
        player_id = ctx.author.id
        hangman_instance = HangmanGame()
        game_over, won = hangman_instance.run(player_id, guess)

        if game_over:
            colour=0xFF0000
            titel="Hahahahahahah, you fucking lost"
            game_over_message = "You fucking shit. You wont reach anything in your life."
            if won:
                colour=0x13FF00
                titel="Hey look at that!"
                game_over_message = "You just reached something in your life congrats."

            game_over_message = game_over_message + \
                " The word was %s" % hangman_instance.get_secret_word()

            await hangman_instance.reset(player_id)
            
            embed = discord.Embed(colour=colour)
            embed.add_field(name=titel, value=game_over_message, inline=False)
            await ctx.send(embed=embed)

        else:
            colour=0x00FFEC
            embed = discord.Embed(colour=colour)
            embed.add_field(name="Progress:", value=hangman_instance.get_progress_string(), inline=False)
            embed.add_field(name="Guesses so far:", value=hangman_instance.get_guess_string(), inline=False)
            await ctx.send(embed=embed)
    
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
    bot.add_cog(Games(bot))