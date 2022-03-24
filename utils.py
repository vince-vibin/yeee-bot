import json
import os
from settings import *
import random
from discord.ext import commands

async def get_yoomum_joke():
    with open(os.path.join(DATA_DIR, "yoomum.json"), encoding='utf-8') as yoomum_file:
        yoomum = json.load(yoomum_file)
    random_category = random.choice(list(yoomum.keys()))
    yoomum = random.choice(list(yoomum[random_category]))
    return yoomum

async def get_wisdom():
    with open(os.path.join(DATA_DIR, "kanyerest.json"), encoding='utf-8') as wisdom_file:
        wisdom = json.load(wisdom_file)
    wisdom = random.choice(list(wisdom))
    return wisdom

async def get_answers():
    with open(os.path.join(DATA_DIR, "8ball.json"), encoding='utf-8') as answers_file:
        answers = json.load(answers_file)
    random_category = random.choice(list(answers.keys()))
    answers = random.choice(list(answers[random_category]))
    return answers
