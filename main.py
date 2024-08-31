import discord
from discord.ext import commands
import os
import random 
mems = os.listdir("img")

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx, img = 0):
    if 1 <= img <= len(mems):
        with open(f"img/{mems[img -1]}","rb") as f :
            imgd = discord.File(f)
    else: 
        with open(f"img/{random.choice(mems)}","rb") as f :
            imgd = discord.File(f)
    await ctx.send(file = imgd)
    
@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run()