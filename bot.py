import os
import discord
import asyncio
import random
from discord.ext import commands


bot = commands.Bot("+")

@bot.event
async def on_ready():
    print('Survival Items is on!')

class Main_Commands():
    def __init__(self, bot):
        self.bot

@bot.command(pass_context=True, no_pm=True)
async def sft(ctx):
    """You search for trees"""
    await bot.say(random.choice(["**You found 1 log and 2 sticks**","**You found 2 logs and 1 sticks**","**You found 3 logs and 3 sticks**","You found 4 logs and 8 sticks","You found 5 logs and 6 sticks","You found 6 logs and 9 sticks"]))

@bot.group(aliases=["ci"], pass_context=True, no_pm=True)
async def craftitem(ctx):
    """Craft an item"""
    if ctx.invoked_subcommand is None:
        await bot.say("Do +help craftitem for help!")

@craftitem.command(name="wp", pass_context=True)
async def ci_wp(ctx):
    """Crafts a wooden pickaxe"""
    await bot.say("You crafted a wooden pickaxe")

@craftitem.command(name="ia", pass_context=True)
async def ci_ia(ctx):
    """Crafts an iron axe"""
    await bot.say("You crafted an iron axe")

@craftitem.command(name="sp", pass_context=True)
async def ci_sp(ctx):
    """Crafts a stone pickaxe"""
    await bot.say("You crafted a stone pickaxe")

@craftitem.command(name="sa", pass_context=True)
async def ci_sa(ctx):
    """Crafts a stone axe"""
    await bot.say("You crafted a stone axe")

@craftitem.command(name="ws", pass_context=True)
async def ci_ws(ctx):
    """Crafts a wooden sword"""
    await bot.say("You crafted a wooden sword")

@craftitem.command(name="is", pass_context=True)
async def ci_is(ctx):
    """Crafts an iron sword"""
    await bot.say("You crafted an iron sword")

@craftitem.command(name="ss", pass_context=True)
async def ci_ss(ctx):
    """Crafts a stone sword"""
    await bot.say("You crafted a stone sword")

@bot.command(pass_context=True)
async def info(ctx):
    """Shows an info about Survival Items!"""
    await bot.say("```--Info-- \n",
                  "Made by: Diru#1601 \n",
                  "I will update the bot when Misten updates the server```")

@bot.command(pass_context=True)
async def change_log(ctx):
    """Shows the bot change log"""
    await bot.say("```Update 1.0 \n",
                  "Added craftitem command \n",
                  "And sft command```")

bot.run("NDI5NTg4ODU5ODc4MTEzMjgw.DaEkeg.0CMTUqXBYOubD75NjHQZX-E_aOI")
