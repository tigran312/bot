import discord
from discord.ext import commands
import os
import random 


intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
decomposition = {"пластик":"450 лет", "жвачка": "35 лет", "фольга":"100 лет", "сигарета":"15 лет"}
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def разложение(ctx, obg = ""):
    if  obg.lower() in decomposition:
        await ctx.send(f"{obg} разлагается {decomposition[obg]}")
         

    
















bot.run()