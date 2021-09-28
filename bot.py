import asyncio

import discord
import os

from discord.ext import commands
from dotenv import load_dotenv
from discord.ext.commands import has_any_role
from pathlib import Path

basepath = Path()
basedir = str(basepath.cwd())
envars = basepath.cwd() / '.env'
load_dotenv(envars)
token = os.getenv('discord_token')
prefix = os.getenv('bot_prefix')
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
cogs = ['cogs.appeal_responses']


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="zeppelin.gg"))
    print('{0.user} is now ready!'.format(bot))
    bot.remove_command('help')
    for cog in cogs:
        bot.load_extension(cog)
    return

@bot.command()
@has_any_role(758104829242507294, 886986131164520518)
async def pingapp(ctx):
    await ctx.send('**Pong!** {0}'.format(round(bot.latency, 1)))

bot.run(token)
